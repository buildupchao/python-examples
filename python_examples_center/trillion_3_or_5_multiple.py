import time

"""
Decorator used for calculating the spent time of program
"""


def wrap_the_function(func):
    def cost(*args, **kwargs):
        print("start calculate:")

        start_time = time.time()

        return_value = func(*args, **kwargs)

        end_time = time.time()
        cost_time = end_time - start_time
        print("end calculate: ", cost_time)
        return return_value
    return cost

"""
Firstly, pick up numbers the multiple of 3 or 5 within 10,000,000.
Secondly, calculate the sum of these numbers.
"""


@wrap_the_Function
def multiple_check():
    sum_value = 0
    for num in range(1, 10000000):
        if num % 3 == 0 | num % 5 == 0:
            sum_value += num
    return sum_value

if __name__ == '__main__':
    value = multiple_check()
    print("value is: ", value)