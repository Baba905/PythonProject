import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def calcul_time():
      start_time = time.time()
      function()
      end_time  =time.time()
      print(f" {function.__name__} Run speed :{end_time-start_time}")
    return calcul_time

print("start")

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
# result = speed_calc_decorator(slow_function)
# test =result()
# print(test)