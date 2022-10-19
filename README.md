## Update Jan/2022
I found that my remote recently stopped working properly with default driver (skipping key presses) on x86_64; the devinput driver does a much better job.  I took the opportunity to update the instructions to use devinput and to streamline re-scoping down to just working with Kodi.  The more expansive version (details for mythtv, mplayer, other) has been archived in [streamzap/old](https://github.com/graysky2/streamzap/tree/old) for those interested.

## Streamzap
![remote](https://i.postimg.cc/02Yd39dh/photo05.jpg)

Getting the [Streamzap USB remote](http://www.streamzap.com/consumer/pc_remote/index.php) to work with Kodi under Linux is fairly straight forward.  This repo contains instructions and files to allow operation with [LIRC](http://www.lirc.org).

### Setup LIRC on x86_64
* Install lirc for your distro. Note that by default, `lircd` runs as root user. However, for increased stability and security, upstream recommends running it as an unprivileged user.  See [Appendix 14](http://www.lirc.org/html/configuration-guide.html) and/or [this](https://wiki.archlinux.org/index.php/LIRC#Running_as_a_regular_user_rather_than_as_root) Arch Wiki page for that setup.  Arch users may build and install [lirc-user-service](https://aur.archlinux.org/packages/lirc-user-service) to automatically configure this behavior.
* Make sure that lirc is using the `devinput` driver which has been defaulted for a number of years now.  Likely, your distro defines this in `/etc/lirc/lirc_options.conf`.
* Start lirc using your init system (systemd, openrc, upstart, etc.)
* Place `kodi/Lircmap.xml` into `~/.kodi/userdata/`
* Place `kodi/remote.xml` into `~/.kodi/userdata/keymaps/`
* Note there does not appear to be a need to define a custom config in `/etc/lirc/lircd.conf.d/` any more.  Just use the package provided `devinput.lircd.conf`

#### Optional setup/custom script
* Optionally place `kodi/audio_switch/audio_switch.py` in `~/bin/` (note you likely need to edit the code to match your system, see the thread in the comments of the file).
* Optionally place the two suggested icons into `~` as shown in the script.

### Setup LIRC on ARM
For whatever reason, I am unable to get lirc to run correctly as an unprivileged user on ARM.  The OK button fails to respond when configured to do so.

* Install lirc for your distro.
* Edit `/etc/lirc/lirc_options.conf` and change the `driver = devinput` line to `driver = default`
* Place `streamzap.lircd.conf` into `/etc/lirc/lircd.conf.d/`
* Place `kodi/Lircmap.xml` into `~/.kodi/userdata/`
* Place `kodi/remote.xml` into `~/.kodi/userdata/keymaps/`
* Start lirc using your init system (systemd, openrc, upstart, etc.)

Note that on Arch ARM, lirc-1:0.10.2-1 breaks this so revert back to 1:0.10.2-12 and add lirc to the IgnorePkg array in `/etc/pacman.conf` to keep it.  Users not wishing to build the package themselves can download the last-good version from [here](http://tardis.tiny-vps.com/aarm/packages/l/lirc/).

### Supplemental info
#### Kodi upstream links
* [keyboard.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/keyboard.xml)
* [remote.xml](https://github.com/xbmc/xbmc/blob/master/system/keymaps/remote.xml)
* [List of built-in function](http://kodi.wiki/view/List_of_built-in_functions)
