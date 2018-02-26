import time
import datetime
import calendar
import unicodecsv
from datetime import datetime as dt

YEAR = 2017 # Constants for defining the year we are processing
PRINT_DEBUG_LOGS = False # Constant for defining if we want to print debug logs for calculating time processing
INDIVIDUAL_DATA_CHUNK_SIZE = 5

## Filenames
chicago = 'chicago.csv'
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


def get_max(dictionary):
    '''Takes a dicationary and returns the key with a max value 
    Args:
        (dic): data needs to be in the form of {key:"key", value:1 }
    Returns:
        (str): Key with the max value in the dictionary
    '''
    max_key = None
    max_value = -1

    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

def read_csv(file):
    '''Opens a file by its name and returns a dictionary with the content

    Args:
        filename to open
    Returns:
        (dictionary) file content
    '''
    print('Reading data from {}...'.format(file))
        
    try:
        with open(file,'rb') as f:
            reader = unicodecsv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return None

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

def render_most_popular_month(most_popular_month):
    '''Prints the most popular month name in screen

    Args:
        (str) most popular month name.
    Returns:
        None
    '''

    print('\n')

    if most_popular_month:
        print("Most popular month for starting trips was {}".format(most_popular_month))
    else:
        print("Most popular month could not be calculated")


def render_most_popular_day(most_popular_day):
    '''Prints the most popular day in screen

    Args:
        (int) most popular day
    Returns:
        None
    '''

    print('\n')

    if most_popular_day:
        print("Most popular day for starting trips was {}".format(most_popular_day))
    else:
        print("Most popular day could not be calculated")
    

def render_most_popular_hour(most_popular_hour):
    '''Prints the most popular hour in screen

    Args:
        (str) most popular hour
    Returns:
        None
    '''

    print('\n')

    if most_popular_hour:
        print("Most popular hour for starting trips was {} Hs.".format(most_popular_hour))
    else:
        print("Most popular hour for starting trips could not be calculated")


def render_trip_duration(total_trip_duration, average_trip_duration):
    '''Prints the total trip duration and average trip duration in the screen

    Args:
        (str) total_trip_duration
        (str) average_trip_duration
    Returns:
        None
    '''

    print('\n')

    if total_trip_duration:
        print("Total trip duration was {}".format(display_time(total_trip_duration,5)))
    else:
        print("Total trip duration could not be calculated")

    if average_trip_duration:
        print("Average trip duration was {}".format(display_time(average_trip_duration,2)))
    else:
        print("Average trip duration could not be calculated")


def render_most_popular_stations(most_popular_start_station, most_popular_end_station):
    '''Prints the most popular end and start station in screen

    Args:
        (str) most popular start station
        (str) most popular end station
    Returns:
        None
    '''

    print('\n')

    if most_popular_start_station:
        print("Most popular Start Station was {}".format(most_popular_start_station))
    else:
        print("Most popular Start Station could not be calculated")

    if most_popular_end_station:
        print("Most popular End Station was {}".format(most_popular_end_station))
    else:
        print("Most popular End Station could not be calculated")

    

def render_most_popular_trip(start_station, end_station):
    '''Prints the most popular trip between 2 stations in screen

    Args:
        (str) start station for the trip
        (str) end station for the trip
    Returns:
        None
    '''

    print('\n')

    if start_station and end_station:
        print("Most popular Trip was from {} to {}".format(start_station, end_station))
    else:
        print("Most popular Trip could not be calculated")


def render_user_types_count(user_types):
    '''Prints the total number of users of each type in screen

    Args:
        (list) list of user types dictionary in the form of {user_type = counter}
    Returns:
        None
    '''

    print('\n')

    for user_type, count in user_types.items():
        print("Number of users of type {} was {}".format(user_type, count))


def render_gender_count(gender_count):
    '''Prints the total total number of users by gender in screen

    Args:
        (list) list of genders dictionary in the form of {gender = counter}
    Returns:
        None
    '''

    print('\n')

    for g, count in gender_count.items():
        print("Number of {} users was {}".format(g, count))


