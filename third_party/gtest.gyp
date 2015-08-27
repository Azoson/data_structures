#
# gtest.gyp
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
    '../build/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'gtest',
      'type': 'static_library',
      'sources': [
        './googletest/googletest/include/gtest/gtest-death-test.h',
        './googletest/googletest/include/gtest/gtest-message.h',
        './googletest/googletest/include/gtest/gtest-param-test.h',
        './googletest/googletest/include/gtest/gtest-printers.h',
        './googletest/googletest/include/gtest/gtest-spi.h',
        './googletest/googletest/include/gtest/gtest-test-part.h',
        './googletest/googletest/include/gtest/gtest-typed-test.h',
        './googletest/googletest/include/gtest/gtest.h',
        './googletest/googletest/include/gtest/gtest_pred_impl.h',
        './googletest/googletest/include/gtest/gtest_prod.h',
        './googletest/googletest/include/gtest/internal/gtest-death-test-internal.h',
        './googletest/googletest/include/gtest/internal/gtest-filepath.h',
        './googletest/googletest/include/gtest/internal/gtest-internal.h',
        './googletest/googletest/include/gtest/internal/gtest-linked_ptr.h',
        './googletest/googletest/include/gtest/internal/gtest-param-util-generated.h',
        './googletest/googletest/include/gtest/internal/gtest-param-util.h',
        './googletest/googletest/include/gtest/internal/gtest-port.h',
        './googletest/googletest/include/gtest/internal/gtest-string.h',
        './googletest/googletest/include/gtest/internal/gtest-tuple.h',
        './googletest/googletest/include/gtest/internal/gtest-type-util.h',
        './googletest/googletest/src/gtest-death-test.cc',
        './googletest/googletest/src/gtest-filepath.cc',
        './googletest/googletest/src/gtest-internal-inl.h',
        './googletest/googletest/src/gtest-port.cc',
        './googletest/googletest/src/gtest-printers.cc',
        './googletest/googletest/src/gtest-test-part.cc',
        './googletest/googletest/src/gtest-typed-test.cc',
        './googletest/googletest/src/gtest.cc',
      ],
      'include_dirs': [
        './googletest/googletest',
        './googletest/googletest/include',
      ],
      'direct_dependent_settings': {
        'defines': [
          'UNIT_TEST',
        ],
        'include_dirs': [
          './googletest/googletest/include',
        ],
      },
    },
    {
      'target_name': 'gtest_main',
      'type': 'static_library',
      'dependencies': [
        'gtest',
      ],
      'sources': [
        './googletest/googletest/src/gtest_main.cc',
      ],
      'direct_dependent_settings': {
        'ldflags': [
          '-pthread',
        ],
      },
    },
  ],
}
