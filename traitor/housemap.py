class Room(object):

    def __init__(self,
                 name,
                 allowed_edges):

        self.name = name
        self.edges = {}
        for edge in allowed_edges:
            self.edges[edge] = None
        return None

    def set_coordnate(self,coordnate):
        self.x,self.y,self.z = coordnate
        return None

    def get_coordnate(self):
        return (self.x,self.y,self.z)

    
    def connect(self, direction, room):
        self.edges[direction] = room.get_coordnate()
        return None
    
    def bi_connect(self, direction, room):
    
        edge_table = [
            ["north","south"],
            ["south","north"],
            ["east","west"],
            ["west","east"],
            ["in","out"],
            ["out","in"],
            ["up","down"],
            ["down","up"]
        ]
        opposite_direction = None
        for d in edge_table:
            if d[0] == direction:
                opposite_direction = d[1]
                break
            else:
                continue
        if opposite_direction == None:
            return "Error: Missing Opposite Edge!"
    
        self.connect(direction, room)
        room.connect(opposite_direction, self)
    
    
    
    
    def is_connected_at(self, direction):
        if self.edges[direction] != None:
            return True
        else:
            return False
    
    def is_connected_to(self,room):
        if room in self.edges.values():
            return True
        else:
            return False
    
    def is_connected_to_at(self, room, direction):
        condition1 = self.is_connected_at(direction)
        condition2 = self.is_connected_to(room)
        if condition1 and condition2:
            return True
        else:
            return False
    
    def move(self, direction):
    
    
        try:
            return self.edges[direction]
        except KeyError:
            return self.get_coordnate()
        except:
            return "Unexpected Error!"
    



class Map(object):
    def __init__(self):
        MAP = {}

        MAP[(0,0,0)]= Room(
            "Entrance Hall",
            ("north","east","west"))

        MAP[(0,1,0)] = Room(
            "Foyer",
            ("north","south","east","west"))


        MAP[(0,2,0)] =  Room(
            "Grand Staircase",
            ("south","east","west"))

        MAP[(0,0,1)] = Room(
            "Upper Landing",
            ("north","south","east","west"))

        MAP[(0,0,-1)] = Room(
            "Basement Landing",
            ("north","south","east","west"))

        for room in MAP:
            MAP[room].set_coordnate(room)


        MAP[(0,0,0)].bi_connect("north", MAP[(0,1,0)])
        MAP[(0,1,0)].bi_connect("north", MAP[(0,2,0)])
        MAP[(0,2,0)].bi_connect("up", MAP[(0,0,1)])




        self.MAP = MAP

    
    def discover(self,coordnate, room):
    
        self.MAP[coordnate] = room
