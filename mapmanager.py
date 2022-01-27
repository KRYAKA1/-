# напиши здесь код создания и управления картой
import pickle 

class Mapmanager():
    def __init__(self):
        self.model = "block"
        self.texture = "block.png"
        self.startNew()
        self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        #self.reparentTo(self.land)
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    
    def Loadland(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0 
            for line in file:
                x = 0
                line = line.split(" ")
                for z in line:
                    for z0 in range(int(z)+1):
                        b = self.addBlock((x,y,z0))
                    x += 1
                y += 1
        return x,y
    
    def findBlock(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def isEmpty(self, pos):
        blocks = self.findBlock(pos)
        if blocks:
            return False
        else:
            return True
    
    def findHighestEmpty(self, pos):
        x, y, z = pos 
        z = 1 
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)

    def buildBlock(self, pos):
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new)

    def delBlock(self, position):
        blocks = self.findHighestEmpty(position)
        print(type(blocks))    
        for block in blocks:
            block.removeNode()

    
    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x, y, z - 1
        for block in self.findBlocks(pos):
                block.removeNode()

    def saveMap(self):

        blocks = self.land.getChildren()
        with open("my_map.dat", "wb") as fout:
            pickle.dump(len(blocks), fout)
            
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)

    def loadMap(self):
        self.clear()
        with open("my_map.dat", "rb") as fin:
            length = pickle.load(fin)

            for i in range(length):
                pos = pickle.load(fin)
                self.addBlock(pos)
                                       