import datetime

birthday_year = int(input("Enter your birthday year: "))
print(birthday_year)

birthday_month = int(input("Enter your birthday month: "))
print(birthday_month)

birthday_date = int(input("Enter your birthday date: "))
print(birthday_date)

today = datetime.date.today()
birthday_this_year = datetime.date(today.year, birthday_month, birthday_date)

# If birthday has passed this year, use next year
if birthday_this_year < today:
    next_birthday = datetime.date(today.year + 1, birthday_month, birthday_date)
    next_age = today.year + 1 - birthday_year
else:
    next_birthday = birthday_this_year
    next_age = today.year - birthday_year

delta = next_birthday - today
days = delta.days

if days == 0:
    print(f"Today is your birthday!")
    print(f"Happy Birthday to you! You are now {next_age} years old!")
else:
    print(f"Your birthday is coming up in {days} days. You will be {next_age} years old.")
