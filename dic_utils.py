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