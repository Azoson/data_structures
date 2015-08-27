{
  'target_defaults': {
    'default_configuration': 'Release',
    'configurations': {
      'Debug': {
        'defines':['DEBUG=1'],
        'cflags': ['-g', '-O0', '-W', '-Wall'],
        'include_dirs': ['../inc']
      }, # Debug
      'Release': {
        'cflags': ['-O3', '-W', '-Wall'],
        'include_dirs': ['../inc']
      }, # Release
    }, # configurations
  }, # target_defaults
}
