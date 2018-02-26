import datetime
import calendar

## Filenames
chicago = 'chicago_sh.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city in rw inpyt and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
        (str) City input by the user
    '''

    # Initializes a dictionary for storing the city - filename reference
    city_file = {}

    city_file["chicago"] = chicago
    city_file["new york"] = new_york_city
    city_file["washington"] = washington

    request_city = True

    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')

    # Requests the city to the user until they enter valid data
    while request_city:
        # For the input data to be valid it needs to exist in the files-cities dictionary, otherwise we keep asking for user input
        if city.lower() not in city_file.keys():
            city = input('We are sorry, we are expanding our operations worldwide, but for now please enter Chicago, New York or Washington\n')
        else:
            request_city = False

    # City file name
    return city_file[city.lower()], city


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str): time period selected by the user, in the form of 'month', 'day', 'none'
    '''

    # Initializes a set with the valid inputs for period
    time_periods_valid = set()

    time_periods_valid.add("month")
    time_periods_valid.add("day")
    time_periods_valid.add("none")

    do_request_time_period = True

    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')

    # Requests the period to the user until they enter valid data
    while do_request_time_period:
        # For the input data to be valid it needs to exist in the time_periods_valid set, otherwise we keep asking for user input
        if time_period.lower() not in time_periods_valid:
            time_period = input('We are sorry, please anter a valid time period in the form of \'month\', \'day\', \'none\', \n')
        else:
            do_request_time_period = False

    # Time period in lower case
    return time_period.lower()

def get_month(year):
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        dicttionary with the selected mont info in the form of '{'month_index':1, 'month_name':January}'
    '''

    months_data = {}
    
    # Initialize a set with the index of the valid months
    month_index_valid = set()
    month_index_valid.add(1) # January
    month_index_valid.add(2) # February
    month_index_valid.add(3) # March
    month_index_valid.add(4) # April
    month_index_valid.add(5) # May
    month_index_valid.add(6) # June

    # Generates a dictionary holding all the months information - key is the month name in lowercase. 
    for i in range(1,13):

        # Gets the month name from the month index
        month_name = datetime.date(year, i, 1).strftime('%B')

        # Initialize the months_data dictionary - Stores the month index, the month name and valid True/False if the index is 
        # included in the set of valid months
        months_data[month_name.lower()] = {"month_index":i, "month_name":month_name, "valid":i in month_index_valid}

    do_request_month = True

    # Asks for month data to the user
    month = input('\nWhich month? January, February, March, April, May, or June?\n')

    while do_request_month:

        # validates the user input is a valid month - If its not in the months_data keys, then it is not even a month 
        if month.lower() not in months_data.keys():
            month = input('\nSorry, that is not a valid month, please enter January, February, March, May or June\n')
        else:
            # If the month input by the user is a month, then we validate that it is one of the valid months accepted in the input
            if months_data[month.lower()]["valid"]:
                do_request_month = False
            else: 
                # If the mont input by the user is a month, but not valid then we display a custom error message to enforce only the valid months
                month = input('\nSorry, it looks like people don\'t ride byciles in {}, please enter January, February, March, May or June\n'.format(month))

    # Dictionary with all the month data
    return {"month_index":months_data[month.lower()]["month_index"],"month_name":months_data[month.lower()]["month_name"]}


def get_day(year, month):
    '''Asks the user for a day and returns the specified day.

    Args:
        (int): month index - is required to validate the day input is in between the number of days for the selected month
    Returns:
        (int): selected day
    '''

    do_request_day = True

    day = input('\nWhich day? Please type your response as an integer.\n')

    while do_request_day:
        try:
            # validates the input is a number
            int_day = int(day)

            # validates the day entered is in between the valid days for the selected month
            max_month_days = calendar.monthrange(year, month)[1]
            if int_day < 1 or int_day > max_month_days:
                day = input('\nDay shuold be in between 1 and {}\n'.format(max_month_days))
            else:
                # day is valid
                do_request_day = False
        except ValueError:
            # input was not a number
            day = input('\nPlease type your response as an integer.\n')

    # Day input as an integer
    return int_day
    

def get_restart_experience():
    '''Asks the user for a yes or no if they want to restart the experience.

    Args:
        None
    Returns:
        (bool): True if user selected yes
    '''
    
    do_request_restart_option = True

    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')

    while do_request_restart_option:
        if restart.lower() == 'yes': return True
        if restart.lower() == 'no': return False
        restart = input('\nPlease type \'yes\' or \'no\'.\n')


def get_display_data(start_row, end_row):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''

    do_request_display_data_option = True

    display = input('\nWould you like to view individual trip data from line {} to line {}?\n'
                    'Type \'yes\' or \'no\'.\n'.format(start_row, end_row))

    while do_request_display_data_option:
        if display.lower() == 'yes': return True
        if display.lower() == 'no': return False
        display = input('\nPlease type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    