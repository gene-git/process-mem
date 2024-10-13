#!/usr/bin/python
"""
Display memory usage for process(es)
"""
# pylint: disable=invalid-name
import sys
import getpass
import argparse
import textwrap
import re
from typing import (List, Dict, Optional)
from pydantic import BaseModel
from lib import version

def _help_epilog():
    """ add to help listing """
    epilog = textwrap.dedent('''\
            Input
              Determines which processes are included.
              User can be any user or :all: for all users. Current user by default.
              Process Names limit the output to those processes.
                If none provided, then all processes are included that match user.
              Process names may may use regex expressions.

            Output
              1 row per process with each row :
                name : [num] rss vms shr
                    name is name of process
                    rss is resident set size
                    vms is virtual memory size
                    shr is memory (potentially) shared with other processes
                    slib is shared library memory (full report)
                    dirty is the number of dirty pages (full report)
             ''')
    return epilog

def likely_regex(name):
    """
    Do our best to guess if the process name is a regex
    """
    regex_chars = r'.^$*+?{}[]|()\\'
    return any(char in name for char in regex_chars)

class Opts(BaseModel):
    """
    Arguments for ProcInfo
    """
    pnames: Optional[List[str]] = []
    is_regex: Optional[Dict] = {}
    regex_comp: Optional[Dict] = {}
    ignore_case: Optional[bool] = False
    current_user: Optional[str] = None
    user: Optional[str] = None
    full: Optional[bool] = False
    vers: Optional[bool] = False
    sort_mem: Optional[bool] = False
    sort_rev: Optional[bool] = False

    def __init__(self):
        super().__init__()
        self.current_user = getpass.getuser()
        self.user = self.current_user

        epilog = _help_epilog()
        par = argparse.ArgumentParser(description='Show Process(es) Memory', epilog=epilog,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)

        ahelp = f'username or :all: default ({self.user})'
        par.add_argument('-u', '--user', default=self.user, help=ahelp)

        ahelp = f'Full report adds shared lib and dirty pages ({self.full})'
        par.add_argument('-f', '--full', help=ahelp, action='store_true', default=self.full)

        ahelp = f'Case insensitive process names match({self.ignore_case})'
        par.add_argument('-i', '--ignore-case', help=ahelp, action='store_true', default=self.ignore_case)

        ahelp = 'Display version'
        par.add_argument('-v', '--vers', help=ahelp, action='store_true', default=self.ignore_case)

        ahelp = 'Sort by resident memory use instead of process name'
        par.add_argument('-sm', '--sort-mem', help=ahelp, action='store_true', default=self.sort_mem)

        ahelp = 'Sort in reverse order'
        par.add_argument('-sr', '--sort-rev', help=ahelp, action='store_true', default=self.ignore_case)

        ahelp = 'process names to check (all processes if not provided)'
        par.add_argument('pnames', nargs='*', help=ahelp)

        parsed = par.parse_args()
        if parsed:
            for (opt, val) in vars(parsed).items():
                setattr(self, opt, val)

        # check process names for regex
        for name in self.pnames:
            self.is_regex[name] = likely_regex(name)

            if self.is_regex[name] :
                regex = name
            else:
                regex = fr'^{name}$'

            if self.ignore_case:
                self.regex_comp[name] = re.compile(regex, re.IGNORECASE)
            else:
                self.regex_comp[name] = re.compile(regex)

        if self.user != self.current_user:
            print(f'Checking process mem for: {self.user}')

        if self.vers:
            print(version())
            sys.exit()
