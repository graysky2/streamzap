#!/usr/bin/env python3

# credit to teeedubb @ https://forum.kodi.org/showthread.php?tid=199579
# and to lotte67890 @ https://forum.kodi.tv/showthread.php?tid=359063
#
# to get the current audio output device which you have set in the Kodi GUI
# (Settings>Display>Audio>Audio output device) run the following:
# curl -v -H "Content-type: application/json" -d \
#   '{"jsonrpc":"2.0","id":1,"method":"Settings.GetSettingValue","params":{"setting":"audiooutput.audiodevice"}}' \
#   http://localhost:8080/jsonrpc -u xbmc:xbmc
#
# change the ip address/port and username:password accordingly
# sample output: {"id":1,"jsonrpc":"2.0","result":{"value":"ALSA:hdmi:CARD=HDMI,DEV=1"}}
# so the target for this source is: ALSA:hdmi:CARD=HDMI,DEV=1
#
# use it in the corresponding python code below and repeat for the other source you wish to define
#
# you can also test the value and syntax by using curl to set it up:
# curl -v -H "Content-type: application/json" -d \
#   '{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"audiooutput.audiodevice","value":"ALSA:hdmi:CARD=HDMI,DEV=1"},"id":1}' \
#   http://localhost:8080/jsonrpc -u xbmc:xbmc

import xbmc
import os

tempdir = xbmc.translatePath('special://temp/')
tempfile0 = os.path.join(tempdir, 'audiooutput0')

print("CURRENT AUDIO DEVICE:")
print((xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.audiodevice"},"id":1}')))
if not os.path.isfile(tempfile0):
	# optical out
	xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.audiodevice", "value":"ALSA:iec958:CARD=PCH,DEV=0"}, "id":1}')
	xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"GUI.ShowNotification", "params":{"title":"AUDIO OUTPUT", "message":"Soundbar", "image":"/var/lib/kodi/fiber.png"}, "id":1}')
	file = open(tempfile0, "a")
	file.close()
else:
	# HDMI out
	xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.audiodevice", "value":"ALSA:hdmi:CARD=HDMI,DEV=1"}, "id":1}')
	xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"GUI.ShowNotification", "params":{"title":"AUDIO OUTPUT", "message":"TV Speakers", "image":"/var/lib/kodi/hdtv-green.png"}, "id":1}')
	os.remove(tempfile0)
