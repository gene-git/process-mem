# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2024-present Gene C <arch@sapience.com>
"""
Project process-mem
"""

__version__ = "1.7.1"
__date__ = "2026-09-08"
__reldev__ = "release"
__githash__ = "b518f574d7"


def version() -> str:
    """ report version and release date """
    vers = f'process-mem: version {__version__} ({__date__})'
    return vers
