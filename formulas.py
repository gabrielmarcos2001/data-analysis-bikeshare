import dic_utils as utils
import calendar
import datetime

def birth_years(city_data, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''

    # TODO: complete function
    year_count = {}
    min_year = 0
    max_year = 0

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue
        if day != None:
            if data["start_time"].day != day:
                continue

        if not data["birth_year"]:
            continue

        if data["birth_year"] in year_count:
            year_count[data["birth_year"]] += 1
        else:
            year_count[data["birth_year"]] = 1

        if data["birth_year"] > max_year:
            max_year = data["birth_year"]

        if data["birth_year"] < min_year or min_year == 0:
            min_year = data["birth_year"]

    return None if min_year == 0 else min_year, None if max_year == 0 else max_year, utils.get_max(year_count)

def gender(city_data, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    
    # TODO: complete function
    gender_count = {}

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue
        if day != None:
            if data["start_time"].day != day:
                continue

        if data["gender"] in gender_count:
            gender_count[data["gender"]] += 1
        else:
            gender_count[data["gender"]] = 1

    return gender_count

def popular_day(city_data, month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    
    # TODO: complete function
    day_popularity_counter = {}

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue

        if data["start_time"].weekday() in day_popularity_counter:
            day_popularity_counter[data["start_time"].weekday()] += 1
        else:
            day_popularity_counter[data["start_time"].weekday()] = 1

    popular_day_index = utils.get_max(day_popularity_counter)

    if popular_day_index:
        return calendar.day_name[utils.get_max(day_popularity_counter)]
    else:
        return None

def popular_hour(city_data, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''

    # TODO: complete function
    hour_popularity_counter = {}

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue
        if day != None:
            if data["start_time"].day != day:
                continue

        if data["start_time"].hour in hour_popularity_counter:
            hour_popularity_counter[data["start_time"].hour] += 1
        else:
            hour_popularity_counter[data["start_time"].hour] = 1

    return utils.get_max(hour_popularity_counter)

def popular_month(city_data, year):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    months_popularity_counter = {}

    for data in city_data:
        if data["start_time"].month in months_popularity_counter:
            months_popularity_counter[data["start_time"].month] += 1
        else:
            months_popularity_counter[data["start_time"].month] = 1

    return datetime.date(year, utils.get_max(months_popularity_counter), 1).strftime('%B')

def popular_stations(city_data, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''

    # TODO: complete function
    start_station_popularity_counter = {}
    end_station_popularity_counter = {}

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue
        if day != None:
            if data["start_time"].day != day:
                continue

        if data["start_station"] in start_station_popularity_counter:
            start_station_popularity_counter[data["start_station"]] += 1
        else:
            start_station_popularity_counter[data["start_station"]] = 1

        if data["end_station"] in end_station_popularity_counter:
            end_station_popularity_counter[data["end_station"]] += 1
        else:
            end_station_popularity_counter[data["end_station"]] = 1

    return utils.get_max(start_station_popularity_counter), utils.get_max(end_station_popularity_counter)

def popular_trip(city_data, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''

    # TODO: complete function
    most_popular_trip_counter = {}
    stations_dict = {}

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue
        if day != None:
            if data["start_time"].day != day:
                continue

        dict_key = str(hash(data["start_station"] + ";" + data["end_station"]))

        if dict_key in most_popular_trip_counter:
            most_popular_trip_counter[dict_key] += 1
        else:
            most_popular_trip_counter[dict_key] = 1

        stations_dict[dict_key] = {}
        stations_dict[dict_key]["start_station"] = data["start_station"]
        stations_dict[dict_key]["end_station"] = data["end_station"]

    if most_popular_trip_counter:
        max_hash = utils.get_max(most_popular_trip_counter)
        return stations_dict[max_hash]["start_station"], stations_dict[max_hash]["end_station"]
    else:
        return None, None
    

def trip_duration(city_data, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''

    # TODO: complete function
    total_trip_duration_seconds = 0
    average_trip_duration_seconds = 0

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue
        if day != None:
            if data["start_time"].day != day:
                continue

        total_trip_duration_seconds += data["trip_duration"]

    average_trip_duration_seconds = total_trip_duration_seconds // len(city_data)

    return total_trip_duration_seconds, average_trip_duration_seconds

def users(city_data, month, day):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''

    # TODO: complete function
    user_types_count = {}

    for data in city_data:
        if month != None:
            if data["start_time"].month != month["month_index"]:
                continue
        if day != None:
            if data["start_time"].day != day:
                continue

        if data["user_type"] in user_types_count:
            user_types_count[data["user_type"]] += 1
        else:
            user_types_count[data["user_type"]] = 1

    return user_types_count