"""Created by Joshua Ye and Bryan Kikuta
June 1, 2018 """

"""This is a choose your adventure where you are stuck in a rainforest. You need to safety. You have inventory where you
choose an item to take with you. You need to stay alive without dying or losing all your energy."""


#Defining Game
def game():
    import time
    import random
    #Pre-game 
    play=['yes','no']
    startGame=input("Do you want to start the game? (yes/no): ")
    while startGame not in play:
        startGame=input("Do you want to start the game? (yes/no): ")
    print('')
    while startGame=="yes":
        
        #Instructions
        print("This is a choose your own adventure game. You will need to type in commands to \
progress further in the game. All commands are to be inputed after storyline text is given. \
When '>' appears, it is a sign to input your command. All comands are to be typed in lowercase. \
In addition, please be mindful to not put any unecessary spaces in your command. \
There are many routes to take, and there will be many commands that the program will not \
understand. It is encouraged to keep on trying commands to trigger moving forward in the game. \
Energy is printed every time you input a valid command to help you keep track of how much energy you have left. \
It is recommened to start with level 1 since level 2 is more difficult. Have fun!")
        print('')
        
    #Starting the Game
        gameMode=input("Select game level (1/2): ")
        print("")
        while gameMode=="1":
            #Energy Counter
            energy=50
            time.sleep(0.5)
            #Instroduction of Story
            print("It is 13:00, you are racing down an abandoned dirt path at high speeds \
in a jungle, suddenly you hit a rock that jolts you into the side of the car. \
The impact severely damages your suspension sending you veering out of control \
until your car collides into a tree and your world goes blank.")
            print(" ")
            time.sleep(3)

            print("You wake up lying on the ground beside your scorched car, your head is throbbing with every pulse of blood spurting out")
            print(" ")
            time.sleep(1)
            print("You focus hard and study your surroundings, you notice some items were ejected out of the car after the impact before they burned to ashes")
            print(" ")
            time.sleep(1)
            print("Due to your current state, you are too weak to carry more than one object, you must pick up an object and evacuate the area before the car blows leaving you dead")
            print(" ")
            time.sleep(1)
            #Choosing your inventory
            objects=["BLANKET","LIFE JACKET"]
            print("The objects are a BLANKET and a LIFE JACKET")
            time.sleep(0.5)
            print("Select the item that you desire to carry along with you: ")
            time.sleep(0.2)
            item=input(">")
            while item not in s10:
                print("I don't understand")
                print("Select the item that you desire to carry along with you: ")
                time.sleep(0.2)
                item=input(">")
            inventory=[]
            inventory.append(item)
            
    #Game Begins

            print("You look around yourself. A flowing RIVER and a massive palm TREE surround you. \
    Before you realize, a small MONKEY appears. The thirst of survival begins now.")

            #Tree Route
            monkeyCount=0
            time.sleep(0.2)
            command=input('>')
            while command not in a1:
                print("I don't understand")
                time.sleep(0.2)
                command=input('>')
            for i in range(10):
                while command in s3:
                    energy=energy-5
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    print("You are now beside the tree")
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a2:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')
                    counter=1
                    counter1=1
                    for i in range(3):
                        #Shaking the Tree
                        while command in s4:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                print(" ")
                                game()
                            print("energy =",energy)
                            if counter>=3:
                                print("A coconut fell on your head")
                                print("YOU DIED")
                                ##########################
                                time.sleep(1)
                                print(" ")
                                game()
                            print("A coconut falls from the tree beside you, and you eat it")
                            energy=energy+10
                            print("energy =",energy)
                            counter=counter+1
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a2:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                        #Climbing the Tree
                        while command in s5:
                            energy=energy-8
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            if counter1>=3:
                                print("You died, the tree collapsed under your weight")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            print("You climb the tree and see smoke from across the river, then you climb down")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a2:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                                

                #Monkey Route
                while command in s2:
                    energy=energy-5
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    while command in s2 and monkeyCount>=1:
                        print("The monkey has left, select another command.")
                        time.sleep(0.2)
                        command=input('>')
                        while command in a5:
                            print("The monkey has left, select another command not related to the monkey.")
                            time.sleep(0.2)
                            command=input('>')
                        while command not in a16:
                            print("The monkey has left, select another command not related to the monkey.")
                            time.sleep(0.2)
                            command=input('>')
                    while command in s2 and monkeyCount<1:
                        print("The monkey is now right in front of you")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a3:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                        #Petting the Monkey
                        if command in s6:
                            print("The monkey appears to enjoy being pet, after it leaves it gives you a banana, and you eat it")
                            energy=energy+15
                            print("energy =",energy)
                            monkeyCount=monkeyCount+1
                            time.sleep(0.2)
                            command=input('>')
                            while command in a5:
                                print("The monkey has left, select another command")
                                time.sleep(0.2)
                                command=input('>')
                            while command not in a4:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                        #DEATH from Attacking the Monkey
                        elif command in s7:
                            print("The monkey runs off only to come back with a gang of apes that devours you")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()

                            
            #River Route
            while command in s1:
                energy=energy-5
                if energy <= 0:
                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                    time.sleep(1)
                    print(" ")
                    game()
                print("energy =",energy)
                print("The river rushes in front of you")
                time.sleep(0.2)
                command=input('>')
                while command in a13:
                    print("A water dam breaks sending water rushing at high speeds, it is not possible to return back.")
                    time.sleep(0.2)
                    command=input('>')
                while command not in a6:
                    print("I don't understand")
                    time.sleep(0.2)
                    command=input('>')
                waterCounter=0
                for i in range(10):
                    #Drinking the Water
                    while command in s9:
                        energy=energy-10
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        if waterCounter>=2:
                            print("You get really sick from the water and die")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()
                        print("You drink the water and puke")
                        waterCounter=waterCounter+1
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a10:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                    #Fishing
                    counter=1
                    while command in s21:
                        print("You decide to go near the shore of the river to grab fish with your bear hands. Caveman style.")
                        fish=random.randint(1,3)
                        if counter>2:
                            print("A shark jumps up and eats you whole. Ouch, indeed.")
                            print("YOU DIED")
                            print('')
                            game()
                        if 2==fish:
                            print("energy =",energy)
                            print("Bingo! You caught a surgeonfish. It was a simple operation, right?!")
                            energy=energy+10
                            print("energy =",energy)
                            counter=counter+1
                            command=input('>')
                        elif 2!=fish:
                            print("energy =",energy)
                            print("Not even a nibble...")
                            energy=energy-1
                            print("energy =",energy)
                            counter=counter+1
                            command=input('>')
                        while command not in a6:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                    #Successfully Swimming Across the River
                    if command in s8 and energy>=46 or "life jacket" in inventory:
                        print("You make it to the other side and lay on the shore")
                        print("You lie on the shore bank exhausted from your swim, you are hungry and tired")
                        time.sleep(1)
                        print("You see a CAVE nearby and a BUSH filled with berries")
                        energy=energy-18
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a7:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')

                            
                        #Cave Route
                        if command in s12:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            print("You run into the dark cave and before you know it a bear is looming over you staring into your eyes")
                            time.sleep(0.5)
                            print("You remember someone mentioned before to you that bears do not attack if you play dead")
                            print("Natural instinct though wants you to run")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a11:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #Successful Bear Encounter
                            if command in s13 and energy>=35:
                                print("You sprint to the road and see a group of fellow bear hunters")
                                time.sleep(0.5)
                                print("The bear hunters kill the bear for you, and you are saved")
                                print("They take you to their home, and you happily eat bear together.")
                                print("YOU ARE SAVED")
                                time.sleep(1)
                                print("You scored:",energy)
                                time.sleep(1)
                                ########################
                                print(" ")
                                game()
                            #DEATH from Running from the Bear
                            elif command in s13:
                                print("Due to your tired state,you try run like a drunk maniac only to collapse and be devoured by the bear, you did make a great meal though")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            #Playing DEAD from the Bear
                            elif command in s14:
                                print("Unfortunately the playing dead was for a different bear species, the bear walks up to you and you feel your arteries in your neck rip with your spine as it gruesomely decapitates you")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()

                                
                        #Berry Bush Route
                        elif command in s15:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            print("You walk to the bush with berries, they are of a darker purple colour")
                            print("You are extremely hungry, though you want to scout the area and look for something else")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a8:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #Eating Berries
                            if command in s16:
                                print("You start to feel more energized and stronger")
                                energy=energy+15
                                print("energy =",energy)
                                print("You can now look around, but you feel somewhat tired.")
                                print("Maybe sleeping would be nice.")
                                time.sleep(0.2)
                                command=input('>')
                                while command not in a9:
                                    print("I don't understand")
                                    time.sleep(0.2)
                                    command=input('>')
                                #Successfully Sleeping after Eating Berries
                                if command in s17 and "blanket" in inventory:
                                    print("You use your blanket for a nap, and it keeps your body warm and refreshed.")
                                    energy=energy+4
                                    print("energy =",energy)
                                    time.sleep(0.2)
                                    command=input('>')
                                    while command not in s18:
                                        print("I don't understand")
                                        time.sleep(0.2)
                                        command=input('>')

                                        
                                    #Car Arrives
                                    if command in s18:
                                        energy=energy-5
                                        if energy <= 0:
                                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                                            time.sleep(1)
                                            print(" ")
                                            game()
                                        print("energy =",energy)
                                        print("Fighting your body you walk around looking for help")
                                        print("You see a jeep driving through the forest")
                                        time.sleep(1)
                                        print("Your last minute thinking tells you to run infront and wave your arms")
                                        print("Or yell at the driver to stop")
                                        time.sleep(0.2)
                                        command=input('>')
                                        while command not in a12:
                                            print("I don't understand")
                                            time.sleep(0.2)
                                            command=input('>')
                                        #DEATH from Running in Front of the Car
                                        if command in s19:
                                            print("The driver just happened to be on his phone playing crossy roads, how ironic")
                                            print("He does not see you and runs you over-you die from severe brain trauma")
                                            print("YOU DIED")
                                            ########################
                                            time.sleep(1)
                                            print(" ")
                                            game()
                                        #Yelling to the Car and Getting SAVED
                                        elif command in s20:
                                            print("Using every last bit of energy, you yell at the driver to stop")
                                            print("He pulls over to take you in")
                                            print("YOU ARE SAVED")
                                            time.sleep(1)
                                            print("You scored:",energy)
                                            time.sleep(1)
                                            print(" ")
                                            game()
                                #DEATH from Sleeping 
                                elif command in s17:
                                    print("After 5 minutes of sleeping you wake up to an excruciating pain and jolt in spasms until you reach your death")
                                    print("YOU DIED")
                                    ########################
                                    time.sleep(1)
                                    print(" ")
                                    game()
                                #DEATH from Eating Berries and Scouting
                                elif command in s18:
                                    print("In your sudden rush of joy from finding food, you start to look around")
                                    print("You see the smoke from a potential village, you run towards it")
                                    print("Out of the blue, you collapse and your body goes completely numb")
                                    time.sleep(2)
                                    print("You die from the berries poisoning you")
                                    print("YOU DIED")
                                    ########################
                                    time.sleep(1)
                                    print(" ")
                                    game()
                            elif command in s18:
                                energy=energy-5
                                if energy <= 0:
                                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                                    time.sleep(1)
                                    print(" ")
                                    game()
                                print("energy =",energy)
                                print("Fighting your body you walk around looking for help")
                                print("You see a jeep driving through the forest")
                                time.sleep(1)
                                print("Your last minute thinking tells you to run in front and wave your arms")
                                print("Or yell at the driver to stop")
                                command=input('>')
                                while command not in a12:
                                    print("I don't understand")
                                    time.sleep(0.2)
                                    command=input('>')
                                #DEATH from Running in Front of the Car
                                if command in s19:
                                    print("The driver just happened to be on his phone playing crossy roads, how ironic")
                                    print("He does not see you and runs you over-you die from severe brain trauma")
                                    print("YOU DIED")
                                    ########################
                                    time.sleep(1)
                                    print(" ")
                                    game()
                                #Yelling to the Car and Getting SAVED
                                elif command in s20:
                                    print("Using every last bit of energy, you yell at the driver to stop")
                                    print("He pulls over to take you in")
                                    time.sleep(0.5)
                                    print("YOU ARE SAVED")
                                    time.sleep(1)
                                    print("You scored:",energy)
                                    time.sleep(1)
                                    print(" ")
                                    game()
                    #Swimming across the River with not Enough Energy
                    elif command in s8 and energy<46:
                        print("You start your crawl across the river, but out of fatigue, you get tired and drown")
                        print("YOU DIED")
                        ########################
                        time.sleep(1)
                        print(" ")
                        game()




                        
    #Game level 2
                        
        while gameMode=="2":
            #Energy Counter
            energy=40
            time.sleep(0.5)
            #Instroduction of Story
            print("It is 13:00, you are racing down an abandoned dirt path at high speeds \
    in a jungle, suddenly you hit a rock that jolts you into the side of the car. \
    The impact severely damages your suspension sending you veering out of control \
    until your car collides into a tree and your world goes blank.")
            print(" ")
            time.sleep(3)

            print("You wake up lying on the ground beside your scorched car, your head is throbbing with every pulse of blood spurting out")
            print(" ")
            time.sleep(1)
            print("You focus hard and study your surroundings only to see your car is engulfed in massive flames upside down")
            print(" ")
            time.sleep(1)
            print("You must leave the area soon before the car explodes completely!")
            print(" ")
            time.sleep(1)
                    
    #Game Begins
            
            #Explosion Scene
            print("You must take cover, you glance and see a TREE, BUSH, and BOULDERS, though you are in shock and cannot makeout much, which way do you run?")
            print("You can go EAST, WEST, or SOUTH, while you car is NORTH")
            time.sleep(0.2)
            command=input('>')
            while command not in directions:
                print("I don't understand")
                time.sleep(0.2)
                command=input('>')
            if command in east:
                print("You run towards a tree and hide")
                time.sleep(2)
                print("KABOOM!!!!")
                print("The car sends shrapnel flying everywhere, some pierce through the tree and puncture your body")
                energy=energy-30
                print("Energy Level Critical! Energy =",energy)
                time.sleep(0.5)
                #Survival Booklet Scene
                print("You quickly open your survival booklet and it has first aid measures, what chapter do you follow (1-3)?")
                time.sleep(0.2)
                command=input('>')
                while command not in numbers:
                    print("I don't understand")
                    time.sleep(0.2)
                    command=input('>')
                chapter=random.randint(1,3)
                if command==str(chapter):
                    print("Luckily you followed the right instructions and saved yourself")
                    energy=energy+26
                    print("energy =",energy)
                elif command != str(chapter):
                    print("WRONG CHAPTER!!, you start to bleed yourself out, too tired you cant do anything")
                    while energy>0:
                        print("Energy =",energy)
                        energy=energy-1
                        time.sleep(0.5)
                    print("YOU DIED")
                    time.sleep(1)
                    print(" ")
                    game()
            elif command in south:
                print("You find a large boulder and hide")
                print("You survive the blow thanks to the giant rock")
            elif command in west:
                print("A bush? OH NO, WRONG WAY!!! you thi...")
                time.sleep(1)
                print("KAABBBOOOMMM!!!!!")
                time.sleep(1)
                print("A shredded cylinder from a 3.6L Pentastar V6 Engine tears straight through your chest, RIP")
                print("YOU DIED")
                time.sleep(1)
                print(" ")
                game()
            elif command in north:
                print("Eh, whatever I think i forgot something in the ca...")
                time.sleep(0.9)
                print("A big flash meets you as you walk towards the car, The End.")
                time.sleep(0.5)
                print("YOU DIED")
                time.sleep(1)
                print(" ")
                game()
            time.sleep(0.5)
            print("You look around yourself. A flowing RIVER and a massive palm TREE surround you. \
    Before you realize, a small MONKEY appears. The thirst of survival begins now.")


            #Tree Route
            monkeyCount=0
            time.sleep(0.2)
            command=input('>')
            while command not in a1:
                print("I don't understand")
                time.sleep(0.2)
                command=input('>')
            for i in range(10):
                while command in s3:
                    energy=energy-5
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    print("You are now beside the tree")
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a2:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')
                    counter=1
                    counter1=1
                    for i in range(3):
                        #Shaking the Tree
                        while command in s4:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            if counter>=3:
                                print("A coconut fell on your head")
                                print("YOU DIED")
                                ##########################
                                time.sleep(1)
                                print(" ")
                                game()

                            print("A coconut falls from the tree beside you, and you eat it")
                            energy=energy+10
                            print("energy =",energy)
                            counter=counter+1
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a2:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                        #Climbing the Tree
                        while command in s5:
                            energy=energy-8
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            if counter1>=3:
                                print("You died, the tree collapsed under your weight")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            print("You climb the tree and see smoke from across the river, then you climb down")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a2:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')


                #Monkey Route
                while command in s2:
                    energy=energy-5
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    while command in s2 and monkeyCount>=1:
                        print("The monkey has left, select another command.")
                        time.sleep(0.2)
                        command=input('>')
                        while command in a5:
                            print("The monkey has left, select another command not related to the monkey.")
                            time.sleep(0.2)
                            command=input('>')
                        while command not in a16:
                            print("The monkey has left, select another command not related to the monkey.")
                            time.sleep(0.2)
                            commadn=input('>')
                    while command in s2 and monkeyCount<1:
                        print("The monkey is now right in front of you")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a3:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                        #Petting the Monkey
                        if command in s6:
                            print("The monkey appears to enjoy being pet, after it leaves it gives you a banana, and you eat it")
                            energy=energy+15
                            print("energy =",energy)
                            monkeyCount=monkeyCount+1
                            time.sleep(0.2)
                            command=input('>')
                            while command in a5:
                                print("The monkey has left, select another command")
                                time.sleep(0.2)
                                command=input('>')
                            while command not in a4:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                        #DEATH from Attacking the Monkey
                        elif command in s7:
                            print("The monkey runs off only to come back with a gang of apes that devours you")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()


            #River Route
            while command in s1:
                energy=energy-5
                if energy <= 0:
                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                    time.sleep(1)
                    print(" ")
                    game()
                print("energy =",energy)
                print("The river rushes in front of you")
                time.sleep(0.2)
                command=input('>')
                while command in a13:
                    print("A water dam breaks sending water rushing at high speeds, it is not possible to return back.")
                    time.sleep(0.2)
                    command=input('>')
                while command not in a6:
                    print("I don't understand")
                    time.sleep(0.2)
                    command=input('>')
                waterCounter=0
                for i in range(10):
                    #Drinking the Water
                    while command in s9:
                        energy=energy-10
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        if waterCounter>=2:
                            print("You get really sick from the water")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()
                        print("You drink the water and puke")
                        waterCounter=waterCounter+1
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a10:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                    #Fishing
                    counter=1
                    while command in s21:
                        print("You decide to go near the shore of the river to grab fish with your bear hands. Caveman style.")
                        fish=random.randint(1,3)
                        if counter>2:
                            print("A shark jumps up and eats you whole. Ouch, indeed.")
                            print("YOU DIED")
                            print('')
                            game()
                        if 2==fish:
                            print("energy =",energy)
                            print("Bingo! You caught a surgeonfish. It was a simple operation, right?!")
                            energy=energy+10
                            print("energy =",energy)
                            counter=counter+1
                            command=input('>')
                        elif 2!=fish:
                            print("energy =",energy)
                            print("Not even a nibble...")
                            energy=energy-1
                            print("energy =",energy)
                            counter=counter+1
                            command=input('>')
                        while command not in a6:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')  
                    #Successfully Swimming Across the River
                    if command in s8 and energy>=46:
                        print("You make it to the other side and lay on the shore")
                        print("You lie on the shore bank exhausted from your swim, you are hungry and tired")
                        energy=energy-18
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        time.sleep(1)
                        
                        #Fire Scene
                        print("You decide it's best to make a fire to warm up, and to your luck you have a pocket lighter")
                        print("You can build a fire on the shoreline, forest, rocks")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in fires:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                        if command in shore:
                            print("You set up your fire on the shore")
                            time.sleep(1)
                            print("Shortly after rough waters hit high and put out your fire")
                            time.sleep(0.3)
                            print("You warmed up slightly but are still cold")
                            energy=energy+5
                            print("energy =",energy)
                        elif command in forest:
                            print("A genius idea sparks in your head")
                            print("You gather some sticks and light your fire")
                            time.sleep(2)
                            print("-NEWS HEADLINE-")
                            print("Lost man sets forest on fire, 1 casualty")
                            print("YOU DIED")
                            print(" ")
                            game()
                        elif command in rocks:
                            print("You set up a nice fire on the rocks, you warm up and are ready to cotinue")
                            energy=energy+12
                            print("energy =",energy)
                        print("You see a CAVE nearby and a BUSH filled with berries")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a7:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')

                            
                        #Cave Route
                        if command in s12:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            print("You run into the dark cave and before you know it a bear is looming over you staring into your eyes")
                            time.sleep(0.5)
                            print("You remember someone mentioned before to you that bears do not attack if you play dead")
                            print("Natural instinct though wants you to run")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a11:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #Successful Bear Encounter
                            if command in s13 and energy>=35:
                                print("You sprint to the road and see a group of fellow bear hunters")
                                time.sleep(0.3)
                                print("The bear hunters kill the bear for you, and you are saved")
                                print("They take you to their home, and you happily eat bear together.")
                                print("YOU ARE SAVED")
                                ########################
                                time.sleep(1)
                                print("You scored:",energy)
                                time.sleep(1)
                                print(" ")
                                game()
                            #DEATH from Running from the Bear
                            elif command in s13:
                                print("Due to your tired state,you try run like a drunk maniac only to collapse and be devoured by the bear, you did make a great meal though")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            #Playing DEAD from the Bear
                            elif command in s14:
                                print("Unfortunately the playing dead was for a different bear species, the bear walks up to you and you feel your arteries in your neck rip with your spine as it gruesomely decapitates you")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()

                                
                        #Berry Bush Route
                        elif command in s15:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            print("You walk to the bush with berries, they are of a darker purple colour")
                            print("You are extremely hungry, though you want to scout the area and look for something else")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a8:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #Eating Berries
                            if command in s16:
                                print("You start to feel more energized and stronger")
                                energy=energy+15
                                print("energy =",energy)
                                print("You can now look around, but you feel somewhat tired.")
                                time.sleep(0.2)
                                print("Maybe sleeping would be nice.")
                                time.sleep(0.2)
                                command=input('>')
                                while command not in a9:
                                    print("I don't understand")
                                    time.sleep(0.2)
                                    command=input('>')
                                #DEATH from Sleeping 
                                if command in s17:
                                    print("After 5 minutes of sleeping you wake up to an excruciating pain and jolt in spasms until you reach your death")
                                    print("YOU DIED")
                                    ########################
                                    time.sleep(1)
                                    print(" ")
                                    game()
                                #DEATH from Eating Berries and Scouting
                                elif command in s18:
                                    print("In your sudden rush of joy from finding food, you start to look around")
                                    print("You see the smoke from a potential village, you run towards it")
                                    print("Out of the blue, you collapse and your body goes completely numb")
                                    time.sleep(2)
                                    print("You die from the berries poisoning you")
                                    print("YOU DIED")
                                    ########################
                                    time.sleep(1)
                                    print(" ")
                                    game()


                            #Car Arrives
                            elif command in s18:
                                energy=energy-5
                                if energy <= 0:
                                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                                    time.sleep(1)
                                    print(" ")
                                    game()
                                print("energy =",energy)
                                print("Fighting your body you walk around looking for help")
                                print("You see a jeep driving through the forest")
                                time.sleep(0.5)
                                print("Your last minute thinking tells you to run in front and wave your arms")
                                print("Or yell at the driver to stop")
                                time.sleep(0.2)
                                command=input('>')
                                while command not in a12:
                                    print("I don't understand")
                                    time.sleep(0.2)
                                    command=input('>')
                                #DEATH from Running in Front of the Car
                                if command in s19:
                                    print("The driver just happened to be on his phone playing crossy roads, how ironic")
                                    print("He does not see you and runs you over, you die from severe brain trauma")
                                    print("YOU DIED")
                                    ########################
                                    time.sleep(1)
                                    print(" ")
                                    game()
                                #Yelling to the Car and Getting SAVED
                                elif command in s20:
                                    print("Using every last bit of energy, you yell at the driver to stop")
                                    time.sleep(0.2)
                                    print("He pulls over to take you in")
                                    print("YOU ARE SAVED")
                                    time.sleep(1)
                                    print("You scored:",energy)
                                    time.sleep(1)
                                    print(" ")
                                    game()
                    #Swimming across the River with not Enough Energy
                    elif command in s8 and energy<46:
                        print("You start your crawl across the river, but out of fatigue, you get tired and drown")
                        print("YOU DIED")
                        ########################
                        time.sleep(1)
                        print(" ")
                        game()

                        

    while startGame =="no":
        raise SystemExit




    
