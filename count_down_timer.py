from datetime import timedelta
import time

def countdown(user_time):
   while user_time >= 0:
        print(str(timedelta(seconds=user_time)), end='\r')
        time.sleep(1)
        user_time -= 1
   print('Lift off!')


if __name__ == '__main__':
   user_time = int(input("Enter a time in seconds: "))
   countdown(user_time)