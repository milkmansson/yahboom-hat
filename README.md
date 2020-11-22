# yahboom-hat (v1)
Code and service to make Yahboom Hat work properly.  Instructions and English in original packaging is unsuitable for noobs.  Here is my learning.

Yahboom sell a device called YB-EPV02 (ver1.1).  When I bought this I was a Pi Noob (probably still am) and was pretty upset to not find an a.b.c guide to making it work.  I learned an incredible amount, which I intend to share here.  Suffice to say it was as useful as a brick until I got through the learning, depite looking like a great device on the surface.

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)

On the outside:
* Raspberry Pi hat, with spacers for mounting
* Small OLED display, which on the package shows test of IP address, RAM usage etc.
* Won't necessarily mount on other cases - but you probably knew that
* Chip heatsinks make a big difference - if you find one to accompany and fit under the hat on the chips, do it.

Practical lessons learned
* heat dissipation was mediocre until i sat the pi with the fan facing sideways, such that airflow was not vertically downward onto the heatsinks.
* maximum fan speed felt pretty poor.  If i wanted to drive my PI hard, I'd be too scared to do it with this device.
* without further action, the device will light up green and do nothing up and until something is done (the purpose of this guide)

Things I needed to learn (the hard way) to make this work:
* How to write a service file that called a Python Script
* That the wiringPi service is depricated, and therefore Python is the only way
* Nomenclature about Python3 such that everything was working (YB docs had Python2 references in some places)
* Troubleshooting using systemctl.
* robbed some of the example code from the manufacturer (links etc in good time!)
* how to write markdown for github :)




