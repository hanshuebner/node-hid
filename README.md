# node-hid - Access USB HID devices from node.js #

Installation
------------

### Prerequisites:

* Mac OS (I use 10.6.8) or Linux (kernel 2.6+ that support libusb-1.0) or Windows XP+
* node.js v0.6
* libusb-1.0 (Linux-only)

### Windows-only

Copy the HID.node file from build/win into your node_modules folder.

### Compile from Source

Pull the required submodule:

```
$ git submodule init
$ git submodule update
```
 Build the extension using node-gyp:

```
$ node-gyp rebuild
```

Or build the extension using node-waf:

```
$ cd src/
$ node-waf configure build
```


How to Use
----------

List devices:
(see show-devices.js)

```
HID.devices();
[ { vendorId: 1452,
    productId: 595,
    path: 'USB_05ac_0253_0x100a148e0',
    serialNumber: '',
    manufacturer: 'Apple Inc.',
    product: 'Apple Internal Keyboard / Trackpad',
    release: 280,
    interface: -1 },
  { vendorId: 1452,
    productId: 595,
    path: 'USB_05ac_0253_0x100a14e20',
    serialNumber: '',
    manufacturer: 'Apple Inc.',
    product: 'Apple Internal Keyboard / Trackpad',
    release: 280,
    interface: -1 },
<and more>
```

Use device:
```
var device = new HID.HID(path);
device.read(function(error, data){}); //async read
device.write([0x00, 0x01, 0x01, 0x05, 0xff, 0xff]);
```

If you need help, send me an email (hans.huebner@gmail.com)
