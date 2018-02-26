
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