Q) Compute the number of days since January 1, 1970 and the current time of day in hours, minutes, and seconds.

Solution:

# Solution goes here

#compute number of days since january 1, 1970
#current time of day in hrs, min, sec
total_seconds = time.time()
#get current time in seconds since jan 1, 1970

seconds_per_minute = 60
seconds_per_hour = 60*60
seconds_per_day = 24*3600

#number of full days since epoch
days = total_seconds // seconds_per_day

#remaining seconds after removing days
remaining = total_seconds % seconds_per_day 

#hours
hours = remaining // seconds_per_hour
remaining = remaining % seconds_per_hour

#minutes
minutes = remaining // seconds_per_minute

#seconds
seconds = remaining % seconds_per_minute

print("Days since Jan 1, 1970:", days)
print("Current time:", hours, "hours", minutes, "minutes", seconds, "seconds")
