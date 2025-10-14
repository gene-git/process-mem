# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2024-present  Gene C <arch@sapience.com>
"""
Project process-mem
"""

__version__ = "1.4.1"
__date__ = "2025-10-14"
__reldev__ = "release"
__githash__ = 'none'


def version() -> str:
    """ report version and release date """
    vers = f'process-mem: version {__version__} ({__date__})'
    return vers
