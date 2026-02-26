class Date:
    """Represents a year, month, and day."""
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0
# TODO: Write make_date(year, month, day)
def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

# TODO: Write print_date(date)
def print_date(date):
    print(f"{date.month}/{date.day}/{date.year}")

# TODO: Write date_to_tuple(date) -- Return (year, month, day)
def date_to_tuple(date):
    dateTuple = (date.year, date.month, date.day)
    return dateTuple

# TODO: Write is_after(d1, d2)
def is_after(d1, d2):
    date1 = date_to_tuple(d1)
    date2 = date_to_tuple(d2)
    return date1 > date2

# --- Test Code ---
d1 = make_date(1933, 6, 22)
d2 = make_date(1933, 9, 17)
print_date(d1)
print_date(d2)
print(is_after(d2, d1))     # Should print True