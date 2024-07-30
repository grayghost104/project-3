import sqlite3
connection = sqlite3.connect("pvz.db")
cursor = connection.cursor()


class Plant:
    def __init__(self, name, health=1000, hits=0, id=None):
        self.id = id
        self.name = name 
        self.health = health 
        self.hits = hits 

        self.zombie=[]

    @classmethod
    def get_plants(cls):
        res = cursor.execute('SELECT * FROM plant')
        data = res.fetchall()
        all_plants = []
        for plant_tuple in data:
            all_plants.append(
                Plant(
                    id = plant_tuple[0], 
                    name = plant_tuple[1],
                    health = plant_tuple[2], 
                    hits = plant_tuple[3]
                )
            )
        return all_plants
    @classmethod
    def selected_plant(cls,id):
        res = cursor.execute(f'''
        SELECT * FROM plant
        WHERE id = {id}
        ''')
        data = res.fetchone()
        if data:
            return Plant(
                id = data[0],
                name = data[1],
                health = data[2], 
                hits = data[3]
            )

    
    def add_more_plants(self):
        cursor.execute('''
        INSERT INTO plant(name,health,hits)
        VALUES(?,?,?)
        ''', (self.name,self.health,self.hits))
        connection.commit()
        all = Plant.get_plants()
        self.id = all[-1].id



#sad :( 
    @classmethod
    def delete_plant(cls,bye):
        cursor.execute(f'''
        DELETE FROM plant
        WHERE id = {bye}
        ''')
        connection.commit()
    @classmethod
    def heal_plant(self,health):
        cursor.execute('''
        UPDATE plant
        SET health = ?
        WHERE id = ?
        ''',(health,self.id))
        connection.commit()
        self.health = health

    def picked_plant(self,name,health):
        pass


class User:
    def __init__(self,
    # lives=3 
    id=None):
        self.id = id 
        # self.lives = lives

    @classmethod
    def get_account(cls,id):
        res = cursor.execute(f'''
        SELECT * FROM login_info
        WHERE id = {id}
        ''')
        data = res.fetchone()
        if data:
            return User(
                id = data[0]
            )

    @classmethod
    def make_account(cls,user):
        print(user)
        cursor.execute(f'''
        INSERT INTO login_info(name)
        VALUES("{user}")
        ''')
        connection.commit()


class Zombies:
    def __init__(self, name, health=100, hits= 0,id= None):
        self.id = id
        self.name = name 
        self.health = health 
        self.hits = hits 
    @classmethod
    def get_zombie(cls,id):
        res = cursor.execute(f'''
        SELECT * FROM zombies
        WHERE id = {id}
        ''')
        data = res.fetchone()
        if data:
            return Zombies(
                name = data[2],
                hits = data[4]
            )

    def horde(self, coming = 0):
        self.coming = coming


    for i in ():
        pass

print(Zombies.get_zombie(1))

# print(Plant.add_more_plants(p1))

# p1 = Plant(
#     name = "backbend" ,
#     health =  10000999,
#     hits = 23948888
# )
# p1.add_more_plants()

# p1.heal_plant(34444)
# ugly_plx 

# ugly_plant.heal_plant(7)

# print(Plant.selected_plant(1))
# p2 = Plant.selected_plant(2)
# print(p2)
# p2.delete_plant()