#End of Defining




    
#List of Commands
    
s1=["go to river","river","go river","walk to river", "move to river","walk to the river","move to the river","go to the river"]
s2=["go to monkey","monkey","go monkey","walk to monkey","move to monkey","walk to the monkey","move to the monkey","go to the monkey"]
s3=["go to tree","tree","go tree","walk to tree","move to tree","walk to the tree","move to the tree","go to the tree"]
s4=["shake tree","shake the tree","hit the tree","shake","kick","kick tree"]
s5=["climb tree","climb up","climb"]
s6=["pet monkey","pat monkey","monkey pet","pet"]
s7=["attack monkey","kill monkey","attack","hurt","hurt monkey","attack","eat","eat monkey","kill"]
s8=["swim across river","swim","swim over","swim over river","swim over the river","swim across the river","cross river"]
s9=["drink water","drink","sip","sip water"]
s10=["life jacket","blanket"]
s12=["go to cave","cave","go cave","walk to cave","move to cave","walk to the cave","move to the cave","walk inside cave","walk inside the cave"]
s13=["run","sprint","dash","escape"]
s14=["play dead","fake dead","lie still","lie down"]
s15=["go to bush","bush","go bush","walk to bush","move to bush","walk to the bush","move to the bush","go to the bush"]
s16=["eat berries","ingest berries","eat"]
s17=["nap","sleep","rest"]
s18=["scout area","scout","look around","walk around"]
s19=["run in front of car","go in front car","go in front of the car","stand in front car","run in front","in front"]
s20=["yell","scream","yell at car","yell at driver","scream at car","scream at driver"]
s21=["fish","fishing","go fishing"]



