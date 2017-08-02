This code can be used with a Unicorn HAT HD on a Raspberry Pi with Raspbian to scroll a day countdown timer for an event, themed to a Disney trip with the addition of Mickey Mouse ears.

All you need to do is change the day (day_of_trip), month (month_of_trip), and year (year_of_trip_ fields. These are currently set for 27 October 2017.

To make it run on startup:

1: save the script and the mickey.png image to the home folder (in the command line this is ~ or /home/pi)
2: open up the terminal and enter the command: sudo nano /etc/profile
3: use the down arrow to move to the bottom of the file and type: python disney_countdown.py &
4: use Ctrl+X to exit, and when prompted press Y and then enter to save the file

Reboot the Raspberry Pi with the Unicorn HAT HD attached. Make sure you've done the initial Unicorn HAT HD setup by Pimoroni first!