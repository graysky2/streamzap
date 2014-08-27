# credit to teeedubb
# http://forum.xbmc.org/showthread.php?tid=199579

import xbmc
import os

tempdir = xbmc.translatePath('special://temp/')
tempfile0 = os.path.join(tempdir, 'audiooutput0')

print("CURRENT AUDIO DEVICE:")
print(xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.audiodevice"},"id":1}'))

if not os.path.isfile(tempfile0):
	# pulseaudio analog out
		xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.audiodevice", "value":"ALSA:@:CARD=PCH,DEV=0"}, "id":1}')
		xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"GUI.ShowNotification", "params":{"title":"AUDIO OUTPUT", "message":"Soundbar", "image":"/var/lib/xbmc/glossy-speaker-icon.png"}, "id":1}')
		file = open(tempfile0, "a")
		file.close()
else:
	# pulseaudio HDMI out
		xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.audiodevice", "value":"ALSA:hdmi:CARD=HDMI,DEV=1"}, "id":1}')
		xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"GUI.ShowNotification", "params":{"title":"AUDIO OUTPUT", "message":"TV Speakers", "image":"/var/lib/xbmc/hdtv.png"}, "id":1}')
		os.remove(tempfile0)
