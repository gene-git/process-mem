# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
Project process-mem
"""

__version__ = "1.2.0"
__date__ = "2024-10-13"
__reldev__ = "release"
__githash__ = 'none'

def version() -> str:
    """ report version and release date """
    vers = f'process-mem: version {__version__} ({__date__})'
    return vers
