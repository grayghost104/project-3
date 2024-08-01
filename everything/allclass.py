import sqlite3
connection = sqlite3.connect("pvz.db")
cursor = connection.cursor()

#class of the plants and hold how to get all the plants, one plant, upgrade the plant, delete the plant, and add your own plant 
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

    def get_name(self):
        return self._name 
    def set_name(self, value):
        if type(value) is str:
            self._name = value
        else:
            print("Input letters")
    name = property(get_name, set_name)


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
        cursor.execute(f'''
        UPDATE plant
        SET health = {health}
        WHERE id = {id}
        ''',)
        connection.commit()
        self.health = health

#this is the user class that holds making an account, and finding your account if you already have one 
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

#this is the zombie class it holds a way to get one zombie and then the number of zombies you input as the horde 
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
                id = data[0],
                name = data[1],
                health = data[2], 
                hits = data[3]
            )

    def more(self,z_pick):
        coming = []
        zz = int(z_pick)
        for i in range (0, zz):
            horde = Zombies(
                name = self.name,  
                health = self.health,
                hits = self.hits  
            )
            coming.append(horde)
        return(coming)
