##Streamzap
Getting the [Streamzap USB remote](http://www.streamzap.com/consumer/pc_remote/index.php) to work under Linux is currently trivial and does NOT require the use of [LIRC](http://www.lirc.org) any more although LIRC does provide the ability to map the same keypress to different actions under a variety of applications.

The repo contains several config files that work with [v4l-utils](http://git.linuxtv.org/v4l-utils.git) and any modern Linux kernel as well as files to allow operation with LIRC, specifically for mythtv, xbmc, and mplayer.

## Option #1 - Full featured operation of mplayer, mythtv, and xbmc using LIRC.
### Step LIRC
* Install lirc for your distro.
* Setup the lirc config to use the streamzap remote by pointing the remote's config file to the daemon. This varies distro-to-distro but is likely /etc/lirc/lircd.conf.  I have provided the upstream file in this repo "lircd.conf.streamzap" for reference.
* Place 90-streamzap.conf in /etc/X11/xorg.conf.d which causes X to ignore the remote without LIRC.  This step is required.
* Restart X if your just did the aforementioned step for the first time.
* Start lirc using your init system (systemd, openrc, upstart, etc.)

### For mythtv and mplayer
* Place the .lirc dir from this repo into your homedir.
* Place .lircrc into your homedir.

### For xbmc
* Place Lirc.xml into ~/.xbmc/userdata before loading xbmc.

## Option #2 - Basic operation of mplayer using only the v4l-utils package.
* Install the v4l-util package (your distro provides this in all likelyhood).
* Modify /etc/rc_maps.cfg so the streamzap line points to /etc/rc_keymaps/streamzap.local
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

* streamzap.local should be installed to /etc/rc_keymaps

### Supplemental Info
#### Syntax of /etc/rc_keymaps/streamzap.local
The syntax of the keymap `scancode button_name`

#### Show Available Scancodes
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

#### Show Availble Button Names
The lrc-utils package is likely required.  Execute `irrecord -l` to see a list of all available button names.

