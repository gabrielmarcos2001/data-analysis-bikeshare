
def render_most_popular_month(most_popular_month, year):
    '''Prints the most popular month name for a specific year in screen

    Args:
        (str) most popular month name.
        (int) year
    Returns:
        None
    '''

    if most_popular_month:
        print("Most popular month for starting trips in {} was {}".format(year,most_popular_month))
    else:
        print("Most popular month could not be calculated for {}".format(year))


def render_most_popular_day(most_popular_day, year, month):
    '''Prints the most popular day for a specific year and month in screen

    Args:
        (int) most popular day
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
    Returns:
        None
    '''

    if most_popular_day:
        if month:
            print("Most popular day for starting trips in {}, {} was {}".format(month["month_name"], year,most_popular_day))
        else:
            print("Most popular day for starting trips in {} was {}".format(year,most_popular_day))
    else:
        if month:
            print("Most popular day could not be calculated for {}, {}".format(month["month_name"], year))
        else:
            print("Most popular day could not be calculated for {}".format(year))
    

def render_most_popular_hour(most_popular_hour, year, month, day):
    '''Prints the most popular hour for a specific year, month and day in screen

    Args:
        (str) most popular hour
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
        (int) day
    Returns:
        None
    '''

    if most_popular_hour:
        if month:
            if day:
                print("Most popular hour for starting trips in {} {}, {} was {} Hs.".format(month["month_name"], day, year,most_popular_hour))
            else:
                print("Most popular hour for starting trips in {}, {} was {} Hs.".format(month["month_name"], year,most_popular_hour))
        else:
            print("Most popular hour for starting trips in {} was {} Hs.".format(year,most_popular_hour))
    else:
        if month:
            if day:
                print("Most popular hour for starting trips in {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Most popular hour for starting trips in {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Most popular hour for starting trips in {} could not be calculated".format(year))


def render_trip_duration(total_trip_duration, average_trip_duration, year, month, day):
    '''Prints the total trip duration and average trip duration for a specific year, month and day in screen

    Args:
        (str) total_trip_duration
        (str) average_trip_duration
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
        (int) day
    Returns:
        None
    '''

    if total_trip_duration:
        if month:
            if day:
                print("Total trip duration for {} {}, {} was {}".format(month["month_name"], day, year,display_time(total_trip_duration,5)))
            else:
                print("Total trip duration for {}, {} was {}".format(month["month_name"], year, display_time(total_trip_duration,5)))
        else:
            print("Total trip duration for {} was {}".format(year,display_time(total_trip_duration,5)))
    else:
        if month:
            if day:
                print("Total trip duration for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Total trip duration for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Total trip duration for {} could not be calculated".format(year))

    if average_trip_duration:
        if month:
            if day:
                print("Average trip duration for {} {}, {} was {}".format(month["month_name"], day, year, display_time(average_trip_duration,2)))
            else:
                print("Average trip duration for {}, {} was {}".format(month["month_name"], year, display_time(average_trip_duration,2)))
        else:
            print("Average trip duration for {} was {}".format(year, display_time(average_trip_duration,2)))
    else:
        if month:
            if day:
                print("Average trip duration for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Average trip duration for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Average trip duration for {} could not be calculated".format(year))


def render_most_popular_stations(most_popular_start_station, most_popular_end_station, year, month, day):
    '''Prints the most popular end and start station for a specific year, month and day in screen

    Args:
        (str) most popular start station
        (str) most popular end station
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
        (int) day
    Returns:
        None
    '''

    if most_popular_start_station:
        if month:
            if day:
                print("Most popular Start Station for {} {}, {} was {}".format(month["month_name"], day, year, most_popular_start_station))
            else:
                print("Most popular Start Station for {}, {} was {}".format(month["month_name"], year, most_popular_start_station))
        else:
            print("Most popular Start Station for {} was {}".format(year, most_popular_start_station))
    else:
        if month:
            if day:
                print("Most popular Start Station for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Most popular Start Station for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Most popular Start Station for {} could not be calculated".format(year))

    if most_popular_end_station:
        if month:
            if day:
                print("Most popular End Station for {} {}, {} was {}".format(month["month_name"], day, year, most_popular_end_station))
            else:
                print("Most popular End Station for {}, {} was {}".format(month["month_name"], year, most_popular_end_station))
        else:
            print("Most popular End Station for {} was {}".format(year, most_popular_end_station))
    else:
        if month:
            if day:
                print("Most popular End Station for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Most popular End Station for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Most popular End Station for {} could not be calculated".format(year))

    

