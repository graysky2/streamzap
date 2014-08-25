##Streamzap
Getting the [Streamzap USB remote](http://www.streamzap.com/consumer/pc_remote/index.php) to work under Linux is currently trivial and does NOT require the use of [LIRC](http://www.lirc.org) any more although LIRC does provide the ability to map the same keypress to different actions under a variety of applications.

The repo contains several config files that work with [v4l-utils](http://git.linuxtv.org/v4l-utils.git) and any modern Linux kernel as well as files to allow operation with LIRC, specifically for mythtv, xbmc, and mplayer.

## Option #1 - Full featured operation of mplayer, mythtv, and xbmc using LIRC.
### Setup LIRC
* Install lirc and/or lirc-utils for your distro.  For Arch, only lirc-utils is required.
* Place lircd.conf.streamzap-new in /etc/lirc renaming it to lircd.conf 
* Place 90-streamzap.conf in /etc/X11/xorg.conf.d which causes X to ignore the remote without LIRC.  This step is required.
* Restart X if you just did the aforementioned step for the first time.
* Start lirc using your init system (systemd, openrc, upstart, etc.)

If the included lircd.conf does not work for you, consider generating your own with irrecord.
```
irrecord --device=/dev/lirc0 streamzap
```
Follow the included instructions.  It is doubtful that the actual scancodes have changed, so you can likely just copy that section into the new file.

#### For mythtv and mplayer
* Place the .lirc dir from this repo into your homedir.
* Place .lircrc into your homedir.
* For mythtv only, create a symlink in your ~/.mythtv to ~/.lirc/mythtv `ln -s ~/.lirc/mythtv ~/.mythtv/mythtv`

#### For XBMC
* Place Lirc.xml into ~/.xbmc/userdata
* Place remote.xml into ~/.xbmc/userdata/keymaps
* Place audio_switch.py in ~/xbmc/bin (note you likely need to edit the code to match your system, see the thread in the comments).
* Two suggestoned icons are included. Place them in ~ as shown in the script.

##### XBMC Files and Formats
* Lircmap.xml - Maps xbmc_buttons to LIRC_buttons.  (`<xbmc_button>LIRC_button</xbmc_button>`)
* remote.xml - Maps xbmc_buttons to xbmc_actions.  (`<xbmc_button>action</xbmc_button>`)

The two together allow for: LIRC_buttons <--> xbmc_buttons <--> xbmc_actions.

### Supplemental Info
#### Mplayer Links
* [Upstream control file](/etc/mplayer/input.conf)
* `mplayer -input keylist`
* `mplayer -input cmdlist`

#### XBMC Upstream Links
* [keyboard.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/keyboard.xml)
* [remote.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/remote.xml)
* [List of built-in function](http://wiki.xbmc.org/index.php?title=List_of_built-in_functions)

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

