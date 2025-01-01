# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2024-present  Gene C <arch@sapience.com>
"""
units utilities
"""

def bytes2human(byts):
    """
    Map Bytes to human units
      - K, G, etc
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}

    # prefix = 1024, 1024^2, 1024^3 ...
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10

    # work from largest to smallest unit
    for s in reversed(symbols):
        if abs(byts) >= prefix[s]:
            value = float(byts) / prefix[s]
            return f'{value:.1f}{s}'
    return f'{byts}B'

def number2metric(num):
    """
    Map number to SI (metric)
      - k, g, etc
    """
    symbols = ('k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {
            'k' : 1000,
            'M' : 1000_000,
            'G' : 1000_000_000,
            'T' : 1000_000_000_000,
            'P' : 1000_000_000_000_000,
            'E' : 1000_000_000_000_000_000,
            'Z' : 1000_000_000_000_000_000_000,
            'Y' : 1000_000_000_000_000_000_000_000,
            }

    # work from largest to smallest unit
    for s in reversed(symbols):
        if abs(num) >= prefix[s]:
            value = float(num) / prefix[s]
            return f'{value:.1f}{s}'
    return f'{num}'
