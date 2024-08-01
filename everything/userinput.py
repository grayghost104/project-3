from allclass import *
import inquirer 
#fun little thing to give credit to the creators of the original game
def ending_credits():
        print("This was orginally created by 4 people, but this downgraded version was created by Gray Hanna")
        print("#please dont sue me creators")



def game_play(pickedP):
    while True:
        num_zom= input("How many zombies you would like your plant to go against: ")
        z1 = Zombies.get_zombie(1)
        list_zom = z1.more(num_zom)
        zzz = int(num_zom)
        print(f"Get ready to see a showdown of one plant against {zzz} zombies!!")
        zombie_health= 0 
        zombie_hits = 0 
        for zom in list_zom:
            zombie_health += zom.health
            zombie_hits += zom.hits
        safe = zombie_health - pickedP.hits 
        no_heal = pickedP.health - zombie_hits
        if safe < 0 and no_heal > 0: 
            print(f"Your plant won!! You even had {no_heal} health left!")
            ending_credits()
        elif safe > 0 and no_heal < 0:
            print(f"You brain was eaten :( ")
            ending_credits()
        else:
            print("both sides lost :(")
            ending_credits()
#this function gets the plant and then passes the plant that you pick to the upper one, to see the gameplay and how your plant does agaisnt the number of zombies you input
def picking():
    while True:
        seedOne = input("Pick a plant ! (input number from 1-3)")
        if seedOne == "1":
            pickedP = Plant.selected_plant(seedOne)
            print(f"You have picked, the {pickedP.name}!")
            game_play(pickedP)
        if seedOne == "2":
            pickedP = Plant.selected_plant(seedOne)
            print(f"You have picked, the {pickedP.name}!")
            game_play(pickedP)
        if seedOne == "3":
            pickedP = Plant.selected_plant(seedOne)
            print(f"You have picked, the {pickedP.name}!")
            game_play(pickedP)
#This code is the "main menu" you are able to upgrade you plant, add your own, delete a plant, or start the game within pick your plant
#When you click on pick your plant it takes you to the upper function that shows you what plant you got
def plant_things():
    while True:
        things_for = [
            inquirer.List('things', 
                message = "Plant....", 
                choices=[('Pick your plant!', 1),('Add your own plant!', 2), ('Delete plant :( ', 3), ('Upgrade the plant', 4), ('Let the zombie eat your brain!!....exit', 5)],
            ),
        ]
        collect = inquirer.prompt(things_for)
        if collect['things'] == 1:
            picking()
        if collect['things'] == 2:
            name = input("Enter the name of your plant: ")
            health = input("Enter the health of your plant: ")
            hits = input("Enter the number of hits your plant can take: ")
            new_plant = Plant(name=name,health= health, hits=hits )
            new_plant.add_more_plants()
            print("Your plant has been added!")
        if collect['things'] == 3:
            bye = input("Enter the ID of the plant that you would like to delete: ")
            Plant.delete_plant(bye)           
        if collect['things'] == 4:
            baby = input("Your plant has been damaged :(, choose a plant to heal: ")  
            if baby == "1":
                healing= Plant.selected_plant(baby)
                healthy= print(f"You are healing {healing.name}, what is their new health: " )
                healing.heal_plant(healthy)

#this is the very beginning of the game, but since we have to call the function above within this function, and it has to already exist 
#its easiest for the code to go backwards!
#this is how a user creates a login or signs back in as themselves 
def account_signin():
    print('Welcome to Plant vs Zombies!')
    while True:
        questions = [
            inquirer.List('login', 
                message = "Create account, or Sign in to existing account", 
                choices=[('Create account', 1),('Sign in', 2), ('Take the easy way out...exit', 3)],
            ),
        ]
        inputs = inquirer.prompt(questions)

        if inputs['login'] == 1:
            sign_in = input("Input your name")
            user = User.get_account(sign_in)   
            print(f"Welcome new user!")
            plant_things()
        if inputs['login'] == 2:
            sign_in = input("Input your id")
            user = User.make_account(sign_in)
            print(f"Welcome back user!")
            plant_things()


account_signin()