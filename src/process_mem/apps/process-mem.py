#!/usr/bin/python
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2024-present Gene C <arch@sapience.com>
"""
Display memory usage for process(es)
"""
# pylint: disable=invalid-name
from process_mem.lib import ProcInfo


def main():
    """
    Get process info for process(es)
     - Optional input is process name(s)
    """
    proc_info = ProcInfo()
    proc_info.show_info()


if __name__ == '__main__':
    main()
