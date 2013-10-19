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
* keyboard.xml to ~/.xbmc/userdata/keymaps and is only for user with xbmc
