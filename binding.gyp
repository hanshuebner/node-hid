{
   'variables': {
      'driver%': 'libusb'
  },
  'targets': [
    {
      'target_name': 'hidapi',
      'type': 'static_library',
      'conditions': [
        [ 'OS=="mac"', {
          'sources': [ 'hidapi/mac/hid.c' ],
          'include_dirs+': [
            '/usr/include/libusb-1.0/'
          ]
        }],
        [ 'OS=="linux"', {
          'conditions': [
            [ 'driver=="libusb"', {
              'sources': [ 'hidapi/linux/hid-libusb.c' ],
              'include_dirs+': [
                '/usr/include/libusb-1.0/'
              ]
            }],
            [ 'driver=="hidraw"', {
              'sources': [ 'hidapi/linux/hid.c' ]
            }]
          ]
        }],
        [ 'OS=="win"', {
          'sources': [ 'hidapi/windows/hid.c' ],
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                'setupapi.lib',
              ]
            }
          }
        }]
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'hidapi/hidapi'
        ]
      },
      'include_dirs': [
        'hidapi/hidapi'
      ],
      'defines': [
        '_LARGEFILE_SOURCE',
        '_FILE_OFFSET_BITS=64',
      ],
      'cflags': ['-g'],
      'cflags!': [
        '-ansi'
      ]
    },
    {
      'target_name': 'HID',
      'sources': [ 'src/HID.cc' ],
      'dependencies': ['hidapi'],
      'defines': [
        '_LARGEFILE_SOURCE',
        '_FILE_OFFSET_BITS=64',
      ],
      'conditions': [
        [ 'OS=="mac"', {
          'ldflags': [
            '-framework',
            'IOKit',
            '-framework',
            'CoreFoundation'
          ]
        }],
        [ 'OS=="linux"', {
          'conditions': [
            [ 'driver=="libusb"', {
              'ldflags': [
                '-lusb-1.0'
              ]
            }],
            [ 'driver=="hidraw"', {
              'ldflags': [
                '-ludev',
                '-lusb-1.0'
              ]
            }]
          ],
        }],
        [ 'OS=="win"', {
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                'setupapi.lib'
              ]
            }
          }
        }]
      ],
      'cflags': ['-g'],
      'cflags!': [
        '-ansi'
      ],
      'cflags_cc!': [ '-fno-exceptions' ]
    }
  ]
}