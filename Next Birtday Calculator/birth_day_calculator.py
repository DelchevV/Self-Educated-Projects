from datetime import date

year = int(input('Year:'))
month = int(input('Month:'))
day = int(input('Day:'))

birthday = date(year, month, day)
today = date.today()
next_birthday = birthday.replace(year=today.year)

if next_birthday < today:
    # birthday for this year has already passed
    next_birthday = next_birthday.replace(year=next_birthday.year + 1)

print('You are', int((today - birthday).days / 365), 'years old')
print('Your next birthday is in', (next_birthday - today).days, 'days')