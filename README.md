# Python network connectivity monitoring tool

This project is a simple python script which periodically pings an IP (8.8.8.8 in this case).

We will ping Google's DNS server every 5 seconds `python time.sleep(5)` with the subprocess function `python subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)` and check if there is an active internet connection.
If there is not - the script will open or write a CSV file and append the Timestamps

## Why?

The use for this is my internet connectivity disrupts from time to time since upgrading my internet and getting a new router from my ISP.
And I simply forget writing the times down for contacting my ISP and have something in hand to give them.
