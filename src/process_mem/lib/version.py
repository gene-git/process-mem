# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
Project process-mem
"""

__version__ = "0.9.1"
__date__ = "2024-09-27"
__reldev__ = "release"
__githash__ = 'none'

def version() -> str:
    """ report version and release date """
    vers = f'wg-tool: version {__version__} ({__date__} commit {__githash__})'
    return vers