def render_birth_years(min_year, max_year, most_popular_year):
    '''Prints the Youngest, Oldest and most popular year of birth in screen

    Args:
        (int) min_year
        (int) max_year
        (int) most_popular_year
    Returns:
        None
    '''

    print('\n')

    if min_year:
        print("Youngest user was born in {}".format(min_year))
    else:
        print("Youngest user could not be calculated")

    if max_year:
        print("Oldest user was born in {}".format(max_year))
    else:
        print("Oldest users could not be calculated")

    if most_popular_year:
        print("Most popular year of birth was {}".format(most_popular_year))
    else:
        print("Most popular year of birth could not be calculated")


def render_individual_data(city_data, offset, num_lines):
    ''' Renders a set of trip data lines for a city in the screen. Supports sending 
    an offset as start position and the chunk_size with the number of lines to render

    Args:
        (list) city data dictionary
        (int) offset for starting line 
        (int) number of lines to be printed
    Returns:
        None
    '''

    print('\n')

    for i in range(num_lines):

        i += offset
        # checks if we have reached the limit of the list
        if i > len(city_data)-1: break

        # Prints the data well-formatted and increments the list index
        print('Start Time: {} - End Time: {} - Trip Duration in seconds: {} - Start Station: {} - End Station: {} - User Type: {} - Gender: {} - Year of Birth: {}\n'
            .format(city_data[i]["start_time"], city_data[i]["end_time"], city_data[i]["trip_duration"], city_data[i]["start_station"], city_data[i]["end_station"], city_data[i]["user_type"], city_data[i]["gender"], city_data[i]["birth_year"]))
        i += 1


def render(message):
    ''' Renders a message in screen

    Args:
        (str) message to be rendered
    Returns:
        None
    '''

    print("\n{}".format(message))


intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),    # 60 * 60 * 24
        ('hours', 3600),    # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
        )

def display_time(seconds, granularity=2):
    ''' Returns a well-formatted string in the form of weeks, days, hours, etc from 
    a specific number of seconds.
    Function was implemented from: https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days

    Args:
        (int) total number of seconds
        (int) level of granularity for the formatting - should be in between 1 - 5
    Returns:
        (str) well-formatted string
    '''

    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
            
    return ', '.join(result[:granularity])

def prepare_city_data(city_data):
    '''Process the city data object normalizing column names and data types

    Args:
        (dictionary) city data dictionary to process.
    Returns:
        (dictionary): city data dictionary cleaned up
    '''
    for data in city_data:

            data["start_time"] = parse_date(data["Start Time"])
            del(data['Start Time'])

            data["end_time"] = parse_date(data["End Time"])
            del(data["End Time"])

            data["trip_duration"] = int(parse_float(data["Trip Duration"]))
            del(data["Trip Duration"])

            data["start_station"] = data["Start Station"]
            del(data["Start Station"])

            data["end_station"] = data["End Station"]
            del(data["End Station"])

            data["user_type"] = data["User Type"]
            del(data["User Type"])

            if "Gender" in data:
                data["gender"] = data["Gender"]
                del(data["Gender"])
            else:
                data["gender"] = None

            if "Birth Year" in data:
                data["birth_year"] = int(parse_float(data["Birth Year"])) if parse_float(data["Birth Year"]) else None
                del(data["Birth Year"])
            else:
                data["birth_year"] = None

    return city_data

def birth_years(city_data, year, month, day):
    '''Process the city_data list for calculating the oldest user, 
    youngest user, and most popular year of birth in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (int): year of birth for the oldest user - None if could not be calculated
        (int): year of birth of the youngest user - None if could not be calculated
        (int): most popular year of birth - None if could not be calculated
    '''

    # Dictionary for counting occurrences of each year
    year_count = {}

    # Holds the min year value
    min_year = 0

    # Holds the max year value
    max_year = 0

    for data in city_data:
        # Checks entry should be processed 
        if not check_valid_start_date(data["start_time"],year,month,day):
            continue

        # Checks birth year data exists
        if not data["birth_year"]:
            continue

        # Summarize year count
        if data["birth_year"] in year_count:
            year_count[data["birth_year"]] += 1
        else:
            year_count[data["birth_year"]] = 1

        # Sets max year
        if data["birth_year"] > max_year:
            max_year = data["birth_year"]

        # Sets min year
        if data["birth_year"] < min_year or min_year == 0:
            min_year = data["birth_year"]

    return None if min_year == 0 else min_year, None if max_year == 0 else max_year, get_max(year_count)

