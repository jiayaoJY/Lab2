def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    # Read user input from console
    user_input = input()

    # Split the string by commas into a list of strings
    string_list = user_input.split(",")

    # Convert list of strings to list of floats
    float_list = []
    for num_str in string_list:
        float_list.append(float(num_str))

    return float_list

def calc_average_temperature(num_list):
    # Calculate sum of all numbers
    total = sum(num_list)

    # Calculate average
    average = total / len(num_list)

    return average

def calc_min_max_temperature(num_list):
    # Find minimum value
    minimum = min(num_list)

    # Find maximum value
    maximum = max(num_list)

    # Return as a list [min, max]
    return [minimum, maximum]

def sort_temperature(num_list):
    # Sort the list in ascending order
    sorted_list = sorted(num_list)
    return sorted_list

def calc_median_temperature(num_list):
    # First, sort the list
    sorted_list = sort_temperature(num_list)

    # Get the length of the list
    length = len(sorted_list)

    # Calculate median
    if length % 2 == 0:
        # Even number of elements: average of two middle values
        mid1 = length // 2 - 1
        mid2 = length // 2
        median = (sorted_list[mid1] + sorted_list[mid2]) / 2
    else:
        # Odd number of elements: middle value
        mid = length // 2
        median = sorted_list[mid]

    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    # Calculate and display average
    average = calc_average_temperature(num_list)
    print("Average temperature: " + str(average))

    # Calculate and display min and max
    min_max = calc_min_max_temperature(num_list)
    print("Minimum temperature: " + str(min_max[0]))
    print("Maximum temperature: " + str(min_max[1]))

    # Calculate and display median
    median = calc_median_temperature(num_list)
    print("Median temperature: " + str(median))

if __name__ == "__main__":
    main()