## Streamzap
![remote](https://i.postimg.cc/02Yd39dh/photo05.jpg)

Getting the [Streamzap USB remote](http://www.streamzap.com/consumer/pc_remote/index.php) to work under Linux is very easy.  The recommended method is to use [LIRC](http://www.lirc.org) as it provides the ability to map the same keypress to different actions under a variety of applications.  Alternatively, [v4l-utils](http://git.linuxtv.org/v4l-utils.git) and any modern Linux kernel works too but is less flexible.

This repo contains instructions and files to allow operation with LIRC or v4l-utils and also gives specific config files for mythtv, kodi, and mplayer.  Use only one of the two options presented.

## Option #1 - Full featured operation of mplayer, mythtv, and kodi (and others) using LIRC.
### Setup LIRC
* Install lirc for your distro. Note that by default, `lircd` runs as root user. However, for increased stability and security, upstream recommends running it as an unprivileged user.  See [Appendix 14](http://www.lirc.org/html/configuration-guide.html) and/or [this](https://wiki.archlinux.org/index.php/LIRC#Running_as_a_regular_user_rather_than_as_root) Arch Wiki page for that setup.
* Place `00-Streamzap_PC_Remote.conf` in `/etc/lirc/lircd.conf.d/` (note this was regenerated using lirc 0.9.4b to prevent some [key doubling](https://sourceforge.net/p/lirc/tickets/219/) observed with the original file).
* If using Xorg, place `90-streamzap-disable.conf` in `/etc/X11/xorg.conf.d/` to keep the remote from being seen as a keyboard.
* If not using Xorg (for example on some ARM devices such as a Raspberry Pi), blacklist the offending modules by placing `streamzap-blacklist.conf` in `/etc/modprobe.d/` to suppress this behavior.
* With the release of lirc v0.9.4a (June of 2016), users need to edit upstream's provided `/etc/lirc/lirc_options.conf` with these changes:
```
driver          = default
device          = /dev/lirc0
```
* Start lirc using your init system (systemd, openrc, upstart, etc.)

#### For mythtv and mplayer
* Place `.lirc/` into your homedir.
* Place `.lircrc` into your homedir.
* For mythtv only, create this symlink: `ln -s ~/.lirc/mythtv ~/.mythtv/lircrc`

#### For kodi
* Place `kodi/Lircmap.xml` into `~/.kodi/userdata/`
* Optionally place `kodi/remote.xml` into `~/.kodi/userdata/keymaps/`
* Optionally place `kodi/audio_switch/audio_switch.py` in `~/bin/` (note you likely need to edit the code to match your system, see the thread in the comments of the file).
* Optionally place the two suggested icons into `~` as shown in the script.

### Supplemental info
#### Mplayer links
* [Upstream control file](/etc/mplayer/input.conf)
* `mplayer -input keylist`
* `mplayer -input cmdlist`

#### Kodi upstream links
* [keyboard.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/keyboard.xml)
* [remote.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/remote.xml)
* [List of built-in function](http://kodi.wiki/view/List_of_built-in_functions)

## Option #2 - Basic operation of mplayer using only the v4l-utils package.
* Install the v4l-util package (your distro provides this in all likelihood).
* Modify `/etc/rc_maps.cfg` so the streamzap line points to `/etc/rc_keymaps/streamzap.local`
```
--- a/etc/rc_maps.cfg	2013-10-08 18:10:04.478595923 -0400
+++ b/etc/rc_maps.cfg	2013-10-08 16:19:34.150994862 -0400
@@ -77,7 +78,7 @@
 *	rc-npgtech               npgtech
 *	rc-leadtek-y04g0051      leadtek_y04g0051
 *	rc-manli                 manli
-*	rc-streamzap             streamzap
+*	rc-streamzap             /etc/rc_keymaps/streamzap.local
 *	rc-winfast-usbii-deluxe  winfast_usbii_deluxe
 *	rc-behold                behold
 *	rc-gadmei-rm008z         gadmei_rm008z
```

* `streamzap.local` should be installed to `/etc/rc_keymaps/`

### Supplemental info
#### Syntax of /etc/rc_keymaps/streamzap.local
The syntax of the keymap `scancode button_name`

#### Show available scancodes
Execute `ir-keytable` without any arguments.  Example:
```
# ir-keytable
Found /sys/class/rc/rc0/ (/dev/input/event3) with:
	Driver streamzap, table rc-streamzap
	Supported protocols: NEC RC-5 RC-6 JVC SONY SANYO LIRC RC-5-SZ other
	Enabled protocols: RC-5-SZ
	Name: Streamzap PC Remote Infrared Rec
	bus: 3, vendor/product: 0e9c:0000, version: 0x0100
	Repeat delay = 500 ms, repeat period = 125 ms
```

Execute `ir-keytable --read --device=/dev/input/PATH` where PATH is what the previous command outputted (event3 in the example above).

#### Show available button names
The lirc package is likely required.  Execute `irrecord -l` to see a list of all available button names.
