#
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
#

project('process-mem', ['c'],
  version: files('src/version.txt'),
  meson_version: '>=1.10.0',
  default_options: [
    'c_std=c23',
    'warning_level=3',
    'b_pie=true',
    'prefix=/usr',
    'mandir=share/man',
    ],
)

d_etc = get_option('sysconfdir')
d_lib = get_option('libdir')
d_bin = get_option('bindir')
d_man = get_option('mandir')
d_share = get_option('datadir')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
proj_root = meson.project_source_root()
py_dep = py.dependency(embed: true)

inc_dir = []
lib_sources = []

#
# top-level files
#

#
# Python submodules
#
subdir('src/process_mem')

#
# Deps
#

#
# Executables
#
configure_file(
  input: 'src/process_mem/apps/process-mem.py',
  output: 'process-mem',
  copy: true,
  install_dir: d_bin,
  install_mode: 'rwxr-xr-x'
)


#
# Install
#

s_license = 'src/data/license'
s_changelog = 'src/data/changelog'
s_man = 'src/data/man'

# 
# /usr/man/man1/
# 
install_data(
  [
    s_man / 'man1' / 'process-mem.1.gz',
  ],
  install_dir: d_man / 'man1'
)

# 
# /usr/share/pyconcurrent 
# 
install_data(
  [
    'README.rst',
    s_changelog / 'Changelog.rst',
    'packaging/Changelog',
  ],
  install_dir: d_share / 'process-mem'
)

# 
# /usr/share/licenses/pyconcurrent 
# 
install_data(
  [
    s_license / 'License-gpl-2.0.txt',
    s_license / 'License.rst',
  ],
  install_dir: d_share / 'licenses/process-mem'
)

#
# Tests
#

