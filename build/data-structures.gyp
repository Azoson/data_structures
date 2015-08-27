{
  'includes': [
    'common.gypi',
  ],
  'targets': [
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
      'target_name': 'dst',
      'product_name': 'dst',
      'type': 'static_library',
      'sources':
      [
        '../src/btree/btree.c'
      ],
    },
  ]
}
