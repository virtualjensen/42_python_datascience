import time
import datetime

#Get the current time in seconds since the epoch (January 1, 1970)
now = time.time()

#Need to print in comma separated format
#Need to print in scientific notation format
print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")

#Get the current time in a human-readable format
date = datetime.datetime.now().strftime("%b %d %Y")
print(date)
print()

#expected output
#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$
#$> 