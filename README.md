## Streamzap
![remote](https://i.postimg.cc/02Yd39dh/photo05.jpg)

Getting the [Streamzap USB remote](http://www.streamzap.com/consumer/pc_remote/index.php) to work with Kodi under Linux is fairly straight forward.

## Update Jan/2023
My recommended method for using this remote with Kodi is not longer via lirc.  This presented disconnects in functionality running kodi-x11 vs kodi-gbm.  The most general implementation for using this remote with Kodi, is allowing the kernel driver to see it and adjusting the keymapping to suit Kodi.

* The really old (details for mythtv, mplayer, other) has been archived in [streamzap/old](https://github.com/graysky2/streamzap/tree/old) for those interested.
* The method using lirc (works fine for x11 but not for gbm) has been archived in [streamzap/lirc](https://github.com/graysky2/streamzap/tree/lirc) for those interested.

### Setup
* Install the v4l-utils package (your distro provides this in all likelihood).
* Place [kodi/keyboard.xml](https://raw.githubusercontent.com/graysky2/streamzap/master/kodi/keyboard.xml) into `~/.kodi/userdata/keymaps/`
* Place [streamzap.toml](https://raw.githubusercontent.com/graysky2/streamzap/master/streamzap.toml) into `/etc/rc_keymaps/`
* Modify `/etc/rc_maps.cfg` so the streamzap line points to `/etc/rc_keymaps/streamzap.toml`
```
# *  rc-streamzap             streamzap.toml
* rc-streamzap             /etc/rc_keymaps/streamzap.local
```

* First time setup only: reboot your system or re-initialize the keycode mapping to use the custom file:
```
# ir-keytable -c -w /etc/rc_keymaps/streamzap.toml
```

* THERE IS NO NEED TO RUN LIRC AT ALL so disable lircd in your init system if you previously had it enabled.

#### Optional setup/custom script
* Optionally place `kodi/audio_switch/audio_switch.py` in `~/bin/` (note you likely need to edit the code to match your system, see the thread in the comments of the file).
* Optionally place the two suggested icons into `~` as shown in the script.

### Supplemental info
#### Kodi upstream links
* [keyboard.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/keyboard.xml)
* [remote.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/remote.xml)
* [List of built-in function](http://kodi.wiki/view/List_of_built-in_functions)
