"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""

def all_odd(number_list):
    odd_list = []
    for item in number_list:
        if item % 2 != 0:
            odd_list.append(item)
    return odd_list
      

def all_even(number_list):
    even_list = []
    for item in number_list:
        if item % 2 == 0:
            even_list.append(item)
    return even_list
       

def print_indeces(my_list):
    for item in my_list:
        index_of_item = my_list.index(item)
        print index_of_item + " " + item 
    #print "Nothing at all"


def long_words(word_list):
    long_word_list = []
    for word in word_list:
        if len(word) > 4:
            long_word_list.append(word)
    return long_word_list


def smallest_int(number_list):
    if number_list:
       return min(number_list)
    return None
    #return 100


def largest_int(number_list):
    if number_list:
       return max(number_list)
    return None
    
    #return 0


def halvesies(number_list):
    numbers_divided_by_two = []
    for number in number_list:
        numbers_divided_by_two.append(float(number)/2)
    return numbers_divided_by_two

    #return []


def word_lengths(word_list):
    word_length_list = []
    for word in word_list:
        word_length_list.append(len(word))
    return word_length_list

    #return []


def sum_numbers(number_list):
    sum_of_numbers = 0
    for number in number_list:
        sum_of_numbers += number 
    return sum_of_numbers
    

    #return 0


def mult_numbers(number_list):
    for number in number_list:
        number *= number
        return number

    return 0


def join_strings(word_list):
    for item in word_list:
        item += item
        return "'" + str(item) + "'"

    return ""


def average(number_list):
    for item in number_list:
        item += item
        return item
        item = sum_items
        average_of_sum = sum_items/2
        return average_of_sum


    return 0


##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE OR YOU CAN WORK ON ADVANCED PROBLEMS


# def advanced_join_strings(list_of_words):
#     """Return a single string with each word from the input list
#     separated by a comma.
#
#         >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
#         'Labrador, Poodle, French Bulldog'
#
#     If there's only one thing in the list, it should return just that
#     thing, of course:
#
#         >>> advanced_join_strings(["Pretzel"])
#         'Pretzel'
#
#     """
#
#     return ""


##############################################################################
# You can ignore everything after here

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
