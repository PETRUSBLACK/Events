from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year, month):
    name = "John"
    month = month.capitalize()

    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # create a calender
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Getting a current year
    now = datetime.now()

    # Getting current time
    time = now.strftime('%I:%M:%S %p')
    current_year= now.year
    return render(request, 'home.html', 
            {"name": name,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "time": time}
            )
