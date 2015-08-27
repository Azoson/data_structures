{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'dst',
      'product_name': 'dst',
      'type': 'static_library',
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
