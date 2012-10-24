#!/usr/bin/python
import os
import time
import pycurl
import cStringIO
import untangle 
from Tkinter import Tk


""" get current time """
localtime = time.localtime()
timeString = time.strftime("%Y%m%d-%H%M%S", localtime)

""" folder to save to """
folder = "~/pix/"
folder = os.path.expanduser(folder)

fileName = folder + timeString +  ".png"

os.system("screencapture -i " + folder + timeString +  ".png")
response = cStringIO.StringIO()


c = pycurl.Curl()
values = [
          ("key", "1eb928a612f162b21105a1ba9afbbcb6"),
          ("image", (c.FORM_FILE, fileName))]
# OR:     ("image", "http://example.com/example.jpg")]
# OR:     ("image", "YOUR_BASE64_ENCODED_IMAGE_DATA")]

c.setopt(c.URL, "http://api.imgur.com/2/upload.xml")
c.setopt(c.HTTPPOST, values)
c.setopt(c.WRITEFUNCTION, response.write)
c.perform()
c.close()

o = untangle.parse(response.getvalue())
url = o.upload.links.original.cdata
delete_page = o.upload.links.delete_page.cdata

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(url)
r.destroy()
print 'url:        ', url
print 'delete page:', delete_page
