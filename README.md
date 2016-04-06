# Pi-Setup
A small setup program I wrote because I kept reinstalling my Raspberry Pi.

Pull requests, additions and ideas are welcomed!

So far, it will:
* Update/upgrade the Pi
* Install a webserver with Apache, PHP, MySQL and FTP
* Install a custom MOTD (Message of the Day, the text that shows whenever you log in via SSH) 

## Installation
* Download the repository: `git clone http://github.com/Deinara/pi-setup`
* enter the directory: `cd pi-setup`
* make the script executable: `chmod +x setup.py`
* run the script: `sudo ./setup.py`

## MOTD
```
  _       __     __                             __
 | |     / /__  / /________  ____ ___  ___     / /_____   _
 | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \ (_)
 | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ / _
 |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/ (_)

    .~~.   .~~.
   '. \ ' ' / .'        Date.........: 12:53:31 04-04-2016
    .~ .~~~..~.         Last login...: Mon Apr 4 12:51 from 00.000.00.000
   : .~.'~'.~. :        SSH Sessions.: 2
  ~ (   ) (   ) ~       Uptime.......: 0 days, 13h 20m 00s
 ( : '~'.~.'~' : )      Memory.......: Total: 925MB, Used: 308MB, Free: 617MB
  ~ .~ (   ) ~. ~       Storage......: Total: 15G, Used: 3.6G, Free: 10G
   (  : '~' :  )        Processes....: 121
    '~ .~~~. ~'         Temperature..: 37°C
        '~'

pi@raspberrypi:~ $
```

#### MOTD Sources:
* [http://patorjk.com](http://patorjk.com/software/taag/) for ASCII 'Welcome To'
* [Raspberry Pi Forum user 'yanewby' and 'b3n'](https://www.raspberrypi.org/forums/viewtopic.php?t=23440) for the ASCII raspberry and ideas for statistics
* Various pages and forums with example commands to construct stats
