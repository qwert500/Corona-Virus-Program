import random

class Individual:

    gridSize
    travelTime = 10

    def __init__(self):
        """ TO DO: make initial spawns according to earth population distributions"""
        """ TO DO: make them able to travel to other countries(maybe other grids for other countries)"""

        self.xcoord = random.randint(1, gridSize) #all continents are 1000x1000
        self.ycoord = random.randint(1, gridSize)
        self.infectionStatus = 'healthy' # healthy, infected, cured, dead.
        self.homeContinent # random.choise(list) from dist.
        self.CurrenttTravelTimeLeft = 0 
        self.currentContinent = homeContinent # current continent location, will determine grid

    def status(self):
        print("(x , y)=","(",self.xcoord,",", self.ycoord,")")

    def randomWalk(self): # ITS WORKING!
        rn = random.uniform(0, 1)
        if (rn <= 0.25 and self.xcoord > 0):
            self.xcoord -= 1
        elif (rn > 0.25 and rn < 0.5 and self.xcoord < self.gridSize):
            self.xcoord += 1
        elif (rn>0.5 and rn < 0.75 and self.ycoord > 0):
            self.ycoord -= 1
        elif (rn > 0.75 and self.ycoord < self.gridSize):
            self.ycoord += 1 

    def travelDestination(self):
        rn = random.randint(0,100)
        if (rn <= 58 ):
            self.currentContinent = 'Europe'
        elif (rn > 58 and rn <= 77.5):
            self.currentContinent = 'ASIA' 
        elif (rn > 77.5 and rn <= 93.5):
            self.currentContinent = 'North America'
        elif (rn > 93.5 and rn <= 96.1):
            self.currentContinent = 'South America'
        elif (rn > 96.1 and rn <= 98.4):
            self.currentContinent = 'Africa'
        elif (rn > 98.4):
            self.currentContinent = 'Oceania'
        else:
            print('ERROR in travelDestination')

    def travelCountdown(self):
        if (self.CurrenttTravelTimeLeft < 0):
            print("ERROR in travelCountdown, should not be able to enter this funtion")
        self.CurrenttTravelTimeLeft-=1
    
    def travelHome(self):
        self.currentContinent = self.homeContinent
    
        



def main():

    POPULATION_SIZE = 5
    GRID_SIZE = 1000
    TRAVEL_TIME = 10

    population = []
    Individual.gridSize = GRID_SIZE
    Individual.travelTime = TRAVEL_TIME

    for i in range (0, POPULATION_SIZE):
        population.append(Individual())
    
    for i in range (0, POPULATION_SIZE):
        population[i].randomWalk()


if __name__ == "__main__":
    main()