def render_most_popular_trip(start_station, end_station, year, month, day):
    '''Prints the most popular trip between 2 stations for a specific year, month and day in screen

    Args:
        (str) start station for the trip
        (str) end station for the trip
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
        (int) day
    Returns:
        None
    '''

    if start_station and end_station:
        if month:
            if day:
                print("Most popular Trip for {} {}, {} was from {} to {}".format(month["month_name"], day, year, start_station, end_station))
            else:
                print("Most popular Trip for {}, {} was from {} to {}".format(month["month_name"], year, start_station, end_station))
        else:
            print("Most popular Trip for {} was from {} to {}".format(year, start_station, end_station))
    else:
        if month:
            if day:
                print("Most popular Trip for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Most popular Trip for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Most popular Trip for {} could not be calculated".format(year))


def render_user_types_count(user_types, year, month, day):
    '''Prints the total number of users of each type for a specific year, month and day in screen

    Args:
        (list) list of user types dictionary in the form of {user_type = counter}
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
        (int) day
    Returns:
        None
    '''

    for user_type, count in user_types.items():
        if month:
            if day:
                print("Number of users of type {} for {} {}, {} was {}".format(user_type, month["month_name"], day, year, count))
            else:
                print("Number of users of type {} for {}, {} was {}".format(user_type, month["month_name"], year, count))
        else:
            print("Number of users of type {} for {}, was {}".format(user_type, year, count))


def render_gender_count(gender_count, year, month, day):
    '''Prints the total total number of users by gender for a specific year, month and day in screen

    Args:
        (list) list of genders dictionary in the form of {gender = counter}
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
        (int) day
    Returns:
        None
    '''

    for g, count in gender_count.items():
        if month:
            if day:
                print("Number of {} users for {} {}, {} was {}".format(g, month["month_name"], day, year, count))
            else:
                print("Number of {} users for {}, {} was {}".format(g, month["month_name"], year, count))
        else:
            print("Number of {} users for {}, was {}".format(g, year, count))


def render_birth_years(min_year, max_year, most_popular_year, year, month, day):
    '''Prints the Youngest, Oldest and most popular year of birth for a specific year, month and day in screen

    Args:
        (int) min_year
        (int) max_year
        (int) most_popular_year
        (int) year
        (dictionary) month data in the form of {month_index:"1", month_name:"January"}
        (int) day
    Returns:
        None
    '''

    if min_year:
        if month:
            if day:
                print("Youngest user for {} {}, {} was born in {}".format(month["month_name"], day, year, min_year))
            else:
                print("Youngest user for {}, {} was born in {}".format(month["month_name"], year, min_year))
        else:
            print("Youngest users for {}, was born in {}".format(year, min_year))
    else:
        if month:
            if day:
                print("Youngest user for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Youngest user for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Youngest users for {} could not be calculated".format(year))

    if max_year:
        if month:
            if day:
                print("Oldest user for {} {}, {} was born in {}".format(month["month_name"], day, year, max_year))
            else:
                print("Oldest user for {}, {} was born in {}".format(month["month_name"], year, max_year))
        else:
            print("Oldest users for {}, was born in {}".format(year, max_year))
    else:
        if month:
            if day:
                print("Oldest user for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Oldest user for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Oldest users for {} could not be calculated".format(year))

    if most_popular_year:
        if month:
            if day:
                print("Most popular year of birth for {} {}, {} was {}".format(month["month_name"], day, year, most_popular_year))
            else:
                print("Most popular year of birth for {}, {} was {}".format(month["month_name"], year, most_popular_year))
        else:
            print("Most popular year of birth for {}, was {}".format(year, most_popular_year))
    else:
        if month:
            if day:
                print("Most popular year of birth for {} {}, {} could not be calculated".format(month["month_name"], day, year))
            else:
                print("Most popular year of birth for {}, {} could not be calculated".format(month["month_name"], year))
        else:
            print("Most popular year of birth for {} could not be calculated".format(year))

def render_individual_data(city_data, offset, chunk_size):

    for i in range(chunk_size):

        i += offset
        if i > len(city_data)-1: break

        print('Start Time: {} - End Time: {} - Trip Duration in seconds: {} - Start Station: {} - End Station: {} - User Type: {} - Gender: {} - Year of Birth: {}\n'
            .format(city_data[i]["start_time"], city_data[i]["end_time"], city_data[i]["trip_duration"], city_data[i]["start_station"], city_data[i]["end_station"], city_data[i]["user_type"], city_data[i]["gender"], city_data[i]["birth_year"]))
        i += 1

def render_no_data_available():
    print("\nThere is no more data available\n")

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