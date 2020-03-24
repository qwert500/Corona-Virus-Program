import random

class Individual:

    #gridSize 
    #travelTime
    #infectionTime

    def __init__(self):
        """ TO DO: make them able to travel to other countries(maybe other grids for other countries)"""

        self.xcoord = random.randint(1, self.gridSize) #all continents are 1000x1000, does not remeber initial home indices (x, y)
        self.ycoord = random.randint(1, self.gridSize)
        self.infectionTime = 0
        self.infectionStatus = 'Healthy' # Healthy, Infected, Cured, Dead.
        self.homeContinent = self.determineHomeContinent() 
        self.CurrentTravelTimeLeft = 0 
        self.currentContinent = self.homeContinent # current continent location, will determine grid

    def status(self):
        print("(x , y)=","(",self.xcoord,",", self.ycoord,")")
        print("Home continent: ",self.homeContinent)
        print("Current continent: ", self.currentContinent)
        print("Infection status: ", self.infectionStatus)

    def determineHomeContinent(self):
        #DATA from https://www.worldatlas.com/articles/continents-by-population.html 
        asiaTotPop = 4_581_757_408
        africaTotPop = 1_216_130_000
        europeTotPop = 738_849_000
        nAmerica = 579_024_000
        sAmerica = 422_535_000
        Oceania = 38_304_000
        totalEarthPopulation = asiaTotPop+africaTotPop+europeTotPop+nAmerica+sAmerica+Oceania
        rn = random.uniform(0, 1)
        if (rn <= 0.5669):
            homeContinent = 'Asia'
        elif ( rn > 0.5669 and rn <= 0.7305 ):
            homeContinent = 'Africa'
        elif ( rn > 0.7305 and rn <= 0.8299):
            homeContinent = 'Europe'
        elif ( rn > 0.8299 and rn <= 0.9078):
            homeContinent = 'North America'
        elif ( rn > 0.9078 and rn <= 0.9646):
            homeContinent = 'South America'
        elif (rn > 0.9646):
            # actually 3% higher probability due to approximations from initial data
            homeContinent = 'Oceania'
        else:
            print("ERROR in determineHomeContinent")
        return homeContinent

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
            currentContinent = 'Europe'
        elif (rn > 58 and rn <= 77.5):
            currentContinent = 'Asia' 
        elif (rn > 77.5 and rn <= 93.5):
            currentContinent = 'North America'
        elif (rn > 93.5 and rn <= 96.1):
            currentContinent = 'South America'
        elif (rn > 96.1 and rn <= 98.4):
            currentContinent = 'Africa'
        elif (rn > 98.4):
            currentContinent = 'Oceania'
        else:
            print('ERROR in travelDestination')
        return currentContinent

    def travelCountdown(self):
        if (self.CurrentTravelTimeLeft < 0):
            print("ERROR in travelCountdown, should not be able to enter this funtion")
        self.CurrentTravelTimeLeft-=1
    
    def travelHome(self):
        self.currentContinent = self.homeContinent
        self.xcoord = random.uniform(0, self.gridSize)
        self.ycoord = random.uniform(0, self.gridSize)

    def travel(self):
        self.CurrentTravelTimeLeft = 20
        self.currentContinent = self.travelDestination()
        self.xcoord = random.uniform(0, self.gridSize)
        self.ycoord = random.uniform(0, self.gridSize)
    
    def infectionTimeCountdownAndCure(self):
        self.infectionTime -= 1
        if (self.infectionTime == 0):
            self.infectionStatus = "Cured"

    def infect(self):
        if (self.infectionStatus == "Healty"):
            infectionStatus = "Infected"
            return infectionStatus

    def checkIfdeathAndDeath(self):
        rn = random.uniform(0, 1)
        # 4 percent risk of death in the infection time, i.e 4/20 each time step 
        if (rn <= 0.04/20):
            self.infectionStatus = "Dead"
   
    def update(self):
        self.randomWalk()

        if (self.infectionStatus == "Infected"):
            self.infectionTimeCountdownAndCure()
            self.checkIfdeathAndDeath()

        if (self.currentContinent == self.homeContinent):
            rn = random.uniform(1, 10000) # 5/10000 that a individual travel
            if (rn <= 5):
                self.currentContinent = self.travelDestination()
                self.CurrentTravelTimeLeft = self.travelTime
                print("someone Travelled")
        
        if (self.currentContinent != self.homeContinent):
            self.travelCountdown()
            if (self.CurrentTravelTimeLeft == 0):
                self.travelHome()

def main():

    POPULATION_SIZE = 5000
    GRID_SIZE = 1000
    TRAVEL_TIME = 10
    INFECTION_TIME = 20
    NUMBER_OF_TIME_STEPS = 100
    INITIAL_NUMBER_OF_INFECTED = 200
    population = []
    Individual.gridSize = GRID_SIZE
    Individual.travelTime = TRAVEL_TIME
    Individual.infectionTime = INFECTION_TIME

    for i in range (0, POPULATION_SIZE):
        population.append(Individual())

    initializationOfDisease(population, INITIAL_NUMBER_OF_INFECTED, POPULATION_SIZE)

    for i in range (0, NUMBER_OF_TIME_STEPS):
        indicesOfInfected = []
        indicesOfInfected = findInfected(population,POPULATION_SIZE)
        print("INDICES OF INFECTED:", indicesOfInfected)
        for index in range (0, len(indicesOfInfected)):
            for popindex in range (0, len(population)):
                spreadVirus(population[indicesOfInfected[index]], population[popindex])
        
        for index in range (0, POPULATION_SIZE):
            population[index].update()
    
    print("Run sucessfull")







def spreadVirus(infectedIndividual, individualInPopulation):
    if (infectedIndividual.currentContinent == individualInPopulation.currentContinent and
        infectedIndividual.xcoord == individualInPopulation.xcoord and 
        infectedIndividual.ycoord == individualInPopulation.ycoord):
        individualInPopulation.infect()
        print("Someone got infected from another one")
    
def findInfected(population, POPULATION_SIZE):
    indices = []
    for i in range (0, POPULATION_SIZE):
        if (population[i].infectionStatus == "Infected"):
            indices.append(i)
    return indices
    
def initializationOfDisease(population,INITIAL_NUMBER_OF_INFECTED, POPULATION_SIZE):
    count = 0
    while (count < INITIAL_NUMBER_OF_INFECTED):
        rn = random.randint(0, POPULATION_SIZE)
        if (population[rn].homeContinent == "Asia"):
            population[rn].infectionStatus = population[rn].infect()
            count += 1

if __name__ == "__main__":
    main()

    