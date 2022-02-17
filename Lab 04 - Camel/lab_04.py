import random

print("Welcome to Camel!")
print("""You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.""")
print()

#variables
milesTraveled = 0
thirst = 0
camelFatigue = 0
nativesTraveled = -20
canteen = 3
done = False

#start main loop
while not done:
    nativesBehind = milesTraveled - nativesTraveled
    fullSpeed = random.randrange(10, 21)
    moderateSpeed = random.randrange(5, 13)
    print("""
    A. Drink from your canteen.
    B. Ahead at moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check
    Q. Quit.""")
    print()
    userInput = input("Your choice? ")
    if userInput.lower() == "q":
            done = True

#status
    elif userInput.lower() == "e":
        print("Miles traveled: ",milesTraveled)
        print("Drinks in canteen: ",canteen)
        print("Your camel has ",camelFatigue,"amount of fatigue.")
        print("The natives are ",nativesBehind,"miles behind you.")
#stop for night
    elif userInput.lower() == "d":
        camelFatigue *= 0
        print("Your camel feels refreshed and happy his fatigue is now ",camelFatigue)
        nativesTraveled += random.randrange(7, 15)
#move full speed
    elif userInput.lower() == "c":
        print("You traveled ",fullSpeed,"miles!")
        milesTraveled += fullSpeed
        thirst += 1
        camelFatigue += random.randrange(1, 4)
        nativesTraveled += random.randrange(7, 15)
        oasis = random.randrange(1, 21)

#move moderate speed
    elif userInput.lower() == "b":
        print("You traveled ",moderateSpeed,"miles!")
        milesTraveled += moderateSpeed
        thirst += 1
        camelFatigue += 1
        nativesTraveled += random.randrange(7, 15)
        oasis = random.randrange(1, 21)

        #drink canteen
    elif userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have ",canteen,"drinks left and you are no longer thirsty.")

#not done check
    if oasis == 20:
        camelFatigue *= 0
        thirst *= 0
        canteen = 3
        print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")
    if nativesBehind <= 15:
        print("The natives are drawing near!")
    if milesTraveled >= 200 and not done:
        print("You made it across the desert, you win!")
        done = True
    if nativesTraveled >= milesTraveled:
        print("The natives caught and beheaded you.")
        print("You're dead!")
        done = True
    if thirst > 4 and thirst <= 6 and not done:
        print("You are thirsty")
    if thirst > 6:
        print("You died of dehydration!")
        done = True
    if camelFatigue > 5 and camelFatigue <= 8 and not done:
        print("Your camel is getting tired.")
    if camelFatigue > 8:
        print("Your camel is dead.")
        done = True