from allclass import *
import inquirer 

def account_signin():
# if __name__ == "__main__":
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
            user = User.make_account(sign_in)   
            print(f"Welcome new user {sign_in}!")
            # plant_things()
        if inputs['login'] == 2:
            sign_in = input("Input your id")
            user = User.get_account(sign_in)
            print(f"Welcome back {sign_in}")
            plant_things
# account_signin()



def plant_things():
    while True:
        things_for = [
            inquirer.List('things', 
                message = "Plant....", 
                choices=[('Pick your plant!', 1),('Add your own plant!', 2), ('Delete plant :( ', 3), ('Upgrade the plant', 4), ('Let the zombie eat your brain!!....exit', 5)],
            ),
        ]
        collect = inquirer.prompt(things_for)

        # if collect['things'] == 1:
        #     (picking())
          
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
            if baby == 1:
                healing= Plant.get_plants(baby)
                healthy= print(f"You are healing {healing.name}, what is their new health: " )
                healing.heal_plant(healthy)

# plant_things()
            

# def picking():
#     while True:
#         seedOne = input("Pick a plant ! (input number)")
#         if seedOne == "1":
#             pickedP = Plant.selected_plant(seedOne)
#             print(f"You have picked, {seedOne}")
#         if seedOne == "2":
#             pickedP = Plant.selected_plant(seedOne)
#             print(f"You have picked, {seedOne}")
#         if seedOne == "3":
#             pickedP = Plant.selected_plant(seedOne)
#             print(f"You have picked, {seedOne}")
    # while seedOne == seedOne:
    #     z_pick = input("Choose the number of zombies you want your plant to go against: ")
    #     .horde(z_pick)
# picking()
        

# def game_play(plant):
#     while True:
#         print(f"Get ready to see a showdown of one plant against {z_pick}!!")
#         zombie_health = Zombies.health * z_pick
#         zombie_hits = Zombies.hits* z_pick
#         safe = zombie_health - {}.health 
#         no_heal = zombie_hits - {}.hits
#         if {}.health > zombie_health and {}.hits > zombie_hits:
#             print(f"Your plant won!! You even had {{self}.health} helath left!")
#         elif {}.health < zombie_health and {}.hits < zombie_hits:
#             print(f"You brain was eaten :( ")

  