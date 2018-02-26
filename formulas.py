import dic_utils as utils
import calendar
import datetime

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

    return None if min_year == 0 else min_year, None if max_year == 0 else max_year, utils.get_max(year_count)

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

    popular_day_index = utils.get_max(day_popularity_counter)

    if popular_day_index:
        return calendar.day_name[utils.get_max(day_popularity_counter)]
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

    return utils.get_max(hour_popularity_counter)

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
        return datetime.date(year, utils.get_max(months_popularity_counter), 1).strftime('%B')
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

    return utils.get_max(start_station_popularity_counter), utils.get_max(end_station_popularity_counter)

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
        max_hash = utils.get_max(most_popular_trip_counter)
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
