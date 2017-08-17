from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()

from selenium import webdriver



# now Firefox will run in a virtual display. 
# you will not see the browser.
browser = webdriver.Firefox()
browser.get('http://www.google.com')
print (browser.title)
browser.quit()

vdisplay.stop()