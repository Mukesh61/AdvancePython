import random
import time
GROUP_MEMBERS = [
    "Person 1",
    "Person 2",
    "Person 3",
    "Person 4",
    "Person 5",
    "Person 6",
    "Person 7",
    "Person 8",
    "Person 9",
    "Person 10"]

breakp = 0

group_div = []
current_team = 0
success_flag = True

def final_print(group_div):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Final LIst %%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    current_team = 0
    for item in group_div:
        print("Member of Team ", current_team + 1)
        for member in item:
            print('              ',member)
            current_team += 1

print("Total number of players :", len(GROUP_MEMBERS))

while(True):
    try:
        no_of_group = int(input("How many groups do you want to create: "))
        break
    except:
        print("Please enter a number")

while(len(GROUP_MEMBERS) > 0):
    choice_by_python = random.randint(0,len(GROUP_MEMBERS)-1)
    print("Selection in progress for group " + str(current_team + 1), end = '')
    time.sleep(1)
    print(".",end='')
    time.sleep(1)
    print(".",end='')
    time.sleep(1)
    print(".",end='')
    time.sleep(1)
    print(".",end='')
    player = GROUP_MEMBERS[choice_by_python]
    del GROUP_MEMBERS[choice_by_python]
    print(player)

    try:
        group_div[current_team].append(player)
    except:
        group_div.append([player])

    current_team += 1

    try:
        current_team %= no_of_group

    except:
        print("Group cannot be created with 0")
        success_flag = False
        break

print()
if success_flag:
    final_print(group_div)
