from datetime import datetime, date, timedelta
import math

def get_following_friday(date_obj):
    '''
    Returns the Friday immediately following the date passed in.
    If the date passed in is a Friday it should return itself.
    '''
    # In Python isoweekday Monday is 1 and Sunday is 7
    weekday = date_obj.isoweekday()
    if weekday > 5:
        distance_from_fri = 7 - abs(5 - weekday)
    else:
        distance_from_fri = 5 - weekday
    return date_obj + timedelta(days=distance_from_fri)

def get_fiscal_year_start_date(date_obj):
    '''
    Returns the start date of the fiscal year of the date passed in.
    ** Walmarts fiscal year starts with the first WM Week that ends in Feburary
    ** WM Weeks start on Saturday and end on Friday
    '''
    # Find the next Friday that follows the given date
    following_friday = get_following_friday(date_obj)

    # Determine Walmart fiscal year
    if date_obj.month == 1 & following_friday.month != 2:
        fiscal_year = date_obj.year - 1
    else:
        fiscal_year = date_obj.year

    # Find the first Friday in Feburary of the fiscal year we just found
    feb_1 = date(fiscal_year, 2, 1)
    first_feb_friday = get_following_friday(feb_1)

    # Get the first day of the WM Week that ends on the first Friday we just found
    fiscal_year_start_date = first_feb_friday - timedelta(days=6)
    return fiscal_year_start_date
