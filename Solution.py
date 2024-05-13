from time import time 
import random as r
def mistake(paragraph,user_input):
        error=0
        for i in range(len(paragraph)):
                try:
                   if paragraph[i] != user_input[i]:
                           error += 1
                except IndexError:
                   error += 1
        return error
def speed_time(time_s,time_e,user_input):
        time_delay = time_e - time_s
        time_R = round(time_delay,2)
        speed = len(user_input) / time_R
        return round(speed)
while True:
        choice = input("Are you ready for typing speed test?(y/n)\n")
        if choice == 'y' or choice == 'Y': 
                test = ["The sun peeked through the clouds, casting a warm glow over the meadow.",
                        "Sarah hurried down the street, clutching her umbrella as the rain began to fall.",
                        "The old house at the end of the lane looked haunted, its windows boarded up and ivy creeping up the walls.",
                        "The smell of freshly baked bread wafted through the air, making everyone's mouths water.",
                        "As the train pulled into the station, James felt a surge of excitement for his upcoming adventure."]
                test1 = r.choice(test)
                print("      _____Typing Speed Test_____")
                print()
                print(test1)
                print()
                print()
                t1 = time()
                user_input = (input("Type the above sentence: "))
                t2 = time()
                print("Your typing speed is: ",speed_time(t1,t2,user_input),"w/sec")
                print("Number of errors: ",mistake(test1,user_input))
        elif choice == 'n' or choice == "N":
                print("Thank you using our typing speed calculator.")
                break
        else:
                print("Invaild input")
