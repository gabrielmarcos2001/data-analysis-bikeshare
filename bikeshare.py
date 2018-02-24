import time
import datetime
import render_engine as re
import user_input
import cvs_tools
import formulas as f

YEAR = 2017 # Constants for defining the year we are processing
PRINT_DEBUG_LOGS = False # Constant for defining if we want to print debug logs for calculating time processing
INDIVIDUAL_DATA_CHUNK_SIZE = 5

def prepare_city_data(city_data):
    '''Process the city data object normalizing column names and data types

    Args:
        (dictionary) city data dictionary to process.
    Returns:
        (dictionary): city data dictionary cleaned up
    '''
    for data in city_data:

            data["start_time"] = cvs_tools.parse_date(data["Start Time"])
            del(data['Start Time'])

            data["end_time"] = cvs_tools.parse_date(data["End Time"])
            del(data["End Time"])

            data["trip_duration"] = int(cvs_tools.parse_float(data["Trip Duration"]))
            del(data["Trip Duration"])

            data["start_station"] = data["Start Station"]
            del(data["Start Station"])

            data["end_station"] = data["End Station"]
            del(data["End Station"])

            data["user_type"] = data["User Type"]
            del(data["User Type"])

            data["gender"] = data["Gender"]
            del(data["Gender"])

            data["birth_year"] = int(cvs_tools.parse_float(data["Birth Year"])) if cvs_tools.parse_float(data["Birth Year"]) else None
            del(data["Birth Year"])

    return city_data

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''

    # Gets user raw input for city to process
    city_file_name = user_input.get_city()

    # Loads the data for the selectec city only if we don't have it preloaded
    if city_file_name not in cities_data:
        start_time = time.time()

        # Data for the city goes to a dictionary after parsed. 
        # Parsing is used to assign proper data types and clean up 
        # column names
        cities_data[city_file_name] = prepare_city_data(cvs_tools.read_csv(city_file_name))
        
        if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))

    # Selected city data
    city_data = cities_data[city_file_name]

    # Gets the user raw input for time period - valid values are
    # none, month, day
    time_period = user_input.get_time_period()

    # Stores the selected month - day. These variables will have data
    # depending on the user selected time period and are used
    # for filteing 
    month_data = None
    day = None

    # When time_period is month or day we need to ask for extra 
    # data to the user
    if time_period == 'day' or time_period == 'month':

        # Gets the user raw input for month
        month_data = user_input.get_month(YEAR)

        # If user selected day as time period then we also get the user
        # raw input for day based on the month selected
        if time_period == 'day':
            day = user_input.get_day(YEAR, month_data["month_index"])

    if PRINT_DEBUG_LOGS: print('Calculating the first statistic...')

    print('\nProcessing Data... \n')

    # What is the most popular month for start time?
    # For calculating the most popular month - Time period needs to
    # be 'none'
    if time_period == 'none':

        # Begin - Most popular month
        start_time = time.time()
        
        # Gets the most popular month
        mp_month = f.popular_month(city_data, YEAR)

        # Prints the result for the most popular month
        re.render_most_popular_month(mp_month, YEAR)

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
        mp_day = f.popular_day(city_data, month_data)
        
        # Prints the most popular day
        re.render_most_popular_day(mp_day, YEAR, month_data)
        
        if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
        if PRINT_DEBUG_LOGS: print("Calculating the next statistic...") 

        # End - Most popular day   

    # What is the most popular hour of day for start time?
    # Begin - Most popular Hour
    start_time = time.time()

    # Gets the most popular hour 
    mp_hour = f.popular_hour(city_data,month_data,day)

    # Prints the most popular hour
    re.render_most_popular_hour(mp_hour, YEAR, month_data, day)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")
    # End - Most popular hour

    # Begin - Total trip duration - Average trip duration
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # Gets the total trip duration and average trip duration for the specified time period
    total_trip_duration, average_trip_duration = f.trip_duration(city_data,month_data,day)

    # Prints the result for the total trip duration and average trip duration
    re.render_trip_duration(total_trip_duration, average_trip_duration, YEAR, month_data, day)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - Total Trip Duration - Average Trip Duration

    # Begin - Most popular start and end stations
    start_time = time.time()

    # Gets the most popular start station and the most popular end station
    mp_start_station, mp_end_station = f.popular_stations(city_data,month_data,day)

    # Prints the result for the most popular start station and most popular end station
    re.render_most_popular_stations(mp_start_station, mp_end_station, YEAR, month_data,day)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - Most popular start and end station

    # Begin - Most popular trip
    start_time = time.time()

    # Gets the Start Station - End Station for the most popular trip
    start_station, end_station = f.popular_trip(city_data,month_data,day)

    # Prints the most popular trip result
    re.render_most_popular_trip(start_station, end_station, YEAR, month_data, day)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - Most popular trip

    # Begin - User Types count
    start_time = time.time()

    # Gets the counts for each user count
    user_types = f.users(city_data,month_data,day)

    # Prints the result for each user count
    re.render_user_types_count(user_types, YEAR, month_data,day)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")

    # End - User types count

    # Begin - Gender counts
    start_time = time.time()

    # Gets the number of users by gender
    gender_count = f.gender(city_data,month_data,day)

    # Prints the gender count
    re.render_gender_count(gender_count, YEAR, month_data, day)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))
    if PRINT_DEBUG_LOGS: print("Calculating the next statistic...")
    # End - Gender Count

    # Begin - Birth years
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    min_year, max_year, mp_year = f.birth_years(city_data,month_data,day)

    # Prints the Birth years result
    re.render_birth_years(min_year, max_year, mp_year, YEAR, month_data, day)

    if PRINT_DEBUG_LOGS: print("That took %s seconds." % (time.time() - start_time))

    # End - Birth years

    # Display five lines of data at a time if user specifies that they would like to
    offset = 0
        
    while user_input.get_display_data(offset, offset + INDIVIDUAL_DATA_CHUNK_SIZE):
        re.render_individual_data(city_data,offset,INDIVIDUAL_DATA_CHUNK_SIZE)
        offset += INDIVIDUAL_DATA_CHUNK_SIZE

        if offset > len(city_data):
            re.render_no_data_available()
            break

    # Restart?
    if user_input.get_restart_experience():
        statistics()

if __name__ == "__main__":

    # Dictionary for storing the city data by file 
    # defined in __main__ to manatain the scope during several
    # executions of statistics()
    cities_data = {}

    statistics()