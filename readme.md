# Abstract
This repository contains the results of my reverse engineering of the firmware
of the Swisscom Centro Grande ADSL box. I will probably do a blog post with all
those notes. But for that I need a blog.

**Note:** I am by no mean a Linux wizard, so I might miss interesting stuff, and
say wrong things. If you think something should be added / changed, feel free to
open an issue / make a pull request.

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

# What's in the vmlinux ?
Once again, binwalk is our friend, let's run it against vmlinux.bin :

    binwalk vmlinux.bin

![alt text](https://github.com/antoinealb/swisscom_centro_grande/raw/master/binwalk_vmlinux.png "Binwalk result on vmlinux.bin")

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
to the UNIX afficionado :

```
.
|-- bin
|-- dlna
|   `-- xml
|       `-- icon
|-- etc
|   |-- ssh
|   `-- wlan
|-- home
|   |-- html
|   `-- httpd
|       `-- html
|           `-- images
`-- lib
```
# Analysis of /etc
The first thing I noticed about /etc is it doesn't contain the usual `passwd` and `shadow` files which would be very cool to have :(
I think it is not possible for a box to boot without them and I just haven't found them yet.
If anyone knows more on this topic, I would be really happy to hear from you.
## sshd_config
This file is the configuration for the OpenSSH server, which is used for remote
administration of the router. I have cut some parts of the file to focus on what
seemed important to me.

At the start of the file, we see some instructions to tell the server to listen
on any IPv4 adress, on port 22:

```
Port 22
AddressFamily inet
```

Then we have some declarations about which method of authentification are allowed:

```
PermitRootLogin yes
RSAAuthentication no
PubkeyAuthentication no
PasswordAuthentication yes
ChallengeResponseAuthentication no
PermitEmptyPasswords yes
```

Let's hope it is used for production with those settings ! :) That's about it
for sshd config, now let's move to something else.

Also, You can notice that the ssh v1 protocol is enabled by default. This could lead to some funny exploit.

# Newer version of the firmware
It seems that there is another more recent version of the firmware (if I can understand Swisscom's file naming convention)
available at : http://rmsdl.bluewin.ch/pirelli/Vx226x1_60208.sig Let's see what it hides.

```
wget http://rmsdl.bluewin.ch/pirelli/Vx226x1_60208.sig
binwalk Vx226x1_60208.sig
```

This time it contains more data directly, for example two SquashFS instances that we will try extracting immediately.

```
binwalk -D squashfs:.fs Vx226x1_60208.sig
cd fmk/src/
./configure
make
cd ../..
mkdir fs1_content fs2_content
./fmk/unsquashfs_all.sh _Vx226x1_60208.sig.extracted/120100.fs fs1_content/
./fmk/unsquashfs_all.sh _Vx226x1_60208.sig.extracted/AC0100.fs fs2_content/
```

Running `tree` against them reveals a directory structure that overlaps each other (we got /etc two times, etc..) but this times there is a lot more files, for example some init.d

After checking /etc/version in both filesystems, it seems that there is a main version and a recovery one which is smaller than the main.

# Default telnet / SSH passwords
* user: `admin`
* password: `1234`

Sadly we don't land on a real shell but on their configuration system.
Perhaps this can get changed ?
