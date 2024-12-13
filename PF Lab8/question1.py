from datetime import datetime

# Define the datetime object
datetime_obj = datetime(2018, 7, 12, 21, 40)

# a) (Thursday, July 13 2018')
print(datetime_obj.strftime("%A, %B %d %Y"))

# b) ('09:40 PM Central Daylight Time on 07/13/2018')
print(datetime_obj.strftime("%I:%M %p %Z on %m/%d/%Y"))

# c) ('I will meet you on Thu July 13 at 09:40 PM.')
print(datetime_obj.strftime("I will meet you on %a %B %d at %I:%M %p."))
