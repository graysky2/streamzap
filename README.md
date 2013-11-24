##Streamzap
Getting the [Streamzap USB remote](http://www.amazon.com/Streamzap-USBIR2-PC-Remote-Control/dp/B00008XETO) to work under Linux is currently trivial and does NOT require the use of [LIRC](http://www.lirc.org) any more.  The repo contains several config files that work with [v4l-utils](http://git.linuxtv.org/v4l-utils.git) and any modern Linux kernel.  These files represent my preferences and are optimized for use with mplayer and xbmc.

## Installation
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
* keyboard.xml to ~/.xbmc/userdata/keymaps and is only for use with xbmc

## Supplemental Info
### Syntax of /etc/rc_keymaps/streamzap.local
The syntax of the keymap `scancode button_name`

### Show Available Scancodes
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

### Show Availble Button Names
The lrc-utils package is likely required.  Execute `irrecord -l` to see a list of all available button names.
