# import sqlite3
# connection = sqlite3.connect("school.db")
# cursor = connection.cursor()

# cursor.execute('''''')
# connection.commit()

class Plant:
    def __init__(self, name, health=1000, spower=0, hits=0):
        self.name = name 
        self.health = health 
        self.spower = spower
        self.hits = hits 
        self.zombie=[]

#   def post_to_database(self):
#         cursor.execute('''
#         INSERT INTO teachers(name,email,specialty)
#         VALUES(?,?,?)
#         ''', (self.name,self.email,self.specialty))
#         connection.commit()

#     def patch_name(self,name):
#         cursor.execute('''
#         UPDATE teachers
#         SET name = ?
#         WHERE id = ?
#         ''',(name,self.id))
#         connection.commit()
#         self.name = name

#     def delete(self):
#         cursor.execute(f'''
#         DELETE FROM teachers
#         WHERE id = {self.id}
#         ''')
#         connection.commit()

class User(Plant):
    def __init__(self, chosen_plants, num_zombies=0, lives=3):
        super().__init__()
        self.chosen_plants = chosen_plants
        self.num_zombies = num_zombies
        self.lives = lives





class Zombies:
    def __init__(self, name, health=100, hits= 0, outfit=0):
        self.name = name 
        self.health = health 
        self.hits = hits 
        self.outfit = outfit 


# [random.randint(0, 640), random.randint(200, 300)]  # Spawn a brownie at a random position
#         self.brownie_img = pygame.image.load('/Users/donjuan/Downloads/data/images/brownie powerup.png')  # Load the brownie asset
    

#   window_width = 1050
#     window_height = 600
#     FPS = 60
#     game_window = pygame.display.set_mode((window_width, window_height))

#     pygame.display.set_caption("Plants VS Zombies")

#     background_image = pygame.image.load("lib/Game/Frontyard.jpg")

#     taskbar_image = pygame.image.load("lib/Game/Level_1-6.jpg")
#     taskbar_rect = taskbar_image.get_rect()
#     taskbar_rect.topleft = (0, 0)
