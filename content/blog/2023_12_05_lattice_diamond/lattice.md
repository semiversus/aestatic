title: Install Lattice Diamond on Linux
date: 2023-12-05
thumbnail: lattice_tb.jpg
english: true

Do you have troubles with segmentation faults using Diamond on your Linux computer? Lattice is providing a Linux installation for Diamond [here](https://www.latticesemi.com/latticediamond).

Starting Diamond in the console I saw following output when starting various tools like "Spreadsheet View" or "Package View":
```console
$ diamond
Use of deprecated SAXv1 function comment
Segmentation fault (core dumped)
```

## Fedora
To get Diamond running on Fedora (tested on Fedora 39) use libxml2 in version 2.10.4:

```console
$ git clone https://github.com/GNOME/libxml2.git
  ...
$ cd libxml2
$ git checkout v2.10.4
$ ./autogen.sh
  ...
$ ./make
  ...
$ sudo make install
  ...
```

The libary will be installed in `/usr/local/lib` (at least here on Fedora 39).

Now add the path to `/usr/local/lib` in two instances in the environment script for diamond (under `/usr/local/diamond/3.13/bin/lin64/diamond_env` for version 3.13):
``` bash
#setup library path
if test -z "$LD_LIBRARY_PATH"; then
        LD_LIBRARY_PATH="/usr/local/lib/:${bindir}:${fpgabindir}"
else
        LD_LIBRARY_PATH="/usr/local/lib/:${bindir}:${fpgabindir}:${LD_LIBRARY_PATH}"
fi
export LD_LIBRARY_PATH
```