#List of Commands for the "I don't understand" function

a1=["go to river","river","go river","walk to river", "move to river","walk to the river","move to the river","go to the river","go to monkey","monkey","go monkey","walk to monkey","move to monkey","walk to the monkey","move to the monkey","go to the monkey","go to tree","tree","go tree","walk to tree","move to tree","walk to the tree","move to the tree","go to the tree"]
a2=["go to river","river","go river","walk to river", "move to river","walk to the river","move to the river","go to the river","go to monkey","monkey","go monkey","walk to monkey","move to monkey","walk to the monkey","kick","kick tree","move to the monkey","go to the monkey","go to tree","tree","go tree","walk to tree","move to tree","walk to the tree","move to the tree","go to the tree","shake tree","shake the tree","hit the tree","shake","climb tree","climb up","climb"]
a3=["pet","attack","go to river","river","go river","walk to river", "move to river","walk to the river","move to the river","go to the river","go to monkey","monkey","go monkey","walk to monkey","move to monkey","walk to the monkey","move to the monkey","go to the monkey","go to tree","tree","go tree","walk to tree","move to tree","walk to the tree","move to the tree","go to the tree","pet monkey","pat monkey","eat","eat monkey","kill","monkey pet","attack monkey","kill monkey","attack","hurt","hurt monkey"]
a4=["go to river","river","go river","walk to river", "move to river","walk to the river","move to the river","go to the river","go to tree","tree","go tree","walk to tree","move to tree","walk to the tree","move to the tree","go to the tree"]
a5=["go to monkey","monkey","go monkey","walk to monkey","move to monkey","walk to the monkey","move to the monkey","go to the monkey","pet","pet monkey","pat monkey","eat","eat monkey","kill","monkey pet","attack monkey","kill monkey","attack","hurt","hurt monkey"]
a6=["swim across river","swim","swim over","swim over river","swim over the river","swim across the river","cross river","drink the water","drink water","drink","sip","sip water","fish","fishing","go fishing"]
a7=["go to bush","bush","go bush","walk to bush","move to bush","walk to the bush","move to the bush","go to the bush","go to cave","cave","go cave","walk to cave","move to cave","walk to the cave","move to the cave","walk inside cave","walk inside the cave"]
a8=["eat berries","ingest berries","eat","scout area","scout","look around","walk around"]
a9=["nap","sleep","rest","scout area","scout","look around","walk around"]
a10=["swim across river","swim","swim over","swim over river","swim over the river","swim across the river","cross river","drink water","drink","sip","sip water","fish","fishing","go fishing"]
a11=["run","sprint","dash","escape","play dead","fake dead","lie still","lie down"]
a12=["run in front","in front","run in front of car","go in front car","go in front of the car","stand in front car","yell","scream","yell at car","yell at driver","scream at car","scream at driver"]
a13=["go to monkey","monkey","go monkey","walk to monkey","move to monkey","walk to the monkey","move to the monkey","go to the monkey","go to tree","tree","go tree","walk to tree","move to tree","walk to the tree","move to the tree","go to the tree"]
a14=["yes","no"]
a15=["pet monkey","pat monkey","monkey pet","pet","attack monkey","kill monkey","attack","hurt","hurt monkey","attack","go to monkey","monkey","go monkey","walk to monkey","move to monkey","walk to the monkey","move to the monkey","go to the monkey"]
a16=["go to tree","tree","go tree","walk to tree","move to tree","walk to the tree","move to the tree","go to the tree","go to river","river","go river","walk to river", "move to river","walk to the river","move to the river","go to the river"]
directions=["East","east","south","South","West","west","North","north"]
north=["North","north"]
east=["East","east"]
south=["South","south"]
west=["West","west"]
numbers=["1","2","3"]
shore=["shore","shoreline","shore line"]
forest=["forest","trees","rain forest","jungle"]
rocks=["rocks","gravel","stones"]
fires=["shore","shoreline","shore line","forest","trees","rain forest","jungle","rocks","gravel","stones"]



