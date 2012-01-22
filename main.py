#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'	
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

print '======================================='
print 'BEGIN ADDING AND CHANGING THE INSTALLER'

# Adding the Linux Mint installer, grub-pc
os.system('apt-get install -y mint-debian-installer')

# mint-debian-installer files:
# /etc/skel/Desktop/mint-debian-installer.desktop
# /usr/bin/mint-debian-installer
# /usr/lib/linuxmint/mint-debian-installer/icon.png
# /usr/lib/linuxmint/mint-debian-installer/mint-debian-installer.glade
# /usr/lib/linuxmint/mint-debian-installer/mint-debian-installer.py
# /usr/lib/linuxmint/mint-debian-installer/version.py
# /usr/share/applications/mint-debian-installer.desktop

print 'FINISHED ADDING AND CHANGING THE INSTALLER'
print '=========================================='
