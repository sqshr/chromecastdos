import time
import pychromecast
import zeroconf

zconf = zeroconf.Zeroconf()
browser = pychromecast.CastBrowser(pychromecast.SimpleCastListener(lambda uuid, service: print(browser.devices[uuid].friendly_name)), zconf)

browser.start_discovery()
chromecasts, browser = pychromecast.get_chromecasts()

while True:
	for c in chromecasts:
		cast = c
		print(f'  "Killing "{cast.name}" on mDNS/host service {cast.cast_info.services} with UUID:{cast.uuid}')
		try:
			cast = c
			cast.wait()
			cast.quit_app()
		except:
			pass
	time.sleep(5)

browser.stop_discovery()
