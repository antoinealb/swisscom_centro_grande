# Abstract
This repository contains the results of my reverse engineering of the firmware
of the Swisscom Centro Grande ADSL box. I will probably do a blog post with all
those notes. But for that I need a blog.

# Getting the firmware
After a bit of googling, I found the download URL for a version of the firmware :

    wget http://rmsdl.bluewin.ch/pirelli/Vx226N1_50033.rmt
 
# Extracting vmlinux.bin
First of all, what's in the box ?

    binwalk Vx226N1_50033.rmt

We can see in the output that there is a gzipped file which was called
"vmlinux.bin". Interesting. Let's extract this file :

    binwalk Vx226N1_50033.rmt -e
    cp _Vx226N1_50033.rmt.extracted/vmlinux.bin .
    gzip -d vmlinux.bin.gz

# What's in the vmlinux ?
Once again, binwalk is our friend, let's run it against vmlinux.bin :

    binwalk vmlinux.bin

*Insert capture_2.png*

So in order we have :

1. A linux kernel image which is slightly old. I did not use the latest
   version of the firmware, which might explain this.
2. Some copyright strings, which, after a bit of Googling around seems to be
   the copyright string of the deflate program of zlib. Nice. 
3. Some LZMA data, I have yet to undertand what they are.
4. Some gzip'd data which was modified just before the linux kernel.
4. Two CramFS file systems. CramFS is a filesystem designed to be embedded on
   flash / ROM. It is read only and can use LZMA compression to gain some
   space.

Let's extract the file systems. For this we will need the size of the various
parts, which we can calculate by taking the diff between the start adress and
the end adress (the start of next element).

    binwalk -D cramfs:.fs -vv vmlinux.bin

    mv _vmlinux.bin.extracted/2B0000.fs cramfs1
    mv _vmlinux.bin.extracted/970000.fs cramfs2

We can still run binwalk against cramfs1 and cramfs2 to check that we
extracted exactly what we wanted.

# Extracting the content of CramFS.
For this part we will use some utilities from the firmware mod kit project :
https://code.google.com/p/firmware-mod-kit/

First of all let's compile the tools we will need to extract it :
uncramfs-lzma. I tried extracting the files using standard CramFS and it did
not work. 

    wget https://firmware-mod-kit.googlecode.com/files/fmk_099.tar.gz
    tar -xzf fmk_099.tar.gz
    cd fmk/src/uncramfs-lzma/
    make
    cd ../../..

You will get some warnings, but you can safely ignore them. Now let's extract
the content of the two cramfs images.

    mkdir cramfs1_content
    ./fmk/src/uncramfs-lzma/uncramfs-lzma cramfs1_content/ cramfs1
    mkdir cramfs2_content
    ./fmk/src/uncramfs-lzma/uncramfs-lzma cramfs2_content/ cramfs2

Listing the content of cramfs1_content shows some directory structure familiar
to the UNIX afficionado.