def gender(city_data, year, month, day):
    '''Process the city_data list for calculating the counts
    by gender in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (dictionary): counts by gender in the form of {"Male":12, "Female":22}
    '''
    
    # Dictionary for counting occurrences by gender
    gender_count = {}

    for data in city_data:
        # Checks entry should be processed 
        if not check_valid_start_date(data["start_time"],year,month,day):
            continue

        # Checks we have Gender data in the dictionary 
        # otherwise, are counted as "Undefined"
        gender = data["gender"]
        if gender == None or gender == "":
            gender = "Undefined"

        # Counts by gender
        if gender in gender_count:
            gender_count[gender] += 1
        else:
            gender_count[gender] = 1

    return gender_count

def popular_day(city_data, year, month):
    '''Process the city_data list for calculating the most popular
    day of week ( Monday, Tuesday, etc) for a start time in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (str): Most popular day of week ( Monday, Tuesday, etc)
    '''
    
    # Dictionary for counting occurrences by week day
    day_popularity_counter = {}

    for data in city_data:
        # Checks entry should be processed 
        if not check_valid_start_date(data["start_time"],year,month,None):
            continue

        # Counts popularity by weekday
        if data["start_time"].weekday() in day_popularity_counter:
            day_popularity_counter[data["start_time"].weekday()] += 1
        else:
            day_popularity_counter[data["start_time"].weekday()] = 1

    popular_day_index = get_max(day_popularity_counter)

    if popular_day_index:
        return calendar.day_name[get_max(day_popularity_counter)]
    else:
        return None

def popular_hour(city_data, year, month, day):
    '''Process the city_data list for calculating the most popular
    hour of day for a start time in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (int): most popular hour of day in 24 hs format
    '''

    # Dictionary for counting occurrences by hour of day
    hour_popularity_counter = {}

    for data in city_data:
        # Checks entry should be processed 
        if not check_valid_start_date(data["start_time"],year,month,day):
            continue

        # Counts hours 
        if data["start_time"].hour in hour_popularity_counter:
            hour_popularity_counter[data["start_time"].hour] += 1
        else:
            hour_popularity_counter[data["start_time"].hour] = 1

    return get_max(hour_popularity_counter)

def popular_month(city_data, year):
    '''Process the city_data list for calculating the most popular
    month for start time in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (str): Name of the most popular month
    '''

    # Dictionary for counting occurrences by month
    months_popularity_counter = {}

    for data in city_data:
        # Checks entry should be processed 
        if not check_valid_start_date(data["start_time"],year,None,None):
            continue

        # Counts by month
        if data["start_time"].month in months_popularity_counter:
            months_popularity_counter[data["start_time"].month] += 1
        else:
            months_popularity_counter[data["start_time"].month] = 1

    if months_popularity_counter:
        return datetime.date(year, get_max(months_popularity_counter), 1).strftime('%B')
    else:
        return None

def popular_stations(city_data, year, month, day):
    '''Process the city_data list for calculating the most popular
    start and most popular end stations in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (str): Name of the most popular start station
        (str): Name of the most popular end station
    '''

    # Dictionary for counting the most popular start station
    start_station_popularity_counter = {}
    # Dictionary for counting the most popular end station
    end_station_popularity_counter = {}

    for data in city_data:
        # Checks entry should be processed
        if not check_valid_start_date(data["start_time"],year,month,day):
            continue

        # Counts start station
        if data["start_station"] in start_station_popularity_counter:
            start_station_popularity_counter[data["start_station"]] += 1
        else:
            start_station_popularity_counter[data["start_station"]] = 1

        # Counts end station
        if data["end_station"] in end_station_popularity_counter:
            end_station_popularity_counter[data["end_station"]] += 1
        else:
            end_station_popularity_counter[data["end_station"]] = 1

    return get_max(start_station_popularity_counter), get_max(end_station_popularity_counter)

