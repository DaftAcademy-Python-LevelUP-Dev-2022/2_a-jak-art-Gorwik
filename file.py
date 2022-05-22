def greeter(func):
    def wrapper(*args):
        names = func(*args)
        return "Aloha " + names.title()
    return wrapper

def sums_of_str_elements_are_equal(func):
    def wrapper(*args):
        numbers = func(*args).split()
        negatives = [True if number[0] == '-' else False for number in numbers]
        
        numbers_to_char, total_values = [], []
        temp_sum = 0

        for index, number in enumerate(numbers):
            temp_list_of_chars = [char for char in number]
            if negatives[index]:
                temp_list_of_chars.pop(0)
            numbers_to_char.append(temp_list_of_chars)

        for number_of_chars in numbers_to_char:
            for char in number_of_chars:
                temp_sum += int(char)
            else:
                total_values.append(temp_sum)
                temp_sum = 0

        for index, negative in enumerate(negatives):
                if negative:
                    total_values[index] *= -1

        if total_values[0] == total_values[1]:
            return f"{total_values[0]} == {total_values[1]}"
        else:
            return f"{total_values[0]} != {total_values[1]}"
    return wrapper

def format_output(*required_keys):
    new_dict = {}
    REQUIRED_KEYS = []
    for required_key in required_keys:
        new_dict[required_key] = False
        if "__" in required_key:
            required_key = required_key.split("__")
            for list_key in required_key:
              REQUIRED_KEYS.append(list_key)
        else:
            REQUIRED_KEYS.append(required_key)
    def wrapper_outer(func):
        def wrapper_inner(*args):
            nonlocal new_dict
            dict_of_parameters = func(*args)

            for key in REQUIRED_KEYS:
                if not key in dict_of_parameters.keys():
                    raise ValueError

            for required_key in new_dict.keys():
                for key, value in dict_of_parameters.items():
                    if key in required_key:
                        if not new_dict[required_key]:
                            if not value:
                                new_dict[required_key] = "Empty value"
                            else:    
                                if f"_{key}_" in required_key:
                                    new_dict[required_key] = new_dict[required_key] = " " + value + " "
                                elif f"{key}_" in required_key:
                                    new_dict[required_key] = value + " "
                                elif f"_{key}" in required_key:
                                    new_dict[required_key] = " " + value
                                else:
                                    new_dict[required_key] = value
                        else:
                            if f"_{key}_" in required_key:
                                new_dict[required_key] = new_dict[required_key].replace(' ', f' {value} ')
                            elif f"{key}_" in required_key:
                                new_dict[required_key] = value + new_dict[required_key]
                            else:
                                new_dict[required_key] = new_dict[required_key] + value
                                
            return new_dict
        return wrapper_inner
    return wrapper_outer
        
def add_method_to_instance(klass):
    def decorator(func):
        def inner_decorator(*args, **kwargs):
            return func()

        setattr(klass, func.__name__, inner_decorator)
        return inner_decorator
        
    return decorator
