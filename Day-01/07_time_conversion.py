minutes= int(input("enter the number of minutes:"))
hours = minutes//60
remaining_minutes= minutes%60
print("Hours:",hours)
print("Remaining minutes:",remaining_minutes)
if hours==1:
    hour_txt= "hour"
else:
    hour_txt="hours"
if remaining_minutes==1:
    minutes_txt="minute"
else:
    minutes_txt="minutes"
print(hours, hour_txt, remaining_minutes, minutes_txt)