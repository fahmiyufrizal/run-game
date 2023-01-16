# run by hostname
# by fahmiyufrizal@2023

import os
import ctypes
from os import path
import pathlib
from sys import exit
import configparser
import socket

# parameters
titlewindow = 'fahmiyufrizal@2023 [github.com/fahmiyufrizal]'
hostname = socket.gethostname()
warning = 'Tidak dapat membuka aplikasi pada client ini. Silahkan hubungi operator!'
section = 'config'
dp0 = os.getcwd()

# param from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
if config.has_section(section):
	game_exe = config['config']['path_to_exe']
	autohide = config['config']['auto_hide_folder_after_blocked']
	warning = config['config']['warning_message']
else:
	ctypes.windll.user32.MessageBoxW(0, 'Invalid settings!', titlewindow, 16)
	exit()

# check config
if not path.exists ('config.ini'):
	ctypes.windll.user32.MessageBoxW(0, 'config.ini tidak terdeteksi!', titlewindow, 16)
	exit()
	
# check allowed_pc_list.txt
if not path.exists ('allowed_pc_list.txt'):
	ctypes.windll.user32.MessageBoxW(0, 'allowed_pc_list.txt tidak terdeteksi!', titlewindow, 16)
	exit()
	
def search_allowed_pc(file_path, pc):
	with open(file_path, 'r') as file:
		allowed_pc = file.read()
		if pc in allowed_pc:
			os.system('start "" "' + game_exe + '"')
			exit()
		else:
			ctypes.windll.user32.MessageBoxW(0, warning, titlewindow, 16)
			if autohide ==  'yes':
				os.system('attrib +s +h "'+ dp0 + '\*.*" /s /d')
			elif autohide == 'no':
				exit()
			else:
				ctypes.windll.user32.MessageBoxW(0, 'Invalid settings!', titlewindow, 16)
			exit()

search_allowed_pc(r'allowed_pc_list.txt', hostname)