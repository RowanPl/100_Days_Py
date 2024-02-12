def is_leap_year(year):
    """Return True if year is a leap year, False otherwise."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Return the number of days in a month."""
    if month > 12 or month < 1:
        return 'Invalid month'
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = is_leap_year(year)
    if leap and month == 2:
        return 29
    return month_days[month - 1]


month = int(input('Enter a month: '))
year = int(input('Enter a year: '))
days = days_in_month(year, month)
print(days)
