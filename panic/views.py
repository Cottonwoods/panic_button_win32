from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render

import win32gui, win32api, win32con, win32process

def index(request):
  return render(request, 'panic/index.html')

def panic(request):
  win32gui.SystemParametersInfo(win32con.SPI_SETFOREGROUNDLOCKTIMEOUT, 0, win32con.SPIF_SENDWININICHANGE | win32con.SPIF_UPDATEINIFILE)

  processes = win32process.EnumProcesses()
  for pid in processes:
    try:
      handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
      exe = win32process.GetModuleFileNameEx(handle, 0)
      if exe.lower().contains('chrome.exe'):
        win32api.TerminateProcess(int(handle), -1)
    except:
      pass

  window = win32api.ShellExecute(0, 'open', 'chrome.exe', '--user-data-dir=$(mktemp -d) --kiosk --start-fullscreen --new-window http://dashboard.txssc.com', '', 1)
  return HttpResponseRedirect(reverse('index'))
