title: Install Lattice iCEcube2 on 32 bit Linux
date: 2023-09-29
thumbnail: lattice_tb.jpg
english: true
draft: true

Do you have troubles installing iCEcube2 on your Linux computer? Lattice is providing a Linux installation for iCEcube2 [here](https://www.latticesemi.com/Products/DesignSoftwareAndIP/FPGAandLDS/iCEcube2).

Following the installation instruction I ran into following issue:
```console
$ unzip iCEcube2setup_Dec_10_2020_2012_lin.zip
Archive:  iCEcube2setup_Dec_10_2020_2012_lin.zip
  inflating: iCEcube2setup_Dec_10_2020_2012
```

```console
$ chmod +x iCEcube2setup_Dec_10_2020_2012
```

```console
$ ./iCEcube2setup_Dec_10_2020_2012
bash: ./iCEcube2setup_Dec_10_2020_2012: Permission denied
```

*iCEcube2* is a 32 bit executable and very probably you're running a 64 bit Linux. The solution? Install the 32 bit dependencies.

### Fedora
Tested with Fedora 38

```console
$ sudo dnf install glibc.i686 libXext.i686 libSM.i686 libXi.i686 libXrender.i686 libXrandr.i686 libXfixes.i686 libXcursor.i686 libXinerama.i686 freetype.i686 libpng12.i686

...
  Verifying        : libxml2-2.10.4-1.fc38.i686                                                                                                                                                                                                                                                                         44/45 
  Verifying        : p11-kit-0.25.0-1.fc38.i686                                                                                                                                                                                                                                                                         45/45 

Installed:
  bzip2-libs-1.0.8-13.fc38.i686          cairo-1.17.8-4.fc38.i686               fontconfig-2.14.2-1.fc38.i686          freetype-2.13.0-2.fc38.i686              glib2-2.76.5-2.fc38.i686              glibc-2.37-5.fc38.i686                 glibc-gconv-extra-2.37-5.fc38.i686          gmp-1:6.2.1-4.fc38.i686              
  gnutls-3.8.1-1.fc38.i686               graphite2-1.3.14-11.fc38.i686          harfbuzz-7.1.0-1.fc38.i686             libICE-1.0.10-10.fc38.i686               libSM-1.2.3-12.fc38.i686              libX11-1.8.6-1.fc38.i686               libXau-1.0.11-2.fc38.i686                   libXcursor-1.2.1-3.fc38.i686         
  libXext-1.3.5-2.fc38.i686              libXfixes-6.0.0-5.fc38.i686            libXi-1.8.1-1.fc38.i686                libXinerama-1.1.5-2.fc38.i686            libXrandr-1.5.2-10.fc38.i686          libXrender-0.9.11-2.fc38.i686          libblkid-2.38.1-4.fc38.i686                 libbrotli-1.0.9-11.fc38.i686         
  libffi-3.4.4-2.fc38.i686               libgcc-13.2.1-1.fc38.i686              libidn2-2.3.4-2.fc38.i686              libmount-2.38.1-4.fc38.i686              libpng-2:1.6.37-14.fc38.i686          libpng12-1.2.57-17.fc38.i686           libseLinux-3.5-1.fc38.i686                  libsepol-3.5-1.fc38.i686             
  libstdc++-13.2.1-1.fc38.i686           libtasn1-4.19.0-2.fc38.i686            libunistring-1.1-3.fc38.i686           libunistring1.0-1.0-1.fc38.i686          libuuid-2.38.1-4.fc38.i686            libxcb-1.13.1-11.fc38.i686             libxml2-2.10.4-1.fc38.i686                  nettle-3.8-3.fc38.i686               
  p11-kit-0.25.0-1.fc38.i686             pcre2-10.42-1.fc38.1.i686              pixman-0.42.2-1.fc38.i686              xz-libs-5.4.1-1.fc38.i686                zlib-1.2.13-3.fc38.i686              

Complete!
```

### Ubuntu
You find a detailed installation guide on [vhdlwiz.com](https://vhdlwhiz.com/lattice-icecube2-ubuntu-20-04-icestick/). I'm not sure if every step is necessary.