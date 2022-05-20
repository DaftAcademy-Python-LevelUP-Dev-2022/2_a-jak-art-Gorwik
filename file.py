from numpy import number


def greeter(func):
    def wrapper(*args):
        names = func(*args)
        return "Aloha " + names.title()
    return wrapper


def sums_of_str_elements_are_equal(func):
    def wrapper(*args):
        numbers = func(*args).split()
        negatives = [True if number[0] == '-' else False for number in numbers]
        
        if negatives[0] ^ negatives[1]:
            return numbers[0] + " != " + numbers[1]
        else:
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
            
            if total_values[0] == total_values[1]:
                return str(total_values[0]) + " == " + str(total_values[1])
            else:
                return str(total_values[0]) + " != " + str(total_values[1])
    return wrapper


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
