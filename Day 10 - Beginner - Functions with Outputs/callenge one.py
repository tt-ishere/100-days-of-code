
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 1:
            if year % 400 == 0:
                return True
            else:
                return False      
        else:
            return True
    else:
        return False 


def days_in_month(year, month):
    """Takes year and checks if it's a leap year before it returns the 
    number of days in the month"""
    if month > 12 or month < 1:
        return "Invalid month"
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return days_in_month[month - 1]
    
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)