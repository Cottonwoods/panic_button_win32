from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render

import win32gui, win32api, win32con

def index(request):
  return render(request, 'panic/index.html')

def panic(request):
  win32gui.SystemParametersInfo(win32con.SPI_SETFOREGROUNDLOCKTIMEOUT, 0, win32con.SPIF_SENDWININICHANGE | win32con.SPIF_UPDATEINIFILE)
  window = win32api.ShellExecute(0, 'open', 'chrome.exe', '--user-data-dir=$(mktemp -d) --kiosk --start-fullscreen --new-window http://dashboard.txssc.com', '', 1)

  return HttpResponseRedirect(reverse('index'))
