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
