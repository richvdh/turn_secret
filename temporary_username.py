#!/usr/bin/env python

from __future__ import print_function

import base64
import time
import hmac
import hashlib
import re
import sys

# read the shared secret from coturn's config file
conffile="/etc/turnserver.conf"
secret=None
with open(conffile) as fh:
    for line in fh:
        m = re.search("^\s*static-auth-secret\s*=\s*(.*)$", line)
        if m is not None:
            secret = m.group(1)
            break

if secret is None:
    print ("Couldn't find static-auth-secret in %s" % conffile,
           file=sys.stderr)
    exit(1)

expiry=int(time.time())+3600
username="%d:temp" % expiry
mac = hmac.new(secret, msg=username, digestmod=hashlib.sha1)
password = base64.b64encode(mac.digest())

print ("Username: %s" % username)
print ("Password: %s" % password)
