months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
date = input("Date: ")
try:
    date = date.split("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
except ValueError:
    try:
        date1 = date[0].replace(",", "")
        day, month, year = date1.split(" ")
    except AttributeError:
        pass
    else:
       month = month.capitalize()
       year = int(year)
       day = int(day)
       j = 0
       for _ in months:
           if month == months[j]:
               print(f"{year:04}-{(j + 1):02}-{day:02}")
               break
           j += 1
else:
    print(f"{year:04}-{(month + 1):02}-{day:02}")