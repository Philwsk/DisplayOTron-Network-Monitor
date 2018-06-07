# DisplayOTron-Network-Monitor
A super basic network monitor I'm making from the example code ipaddr.py included in the basic examples that come with the Pimoroni Display O Tron HAT.

The script currently pings google(better to use your DNS server IP) to determine if DNS is working on my home network.

If the DNS is working then it displays Green LED & DNS is UP, otherwise it displays Red LED and DNS is DOWN.

The while loop is not the best way to do this. I will figure out the best method for intermittently checking DNS hosts.

Additional Thoughts/Ideas to possibly add:

-Turn script into daemon so it runs in the background without intervention and needing shell

-Use the graph led on right of display to indicate pinging is taking place.

-Ping local DNS & then alternative DNS servers to check if the problem is my home DNS server or my internet connection.

-Flash LED and then display hostname of device that has joined or disconnected from network.

- Replace hostname with a display of current CPU and Memory load/use. Perhaps have LED's reflect high temp or load.
