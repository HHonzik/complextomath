import math
import random
from json import loads, dumps, load
import sys
import time
i,action,num,complexity,problem_out = 0,0,0,0,0
try: # I really don't like this bad code...
    import pyperclip
except:
    print("Hey, you need to install pyperclip to have the automatic copy feature which can be installed by running in a terminal:\npip install pyperclip\n.")
# --------  Configureables --------
multiplication = False
devision = True
addition = True
subtraction = True
LOG_all_problems = True
auto_copy = True
pause_on_end = 3
try:
    with open("config.json") as f:
        data = load(f)
        multiplication = data.get("multiplication", False)
        devision = data.get("devision", True)
        addition = data.get("addition", True)
        subtraction = data.get("subtraction", True)
        LOG_all_problems = data.get("LOG_all_problems", True)
        auto_copy = data.get("auto_copy", True)
        pause_on_end = data.get("pause_on_end", 3)
except:
    pass
# -------(use config.json)----------
def get_args_and_set_values(): # Getting the args
    global problem_out,num,complexity
    tmp=0
    try:
        try:
            if sys.argv[1].startswith("num="):
                num = int(sys.argv[1][4:])
            elif sys.argv[1].startswith("complexity="):
                complexity = int(sys.argv[1][11:])
        except:
            tmp+=1
            print("No number supplied... Defaulting to 5.")
            num = 5
        try:
            if sys.argv[2].startswith("complexity="):
                complexity = int(sys.argv[2][11:])
            elif sys.argv[2].startswith("num="):
                num = int(sys.argv[2][4:])
            if complexity < 1:
                complexity = 1
        except:
            tmp+=1
            print("No complexity supplied... Defaulting to 250.")
            complexity = 250
            if tmp == 2:
                die.die("Go to supply pls ignore this error :DDDDDDDDD.") # Error out to ask for the user (yes this is actually working so im not gonna touch it beacuse if it works don't fix it)
    except:
        print("No arguments supplied... Asking for input... ")
        num = int(input("Enter a number: "))
        complexity = int(input("Enter a complexity (1-infinity): "))
get_args_and_set_values()
i,action,problem,problem_out=0,0,str(num),num # Variable decleration

def handle_devision_and_multiplication():
    global problem,problem_out,i,action,num,last_operator,problem_out_old,randnum_str,randnum,action
    if problem[-1] == ")":
        problem_last_char = problem[-2]
        offset=2
    else:
        problem_last_char = problem[-1]
        offset=1
    problem_last_num = int(problem_last_char)
    if action == 3 and multiplication == True:
        str_action = "*"
        last_part_new_problem_out = (problem_last_num * randnum)
    else:
        str_action = "/"
        last_part_new_problem_out = (problem_last_num / randnum)
    try: # Just some junk code to handle all of the operations
        if last_operator == 1 and addition == True:
            problem_out = problem_out_old+last_part_new_problem_out
            problem = problem + "+(" + problem_last_char + str_action + randnum_str + ")"
        elif last_operator == 2 and subtraction == True:
            problem_out = problem_out_old-last_part_new_problem_out
            problem = problem + "-(" + problem_last_char + str_action + randnum_str + ")"
        elif last_operator == 3 and multiplication == True:
            problem_out = problem_out_old*last_part_new_problem_out
            problem = problem + "*(" + problem_last_char + str_action + randnum_str + ")"
        elif last_operator == 4: # Yes beacuse this ran, we don't need to check if its enabled
            problem_out = problem_out_old/last_part_new_problem_out
            problem = problem + "/(" + problem_last_char + str_action + randnum_str + ")"
    except ZeroDivisionError:
        if LOG_all_problems:
            print("LOL it did a something / 0 thingy so lets ignore that operation like it didn't happen :DDDDD.")
            i-=1
while True: # Yes this is important too
    problem_out_old = problem_out
    last_operator = action
    i+=1
    if i > complexity:
        for z in range(3):
            lefttocorrect = problem_out - num
            problem = problem + "-" + str(lefttocorrect)
            problem_out = problem_out - lefttocorrect
        break
    action = random.randint(1, 4)
    if random.randint(1,10) > 5:
        action = 4
        if i == 1:
            last_operator = 4
    randnum = int(random.randint(1, complexity))
    if randnum < 1:
        randnum = 1
    randnum_str = str(randnum)
    if action == 1 and addition == True:

        problem = problem + "+" + randnum_str
        problem_out = problem_out + randnum
    elif action == 2 and subtraction == True:
        problem = problem + "-" + randnum_str
        problem_out = problem_out - randnum
    elif action == 3 and multiplication == True:
        handle_devision_and_multiplication()
    elif action == 4 and devision == True:
        handle_devision_and_multiplication()
    else:
        if LOG_all_problems:
            print("No action could have been done in this turn, redoing it and ignoring it...")
        i-=1
    if LOG_all_problems:
        print("Problem: ", problem, ", answer to it:", problem_out)
new_problem = problem.replace(" ", "")
new_problem = new_problem.replace("--", "+")
try:
    if auto_copy == False:
        idontwannacopysoletserroroutnoreasontonot.hey("error")
    pyperclip.copy(new_problem)
    copied = True
except:
    copied = False
if copied:
    del(copied)
    copied = ". Its also coppied to the clipboard."
else:
    del(copied)
    copied = "."
print("Done, heres the math problem: ",new_problem, "which equals", problem_out, copied)
print("Waiting", pause_on_end, "seconds before exiting...")
time.sleep(pause_on_end)