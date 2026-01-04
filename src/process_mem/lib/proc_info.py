# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2024-present Gene C <arch@sapience.com>
"""
Display memory usage for process(es)
"""
# pylint: disable=invalid-name
from typing import Any
import psutil

from .opts import Opts
from .units import (bytes2human, number2metric)


class MemInfo():
    """ process memory data """
    name: str = ''
    num: int = 0
    rss: int = 0
    vms: int = 0
    shared: int = 0
    slib: int = 0
    dirty: int = 0

    def add(self, num: int, rss: int, vms: int,
            shared: int, slib: int = 0, dirty: int = 0):
        """
        increment the counters for each process
        """
        # pylint: disable=too-many-arguments,too-many-positional-arguments
        self.num += num
        self.rss += rss
        self.vms += vms
        self.shared += shared
        self.slib += slib
        self.dirty += dirty

    def text_units(self):
        """
        return dictionary with each item as text with human units
        """
        info = {'num': number2metric(self.num),
                'rss': bytes2human(self.rss),
                'vms': bytes2human(self.vms),
                'shared': bytes2human(self.shared),
                'slib': bytes2human(self.slib),
                'dirty': number2metric(self.dirty)
                }
        return info


class ProcInfo:
    """
    Mini class to get process info
    """
    def __init__(self):
        self.opts = Opts()

    def show_info(self):
        """
        Pull info matching user and pnames
        """
        opts = self.opts

        summary = self.proc_mem_info()
        if not summary or len(summary) < 1:
            return

        show_total = False
        if len(summary) > 2:
            # length = num_proces names + total
            show_total = True

        hdr = f'{"Proc-Name":>28s} : [num] {"rss":>8s} {"vms":>8s} {"shr":>8s}'
        if opts.full:
            hdr += f' {"slib":>8s} {"dirty":>8s}'
        print(hdr)

        for mem in summary:
            name = mem.name
            info = mem.text_units()

            row = f'[{info['num']:>3s}] {info['rss']:>8s} '
            row += f'{info['vms']:>8s} {info['shared']:>8s}'
            if opts.full:
                row += f' {info['slib']:>8s} {info['dirty']:>8}'

            if mem.name != 'Total' or show_total:
                print(f'{name:>28s} : {row}')

    def proc_mem_info(self) -> list[MemInfo]:
        """
        Retrieve meminfo about each process in pnames
        """
        #
        # Gather the info
        #
        opts = self.opts
        # list[psutil._pslinux.pmem] use Any
        proc_info: dict[str, list[Any]] = {}
        col_names = ['pid', 'username', 'name', 'memory_info']
        for proc in psutil.process_iter(col_names):
            pname = proc.info.get('name')

            if not self._keep_filter(proc):
                continue

            if not proc_info.get(pname):
                proc_info[pname] = []

            #
            # pmem ~ pmem.rss. pmem.vms, pmem.shared
            #
            pmem = proc.info['memory_info']
            proc_info[pname].append(pmem)

        #
        # Summarize
        #
        summary: list[MemInfo] = []
        mem_tot = MemInfo()
        mem_tot.name = 'Total'
        for (name, pmems) in proc_info.items():
            num = len(pmems)
            mem_info = MemInfo()
            mem_info.name = name
            for pmem in pmems:
                mem_info.add(1, pmem.rss, pmem.vms,
                             pmem.shared, pmem.lib, pmem.dirty)

            summary.append(mem_info)
            mem_tot.add(num, mem_info.rss, mem_info.vms, mem_info.shared,
                        mem_info.slib, mem_info.dirty)

        #
        # Sort by process name and keep total at the end
        #
        if len(summary) > 1:
            if opts.sort_mem:
                summary = sorted(summary,
                                 key=lambda meminfo: meminfo.rss,
                                 reverse=opts.sort_rev)
            else:
                summary = sorted(summary,
                                 key=lambda meminfo: meminfo.name.lower(),
                                 reverse=opts.sort_rev)

        summary.append(mem_tot)

        return summary

    def _keep_filter(self, proc: psutil.Process):
        """
        return true if this proc is to be kept
        """
        opts = self.opts
        info: dict[str, Any] = proc.info    # type: ignore[attr-defined]

        # user
        proc_user = info.get('username')
        if opts.user not in (':all:', proc_user):
            return False

        if not opts.pnames:
            return True

        # process name
        proc_name = info.get('name')
        for (_name, regcomp) in opts.regex_comp.items():
            if regcomp.match(proc_name):
                return True

        return False