#Beginning of Real Script



#Start of Game with Defined Function
import time
import random
#Pre-game 
play=['yes','no']
startGame=input("Do you want to start the game? (yes/no): ")
while startGame not in play:
    startGame=input("Do you want to start the game? (yes/no): ")
print('')
while startGame=="yes":
    
    #Instructions
    print("This is a choose your own adventure game. You will need to type in commands to \
progress further in the game. All commands are to be inputed after storyline text is given. \
When '>' appears, it is a sign to input your command. All comands are to be typed in lowercase. \
In addition, please be mindful to not put any unecessary spaces in your command. \
There are many routes to take, and there will be many commands that the program will not \
understand. It is encouraged to keep on trying commands to trigger moving forward in the game. \
Energy is printed every time you input a valid command to help you keep track of how much energy you have left. \
It is recommened to start with level 1 since level 2 is more difficult. Have fun!")
    print('')
    
#Starting the Game
    gameMode=input("Select game level (1/2): ")
    print("")
    while gameMode=="1":
        #Energy Counter
        energy=50
        time.sleep(0.5)
        #Instroduction of Story
        print("It is 13:00, you are racing down an abandoned dirt path at high speeds \
in a jungle, suddenly you hit a rock that jolts you into the side of the car. \
The impact severely damages your suspension sending you veering out of control \
until your car collides into a tree and your world goes blank.")
        print(" ")
        time.sleep(3)
        print("You wake up lying on the ground beside your scorched car, your head is throbbing with every pulse of blood spurting out")
        print(" ")
        time.sleep(1)
        print("You focus hard and study your surroundings, you notice some items were ejected out of the car after the impact before they burned to ashes")
        print(" ")
        time.sleep(1)
        print("Due to your current state, you are too weak to carry more than one object, you must pick up an object and evacuate the area before the car blows leaving you dead")
        print(" ")
        time.sleep(1)
        #Choosing your inventory
        objects=["BLANKET","LIFE JACKET"]
        print("The objects are a BLANKET and a LIFE JACKET")
        time.sleep(0.5)
        print("Select the item that you desire to carry along with you: ")
        time.sleep(0.2)
        item=input(">")
        while item not in s10:
            print("I don't understand")
            print("Select the item that you desire to carry along with you: ")
            time.sleep(0.2)
            item=input(">")
        inventory=[]
        inventory.append(item)
        