def popular_trip(city_data, year, month, day):
    '''Process the city_data list for calculating the most popular 
    trip in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (str): Start station for the most popular trip
        (str): End station for the most popular trip
    '''

    # Dictionary for counting the trip occurrences
    most_popular_trip_counter = {}

    # Dictionary for storing trip hash - stations data association
    stations_dict = {}

    for data in city_data:
        # Checks entry should be processed
        if not check_valid_start_date(data["start_time"],year,month,day):
            continue

        # Creates a unique hash key combinend the start and end station
        dict_key = str(hash(data["start_station"] + ";" + data["end_station"]))

        # Counts the number of occurrences of the trip hash 
        if dict_key in most_popular_trip_counter:
            most_popular_trip_counter[dict_key] += 1
        else:
            most_popular_trip_counter[dict_key] = 1

        # Initialize the trip hash with the start and end stations data
        stations_dict[dict_key] = {}
        stations_dict[dict_key]["start_station"] = data["start_station"]
        stations_dict[dict_key]["end_station"] = data["end_station"]

    if most_popular_trip_counter:
        # Gets the has with highest occurrences and returns the start station and end station for that hash
        max_hash = get_max(most_popular_trip_counter)
        return stations_dict[max_hash]["start_station"], stations_dict[max_hash]["end_station"]
    else:
        return None, None
    

def trip_duration(city_data, year, month, day):
    '''Process the city_data list for calculating the total trip duration
    and average trip duration in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (int): total trip duration in seconds
        (int): average trip duration in seconds
    '''

    total_trip_duration_seconds = 0
    average_trip_duration_seconds = 0

    for data in city_data:
        # Checks entry should be processed
        if not check_valid_start_date(data["start_time"],year,month,day):
            continue

        # Summarize total trip duration
        total_trip_duration_seconds += data["trip_duration"]

    # Calculates average trip duration in seconds
    average_trip_duration_seconds = total_trip_duration_seconds // len(city_data)

    return total_trip_duration_seconds, average_trip_duration_seconds

def users(city_data, year, month, day):
    '''Process the city_data list for calculating the counts 
    for each user type in a specific time period

    Args:
        (list): list with the city_data dictionary.
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (dictionary): counts by user type in the form of {"Customer":12, "Other type":13}
    '''

    # Dictionary four counting users by type
    user_types_count = {}

    for data in city_data:
        # Checks entry should be processed
        if not check_valid_start_date(data["start_time"],year,month,day):
            continue

        # Counts by user type
        if data["user_type"] in user_types_count:
            user_types_count[data["user_type"]] += 1
        else:
            user_types_count[data["user_type"]] = 1

    return user_types_count

