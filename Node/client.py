# This code is part of the Olympus Server Management Program
#Copyright (C) 2011  Asher Glick
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.



# Echo client program
import socket
import sys
import os
from stat import *
import time

# load plugins
print '\n--- plugin list ---'
fileList = os.listdir('./plugins');
for f in os.listdir('./plugins'):
  if (f is " PLUGINS "):
    print "hello world"
  print f
 
print '--- end plugin list ---\n'

print "loaded", len(fileList), "plugins"

# connect to remote computer
HOST = '127.0.0.1'    # The remote host
PORT = 50007          # The same port as used by the server
s = None
while 1:
  for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
      s = socket.socket(af, socktype, proto)
    except socket.error, msg:
      s = None
      continue
    try:
      s.connect(sa)
    except socket.error, msg:
      s.close()
      s = None
      continue
    break
  if s is None:
    print 'Could not connect to root server, Retrying in 10 seconds'
    time.sleep(30)
    continue
  else:
    break
    
# Now the socket is configured
print 'Connection to root server'

#data transfer goes through here
s.send('Hello, world')
data = s.recv(1024)

# Done sending data close the socket
s.close()
print 'Received', repr(data)