#Game Begins

        print("You look around yourself. A flowing RIVER and a massive palm TREE surround you. \
Before you realize, a small MONKEY appears. The thirst of survival begins now.")


        #Tree Route
        monkeyCount=0
        time.sleep(0.2)
        command=input('>')
        while command not in a1:
            print("I don't understand")
            time.sleep(0.2)
            command=input('>')
        for i in range(10):
            while command in s3:
                energy=energy-5
                if energy <= 0:
                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                    time.sleep(1)
                    print(" ")
                    game()
                print("energy =",energy)
                print("You are now beside the tree")
                time.sleep(0.2)
                command=input('>')
                while command not in a2:
                    print("I don't understand")
                    time.sleep(0.2)
                    command=input('>')
                counter=1
                counter1=1
                for i in range(3):
                    #Shaking the Tree
                    while command in s4:
                        energy=energy-5
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            print(" ")
                            game()
                        print("energy =",energy)
                        if counter>=3:
                            print("A coconut fell on your head")
                            print("YOU DIED")
                            ##########################
                            time.sleep(1)
                            print(" ")
                            game()
                        print("A coconut falls from the tree beside you, and you eat it")
                        energy=energy+10
                        print("energy =",energy)
                        counter=counter+1
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a2:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                    #Climbing the Tree
                    while command in s5:
                        energy=energy-8
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        if counter1>=3:
                            print("You died, the tree collapsed under your weight")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()
                        print("You climb the tree and see smoke from across the river, then you climb down")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a2:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')


            #Monkey Route
            while command in s2:
                energy=energy-5
                if energy <= 0:
                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                    time.sleep(1)
                    print(" ")
                    game()
                print("energy =",energy)
                while command in s2 and monkeyCount>=1:
                    print("The monkey has left, select another command.")
                    time.sleep(0.2)
                    command=input('>')
                    while command in a5:
                        print("The monkey has left, select another command not related to the monkey.")
                        time.sleep(0.2)
                        command=input('>')
                    while command not in a16:
                        print("The monkey has left, select another command not related to the monkey.")
                        time.sleep(0.2)
                        command=input('>')
                while command in s2 and monkeyCount<1:
                    print("The monkey is now right in front of you")
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a3:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')
                    #Petting the Monkey
                    if command in s6:
                        print("The monkey appears to enjoy being pet, after it leaves it gives you a banana, and you eat it")
                        energy=energy+15
                        print("energy =",energy)
                        monkeyCount=monkeyCount+1
                        time.sleep(0.2)
                        command=input('>')
                        while command in a5:
                            print("The monkey has left, select another command")
                            time.sleep(0.2)
                            command=input('>')
                        while command not in a4:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                    #DEATH from Attacking the Monkey
                    elif command in s7:
                        print("The monkey runs off only to come back with a gang of apes that devours you")
                        print("YOU DIED")
                        ########################
                        time.sleep(1)
                        print(" ")
                        game()


        #River Route
        while command in s1:
            energy=energy-5
            if energy <= 0:
                print("You died of exhaustion, WATCH YOUR ENERGY!")
                time.sleep(1)
                print(" ")
                game()
            print("energy =",energy)
            print("The river rushes in front of you")
            time.sleep(0.2)
            command=input('>')
            while command in a13:
                print("A water dam breaks sending water rushing at high speeds, it is not possible to return back.")
                time.sleep(0.2)
                command=input('>')
            while command not in a6:
                print("I don't understand")
                time.sleep(0.2)
                command=input('>')
            waterCounter=0
            for i in range(10):
                #Drinking the Water
                while command in s9:
                    energy=energy-10
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    if waterCounter>=2:
                        print("You get really sick from the water and die")
                        print("YOU DIED")
                        ########################
                        time.sleep(1)
                        print(" ")
                        game()
                    print("You drink the water and puke")
                    waterCounter=waterCounter+1
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a10:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')
                #Fishing
                counter=1
                while command in s21:
                    print("You decide to go near the shore of the river to grab fish with your bear hands. Caveman style.")
                    fish=random.randint(1,3)
                    if counter>2:
                        print("A shark jumps up and eats you whole. Ouch, indeed.")
                        print("YOU DIED")
                        print('')
                        game()
                    if 2==fish:
                        print("energy =",energy)
                        print("Bingo! You caught a surgeonfish. It was a simple operation, right?!")
                        energy=energy+10
                        print("energy =",energy)
                        counter=counter+1
                        command=input('>')
                    elif 2!=fish:
                        print("energy =",energy)
                        print("Not even a nibble...")
                        energy=energy-1
                        print("energy =",energy)
                        counter=counter+1
                        command=input('>')
                    while command not in a6:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')      
                #Successfully Swimming Across the River
                if command in s8 and energy>=46 or "life jacket" in inventory:
                    print("You make it to the other side and lay on the shore")
                    print("You lie on the shore bank exhausted from your swim, you are hungry and tired")
                    time.sleep(1)
                    print("You see a CAVE nearby and a BUSH filled with berries")
                    energy=energy-18
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a7:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')

                        
                    #Cave Route
                    if command in s12:
                        energy=energy-5
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        print("You run into the dark cave and before you know it a bear is looming over you staring into your eyes")
                        time.sleep(0.5)
                        print("You remember someone mentioned before to you that bears do not attack if you play dead")
                        print("Natural instinct though wants you to run")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a11:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                        #Successful Bear Encounter
                        if command in s13 and energy>=35:
                            print("You sprint to the road and see a group of fellow bear hunters")
                            time.sleep(0.5)
                            print("The bear hunters kill the bear for you, and you are saved")
                            print("They take you to their home, and you happily eat bear together.")
                            print("YOU ARE SAVED")
                            time.sleep(1)
                            print("You scored:",energy)
                            time.sleep(1)
                            ########################
                            print(" ")
                            game()
                        #DEATH from Running from the Bear
                        elif command in s13:
                            print("Due to your tired state,you try run like a drunk maniac only to collapse and be devoured by the bear, you did make a great meal though")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()
                        #Playing DEAD from the Bear
                        elif command in s14:
                            print("Unfortunately the playing dead was for a different bear species, the bear walks up to you and you feel your arteries in your neck rip with your spine as it gruesomely decapitates you")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()

                            
                    #Berry Bush Route
                    elif command in s15:
                        energy=energy-5
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        print("You walk to the bush with berries, they are of a darker purple colour")
                        print("You are extremely hungry, though you want to scout the area and look for something else")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a8:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                        #Eating Berries
                        if command in s16:
                            print("You start to feel more energized and stronger")
                            energy=energy+15
                            print("energy =",energy)
                            print("You can now look around, but you feel somewhat tired.")
                            print("Maybe sleeping would be nice.")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a9:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #Successfully Sleeping after Eating Berries
                            if command in s17 and "blanket" in inventory:
                                print("You use your blanket for a nap, and it keeps your body warm and refreshed.")
                                energy=energy+4
                                print("energy =",energy)
                                time.sleep(0.2)
                                command=input('>')
                                while command not in s18:
                                    print("I don't understand")
                                    time.sleep(0.2)
                                    command=input('>')

                                    
                                #Car Arrives
                                if command in s18:
                                    energy=energy-5
                                    if energy <= 0:
                                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                                        time.sleep(1)
                                        print(" ")
                                        game()
                                    print("energy =",energy)
                                    print("Fighting your body you walk around looking for help")
                                    print("You see a jeep driving through the forest")
                                    time.sleep(1)
                                    print("Your last minute thinking tells you to run infront and wave your arms")
                                    print("Or yell at the driver to stop")
                                    time.sleep(0.2)
                                    command=input('>')
                                    while command not in a12:
                                        print("I don't understand")
                                        time.sleep(0.2)
                                        command=input('>')
                                    #DEATH from Running in Front of the Car
                                    if command in s19:
                                        print("The driver just happened to be on his phone playing crossy roads")
                                        print("He does not see you and runs you over-you die from severe brain trauma")
                                        print("YOU DIED")
                                        ########################
                                        time.sleep(1)
                                        print(" ")
                                        game()
                                    #Yelling to the Car and Getting SAVED
                                    elif command in s20:
                                        print("Using every last bit of energy, you yell at the driver to stop")
                                        print("He pulls over to take you in")
                                        print("YOU ARE SAVED")
                                        time.sleep(1)
                                        print("You scored:",energy)
                                        time.sleep(1)
                                        print(" ")
                                        game()
                            #DEATH from Sleeping 
                            elif command in s17:
                                print("After 5 minutes of sleeping you wake up to an excruciating pain and jolt in spasms until you reach your death")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            #DEATH from Eating Berries and Scouting
                            elif command in s18:
                                print("In your sudden rush of joy from finding food, you start to look around")
                                print("You see the smoke from a potential village, you run towards it")
                                print("Out of the blue, you collapse and your body goes completely numb")
                                time.sleep(2)
                                print("You die from the berries poisoning you")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                        elif command in s18:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            print("Fighting your body you walk around looking for help")
                            print("You see a jeep driving through the forest")
                            time.sleep(1)
                            print("Your last minute thinking tells you to run in front and wave your arms")
                            print("Or yell at the driver to stop")
                            command=input('>')
                            while command not in a12:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #DEATH from Running in Front of the Car
                            if command in s19:
                                print("The driver just happened to be on his phone playing crossy roads, how ironic")
                                print("He does not see you and runs you over-you die from severe brain trauma")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            #Yelling to the Car and Getting SAVED
                            elif command in s20:
                                print("Using every last bit of energy, you yell at the driver to stop")
                                print("He pulls over to take you in")
                                time.sleep(0.5)
                                print("YOU ARE SAVED")
                                time.sleep(1)
                                print("You scored:",energy)
                                time.sleep(1)
                                print(" ")
                                game()
                #Swimming across the River with not Enough Energy
                elif command in s8 and energy<46:
                    print("You start your crawl across the river, but out of fatigue, you get tired and drown")
                    print("YOU DIED")
                    ########################
                    time.sleep(1)
                    print(" ")
                    game()




                    