def check_valid_start_date(date, year, month, day):
    '''Checks if the datetime object shuold be processed 
    based on the filters for year, month, day passed as arguemnts

    Args:
        (int): year for filtering data - Optional, pass None if no filtering by year is required 
        (dictionary): month for filtering data - Dictionary in the form of {month_index:"1", month_name:"January"} - Optional, pass None if no filtering by month is required
        (int) day for filtering data - Optional, pass None if no filtering by day is required
    Returns:
        (bool): True if datetime object is valid for the filtering options / False otherwise
    '''
    if month != None:
        if date.month != month["month_index"]:
            return False
    if day != None:
        if date.day != day:
            return False
    if year != None:
        if date.year != year:
            return False
    return True

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''

    # Gets user raw input for city to process
    city_file_name, city_name = get_city()

    # Loads the data for the selectec city only if we don't have it preloaded
    if city_file_name not in cities_data:
        
        start_time = time.time()

        # Data for the city goes to a dictionary after parsed. 
        # Parsing is used to assign proper data types and clean up 
        # column names
        raw_city_data = read_csv(city_file_name)

        # Validates the file exists in the root directory or displays an error message and terminates program otherwise
        if raw_city_data:
            cities_data[city_file_name] = prepare_city_data(raw_city_data)
            if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
        else:
            render("Sorry, There was an error opening the data file. Please check {} exists in the root directory".format(city_file_name))
            return

    # Selected city data
    city_data = cities_data[city_file_name]

    # Gets the user raw input for time period - valid values are
    # none, month, day
    time_period = get_time_period()

    # Stores the selected month - day. These variables will have data
    # depending on the user selected time period and are used
    # for filteing 
    month_data = None
    day = None

    # When time_period is month or day we need to ask for extra 
    # data to the user
    if time_period == 'day' or time_period == 'month':

        # Gets the user raw input for month
        month_data = get_month(YEAR)

        # If user selected day as time period then we also get the user
        # raw input for day based on the month selected
        if time_period == 'day':
            day = get_day(YEAR, month_data["month_index"])

    if PRINT_DEBUG_LOGS: print('Calculating the first statistic...')

    if month_data:
        if day:
            render('Processing Data for {} in {}, {} {}...'.format(city_name,day, month_data["month_name"],YEAR))
        else:
            render('Processing Data for {} in {} {}...'.format(city_name,month_data["month_name"],YEAR))
    else:
        render('Processing Data for {} in {}...'.format(city_name,YEAR))
        

    # What is the most popular month for start time?
    # For calculating the most popular month - Time period needs to
    # be 'none'
    if time_period == 'none':

        # Begin - Most popular month
        start_time = time.time()
        
        # Gets the most popular month
        mp_month = popular_month(city_data, YEAR)

        # Prints the result for the most popular month
        render_most_popular_month(mp_month)

        if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
        if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

        # Ends - Most popular month

    # What is the most popular day for start time?
    # For calculating the most popular day - Time period needs to 
    # be either 'none' or 'month'
    if time_period == 'none' or time_period == 'month':

        # Begin - Most popular day
        start_time = time.time()
        
        # Gets the most popular day
        mp_day = popular_day(city_data, YEAR, month_data)
        
        # Prints the most popular day
        render_most_popular_day(mp_day)
        
        if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
        if PRINT_DEBUG_LOGS: print("Calculating the next statistic...") 

        # End - Most popular day   

    # What is the most popular hour of day for start time?
    # Begin - Most popular Hour
    start_time = time.time()

    # Gets the most popular hour 
    mp_hour = popular_hour(city_data,YEAR,month_data,day)

    # Prints the most popular hour
    render_most_popular_hour(mp_hour)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")
    # End - Most popular hour

    # Begin - Total trip duration - Average trip duration
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # Gets the total trip duration and average trip duration for the specified time period
    total_trip_duration, average_trip_duration = trip_duration(city_data,YEAR,month_data,day)

    # Prints the result for the total trip duration and average trip duration
    render_trip_duration(total_trip_duration, average_trip_duration)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - Total Trip Duration - Average Trip Duration

    # Begin - Most popular start and end stations
    start_time = time.time()

    # Gets the most popular start station and the most popular end station
    mp_start_station, mp_end_station = popular_stations(city_data,YEAR,month_data,day)

    # Prints the result for the most popular start station and most popular end station
    render_most_popular_stations(mp_start_station, mp_end_station)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - Most popular start and end station

    # Begin - Most popular trip
    start_time = time.time()

    # Gets the Start Station - End Station for the most popular trip
    start_station, end_station = popular_trip(city_data,YEAR,month_data,day)

    # Prints the most popular trip result
    render_most_popular_trip(start_station, end_station)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - Most popular trip

    # Begin - User Types count
    start_time = time.time()

    # Gets the counts for each user count
    user_types = users(city_data,YEAR,month_data,day)

    # Prints the result for each user count
    render_user_types_count(user_types)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - User types count

    # Begin - Gender counts
    start_time = time.time()

    # Gets the number of users by gender
    gender_count = gender(city_data,YEAR,month_data,day)

    # Prints the gender count
    render_gender_count(gender_count)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")
    # End - Gender Count

    # Begin - Birth years
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    min_year, max_year, mp_year = birth_years(city_data,YEAR,month_data,day)

    # Prints the Birth years result
    render_birth_years(min_year, max_year, mp_year)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))

    # End - Birth years

    # Display five lines of data at a time if user specifies that they would like to
    offset = 0
        
    while get_display_data(offset, offset + INDIVIDUAL_DATA_CHUNK_SIZE):
        render_individual_data(city_data,offset,INDIVIDUAL_DATA_CHUNK_SIZE)
        offset += INDIVIDUAL_DATA_CHUNK_SIZE

        if offset > len(city_data):
            render("There is no more data available")
            break

    # Restart?
    if get_restart_experience():
        statistics()

if __name__ == "__main__":

    # Dictionary for storing the city data by file 
    # defined in __main__ to manatain the scope during several
    # executions of statistics()
    cities_data = {}

    statistics()