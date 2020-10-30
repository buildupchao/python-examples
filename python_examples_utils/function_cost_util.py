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