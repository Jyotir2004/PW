import time


def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        print(start_time)
        result=func(*args,**kwargs)
        end_time=time.time()-start_time
        print(end_time)
        print("procss time",end_time-start_time)
        return result
    return wrapper


@timer
def greet():
    print("good moring")

greet()







