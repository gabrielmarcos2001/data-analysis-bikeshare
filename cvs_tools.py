import unicodecsv
from datetime import datetime as dt

def read_csv(file):
    '''Opens a file by its name and returns a dictionary with the content

    Args:
        filename to open
    Returns:
        (dictionary) file content
    '''
    print('Reading data from {}...'.format(file))
        
    with open(file,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def parse_date(date):
    '''Takes a date as a string, and returns a Python datetime object. 
    If there is no date given, returns None

    Args:
        (str): date string in the form of YYYY-MM-DD HH:MM:SS
    Returns:
        (datetime): date object - None if invalid
    '''
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d %H:%M:%S')

def parse_float(f):
    '''Takes a float as a string, and returns a float number. 
    If there is no date given, returns None
    Args:
        (str): float number as string
    Returns:
        (float): float number - None if invalid
    '''

    if f == '':
        return None
    else:
        return float(f)