#
# data-structures.gyp
#
# Copyright (c) 2015, Makoto Shimazu
# All rights reserved.
#  
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#  
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#  
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#  
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'dst',
      'product_name': 'dst',
      'type': 'static_library',
      'cflags': ['-std=gnu99',],
      'sources':
      [
        '../src/btree/btree.c'
      ],
    },
    {
      'target_name': 'btree',
      'product_name': 'btree.bin',
      'type': 'executable',
      'sources':
      [
        '../src/btree/main.c',
      ],
      'dependencies': [
        'dst',
      ]
    },
    {
      'target_name': 'btree_unittest',
      'product_name': 'btree_unittest.bin',
      'type': 'executable',
      'sources':
      [
        '../src/btree/test.cpp',
      ],
      'dependencies': [
        'dst',
        '<(DEPTH)/third_party/gtest.gyp:gtest',
        '<(DEPTH)/third_party/gtest.gyp:gtest_main',
      ],
      'cflags': [
        '-std=c++11',
      ]
    },
  ]
}