#Game level 2

                    
    while gameMode=="2":
        #Energy Counter
        energy=40
        time.sleep(0.5)
        #Instroduction of Story
        print("It is 13:00, you are racing down an abandoned dirt path at high speeds \
in a jungle, suddenly you hit a rock that jolts you into the side of the car. \
The impact severely damages your suspension sending you veering out of control \
until your car collides into a tree and your world goes blank.")
        print(" ")
        time.sleep(3)

        print("You wake up lying on the ground beside your scorched car, your head is throbbing with every pulse of blood spurting out")
        print(" ")
        time.sleep(1)
        print("You focus hard and study your surroundings only to see your car is engulfed in massive flames upside down")
        print(" ")
        time.sleep(1)
        print("You must leave the area soon before the car explodes completely!")
        print(" ")
        time.sleep(1)
      
#Game Begins

        #Explosion Scene
        print("You must take cover, you glance and see a TREE, BUSH, and BOULDERS, though you are in shock and cannot makeout much, which way do you run?")
        print("You can go EAST, WEST, or SOUTH, while you car is NORTH")
        time.sleep(0.2)
        command=input('>')
        while command not in directions:
            print("I don't understand")
            time.sleep(0.2)
            command=input('>')
        if command in east:
            print("You run towards a tree and hide")
            time.sleep(2)
            print("KABOOM!!!!")
            print("The car sends shrapnel flying everywhere, some pierce through the tree and puncture your body")
            energy=energy-30
            print("Energy Level Critical! Energy =",energy)
            time.sleep(0.5)
            #Survival Booklet Scene
            print("You quickly open your survival booklet and it has first aid measures, what chapter do you follow (1-3)?")
            time.sleep(0.2)
            command=input('>')
            while command not in numbers:
                print("I don't understand")
                time.sleep(0.2)
                command=input('>')
            chapter=random.randint(1,3)
            if command==str(chapter):
                print("Luckily you followed the right instructions and saved yourself")
                energy=energy+26
                print("energy =",energy)
            elif command != str(chapter):
                print("WRONG CHAPTER!!, you start to bleed yourself out, too tired you cant do anything")
                while energy>0:
                    print("Energy =",energy)
                    energy=energy-1
                    time.sleep(0.5)
                print("YOU DIED")
                time.sleep(1)
                print(" ")
                game()
        elif command in south:
            print("You find a large boulder and hide")
            print("You survive the blow thanks to the giant rock")
        elif command in west:
            print("A bush? OH NO, WRONG WAY!!! you thi...")
            time.sleep(1)
            print("KAABBBOOOMMM!!!!!")
            time.sleep(1)
            print("A shredded cylinder from a 3.6L Pentastar V6 Engine tears straight through your chest, RIP")
            print("YOU DIED")
            time.sleep(1)
            print(" ")
            game()
        elif command in north:
            print("Eh, whatever I think i forgot something in the ca...")
            time.sleep(0.9)
            print("A big flash meets you as you walk towards the car, The End.")
            time.sleep(0.5)
            print("YOU DIED")
            time.sleep(1)
            print(" ")
            game()
        time.sleep(0.5)
        print("You look around yourself. A flowing RIVER and a massive palm TREE surround you. \
Before you realize, a small MONKEY appears. The thirst of survival begins now.")


        #Tree Route
        monkeyCount=0
        time.sleep(0.2)
        command=input('>')
        while command not in a1:
            print("I don't understand")
            time.sleep(0.2)
            command=input('>')
        for i in range(10):
            while command in s3:
                energy=energy-5
                if energy <= 0:
                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                    time.sleep(1)
                    print(" ")
                    game()
                print("energy =",energy)
                print("You are now beside the tree")
                time.sleep(0.2)
                command=input('>')
                while command not in a2:
                    print("I don't understand")
                    time.sleep(0.2)
                    command=input('>')
                counter=1
                counter1=1
                for i in range(3):
                    #Shaking the Tree
                    while command in s4:
                        energy=energy-5
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        if counter>=3:
                            print("A coconut fell on your head")
                            print("YOU DIED")
                            ##########################
                            time.sleep(1)
                            print(" ")
                            game()

                        print("A coconut falls from the tree beside you, and you eat it")
                        energy=energy+10
                        print("energy =",energy)
                        counter=counter+1
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a2:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                    #Climbing the Tree
                    while command in s5:
                        energy=energy-8
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        if counter1>=3:
                            print("You died, the tree collapsed under your weight")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()
                        print("You climb the tree and see smoke from across the river, then you climb down")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a2:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')


            #Monkey Route
            while command in s2:
                energy=energy-5
                if energy <= 0:
                    print("You died of exhaustion, WATCH YOUR ENERGY!")
                    time.sleep(1)
                    print(" ")
                    game()
                print("energy =",energy)
                while command in s2 and monkeyCount>=1:
                    print("The monkey has left, select another command.")
                    time.sleep(0.2)
                    command=input('>')
                    while command in a5:
                        print("The monkey has left, select another command not related to the monkey.")
                        time.sleep(0.2)
                        command=input('>')
                    while command not in a16:
                        print("The monkey has left, select another command not related to the monkey.")
                        time.sleep(0.2)
                        commadn=input('>')
                while command in s2 and monkeyCount<1:
                    print("The monkey is now right in front of you")
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a3:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')
                    #Petting the Monkey
                    if command in s6:
                        print("The monkey appears to enjoy being pet, after it leaves it gives you a banana, and you eat it")
                        energy=energy+15
                        print("energy =",energy)
                        monkeyCount=monkeyCount+1
                        time.sleep(0.2)
                        command=input('>')
                        while command in a5:
                            print("The monkey has left, select another command")
                            time.sleep(0.2)
                            command=input('>')
                        while command not in a4:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                    #DEATH from Attacking the Monkey
                    elif command in s7:
                        print("The monkey runs off only to come back with a gang of apes that devours you")
                        print("YOU DIED")
                        ########################
                        time.sleep(1)
                        print(" ")
                        game()


        #River Route
        while command in s1:
            energy=energy-5
            if energy <= 0:
                print("You died of exhaustion, WATCH YOUR ENERGY!")
                time.sleep(1)
                print(" ")
                game()
            print("energy =",energy)
            print("The river rushes in front of you")
            time.sleep(0.2)
            command=input('>')
            while command in a13:
                print("A water dam breaks sending water rushing at high speeds, it is not possible to return back.")
                time.sleep(0.2)
                command=input('>')
            while command not in a6:
                print("I don't understand")
                time.sleep(0.2)
                command=input('>')
            waterCounter=0
            for i in range(10):
                #Drinking the Water
                while command in s9:
                    energy=energy-10
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    if waterCounter>=2:
                        print("You get really sick from the water")
                        print("YOU DIED")
                        ########################
                        time.sleep(1)
                        print(" ")
                        game()
                    print("You drink the water and puke")
                    waterCounter=waterCounter+1
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a10:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')
                #Fishing
                counter=1
                while command in s21:
                    print("You decide to go near the shore of the river to grab fish with your bear hands. Caveman style.")
                    fish=random.randint(1,3)
                    if counter>2:
                        print("A shark jumps up and eats you whole. Ouch, indeed.")
                        print("YOU DIED")
                        print('')
                        game()
                    if 2==fish:
                        print("energy =",energy)
                        print("Bingo! You caught a surgeonfish. It was a simple operation, right?!")
                        energy=energy+10
                        print("energy =",energy)
                        counter=counter+1
                        command=input('>')
                    elif 2!=fish:
                        print("energy =",energy)
                        print("Not even a nibble...")
                        energy=energy-1
                        print("energy =",energy)
                        counter=counter+1
                        command=input('>')
                    while command not in a6:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')                             
                #Successfully Swimming Across the River
                if command in s8 and energy>=46:
                    print("You make it to the other side and lay on the shore")
                    print("You lie on the shore bank exhausted from your swim, you are hungry and tired")
                    energy=energy-18
                    if energy <= 0:
                        print("You died of exhaustion, WATCH YOUR ENERGY!")
                        time.sleep(1)
                        print(" ")
                        game()
                    print("energy =",energy)
                    time.sleep(1)
                    
                    #Fire Scene
                    print("You decide it's best to make a fire to warm up, and to your luck you have a pocket lighter")
                    print("You can build a fire on the shoreline, forest, rocks")
                    time.sleep(0.2)
                    command=input('>')
                    shore=["shore","shoreline","shore line"]
                    forest=["forest","trees","rain forest","jungle"]
                    rocks=["rocks","gravel","stones"]
                    fires=["shore","shoreline","shore line","forest","trees","rain forest","jungle","rocks","gravel","stones"]
                    while command not in fires:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')
                    if command in shore:
                        print("You set up your fire on the shore")
                        time.sleep(1)
                        print("Shortly after rough waters hit high and put out your fire")
                        time.sleep(0.3)
                        print("You warmed up slightly but are still cold")
                        energy=energy+5
                        print("energy =",energy)
                    elif command in forest:
                        print("A genius idea sparks in your head")
                        print("You gather some sticks and light your fire")
                        time.sleep(2)
                        print("-NEWS HEADLINE-")
                        print("Lost man sets forest on fire, 1 casualty")
                        print("YOU DIED")
                        print(" ")
                        game()
                    elif command in rocks:
                        print("You set up a nice fire on the rocks, you warm up and are ready to cotinue")
                        energy=energy+12
                        print("energy =",energy)
                    print("You see a CAVE nearby and a BUSH filled with berries")
                    time.sleep(0.2)
                    command=input('>')
                    while command not in a7:
                        print("I don't understand")
                        time.sleep(0.2)
                        command=input('>')

                        
                    #Cave Route
                    if command in s12:
                        energy=energy-5
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        print("You run into the dark cave and before you know it a bear is looming over you staring into your eyes")
                        time.sleep(0.5)
                        print("You remember someone mentioned before to you that bears do not attack if you play dead")
                        print("Natural instinct though wants you to run")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a11:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                        #Successful Bear Encounter
                        if command in s13 and energy>=35:
                            print("You sprint to the road and see a group of fellow bear hunters")
                            time.sleep(0.3)
                            print("The bear hunters kill the bear for you, and you are saved")
                            print("They take you to their home, and you happily eat bear together.")
                            print("YOU ARE SAVED")
                            ########################
                            time.sleep(1)
                            print("You scored:",energy)
                            time.sleep(1)
                            print(" ")
                            game()
                        #DEATH from Running from the Bear
                        elif command in s13:
                            print("Due to your tired state,you try run like a drunk maniac only to collapse and be devoured by the bear, you did make a great meal though")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()
                        #Playing DEAD from the Bear
                        elif command in s14:
                            print("Unfortunately the playing dead was for a different bear species, the bear walks up to you and you feel your arteries in your neck rip with your spine as it gruesomely decapitates you")
                            print("YOU DIED")
                            ########################
                            time.sleep(1)
                            print(" ")
                            game()

                            
                    #Berry Bush Route
                    elif command in s15:
                        energy=energy-5
                        if energy <= 0:
                            print("You died of exhaustion, WATCH YOUR ENERGY!")
                            time.sleep(1)
                            print(" ")
                            game()
                        print("energy =",energy)
                        print("You walk to the bush with berries, they are of a darker purple colour")
                        print("You are extremely hungry, though you want to scout the area and look for something else")
                        time.sleep(0.2)
                        command=input('>')
                        while command not in a8:
                            print("I don't understand")
                            time.sleep(0.2)
                            command=input('>')
                        #Eating Berries
                        if command in s16:
                            print("You start to feel more energized and stronger")
                            energy=energy+15
                            print("energy =",energy)
                            print("You can now look around, but you feel somewhat tired.")
                            time.sleep(0.2)
                            print("Maybe sleeping would be nice.")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a9:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #DEATH from Sleeping 
                            if command in s17:
                                print("After 5 minutes of sleeping you wake up to an excruciating pain and jolt in spasms until you reach your death")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            #DEATH from Eating Berries and Scouting
                            elif command in s18:
                                print("In your sudden rush of joy from finding food, you start to look around")
                                print("You see the smoke from a potential village, you run towards it")
                                print("Out of the blue, you collapse and your body goes completely numb")
                                time.sleep(2)
                                print("You die from the berries poisoning you")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                        elif command in s18:
                            energy=energy-5
                            if energy <= 0:
                                print("You died of exhaustion, WATCH YOUR ENERGY!")
                                time.sleep(1)
                                print(" ")
                                game()
                            print("energy =",energy)
                            print("Fighting your body you walk around looking for help")
                            print("You see a jeep driving through the forest")
                            time.sleep(0.5)
                            print("Your last minute thinking tells you to run in front and wave your arms")
                            print("Or yell at the driver to stop")
                            time.sleep(0.2)
                            command=input('>')
                            while command not in a12:
                                print("I don't understand")
                                time.sleep(0.2)
                                command=input('>')
                            #DEATH from Running in Front of the Car
                            if command in s19:
                                print("The driver just happened to be on his phone playing crossy roads, how ironic")
                                print("He does not see you and runs you over, you die from severe brain trauma")
                                print("YOU DIED")
                                ########################
                                time.sleep(1)
                                print(" ")
                                game()
                            #Yelling to the Car and Getting SAVED
                            elif command in s20:
                                print("Using every last bit of energy, you yell at the driver to stop")
                                time.sleep(0.2)
                                print("He pulls over to take you in")
                                print("YOU ARE SAVED")
                                time.sleep(1)
                                print("You scored:",energy)
                                time.sleep(1)
                                print(" ")
                                game()
                #Swimming across the River with not Enough Energy
                elif command in s8 and energy<46:
                    print("You start your crawl across the river, but out of fatigue, you get tired and drown")
                    print("YOU DIED")
                    ########################
                    time.sleep(1)
                    print(" ")
                    game()

        

while startGame =="no":
    raise SystemExit
