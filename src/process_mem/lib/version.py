# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2024-present Gene C <arch@sapience.com>
"""
Project process-mem
"""

__version__ = "1.6.0"
__date__ = "2026-02-07"
__reldev__ = "release"
__githash__ = 'none'


def version() -> str:
    """ report version and release date """
    vers = f'process-mem: version {__version__} ({__date__})'
    return vers
