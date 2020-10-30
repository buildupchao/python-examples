from python_examples_utils import function_cost_util

@function_cost_util
def calculate_total_of_5_multiple():
    sum = 0
    for i in range(1, 100000):
        if i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    sum = calculate_total_of_5_multiple()
    print(sum)