#1. fill in this class
#   it will need to provide for what happens below in the
#	main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
# 	a function called showEvaluation, and an attribute carCount
class CarEvaluation:
    'A simple class that represents a car evaluation'
    #all your logic here

    carCount = 0

    def __init__(self, carBrand, carPrice, carSafety):
        self.carBrand = carBrand
        self.carPrice = carPrice
        self.carSafety = carSafety
        CarEvaluation.carCount += 1

# This is the main of the program. Expected outputs are in comments after the function calls.
    def showEvaluation(self):
        print "The", self.carBrand, "has a", self.carPrice, " price and its safety is rated a", self.carSafety

#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
# 	otherwise by descending price
def sortbyprice(cars, order):
    High = []
    Med = []
    Low = []
    for i in cars:
        if i.carPrice == "High":
            High.append(i.carBrand)
        elif i.carPrice == "Med":
            Med.append(i.carBrand)
        else:
            Low.append(i.carBrand)
    if order == "asc":
        return Low + Med + High
    else:
        return High + Med + Low

# This was a solution I learned from Honey Berk.
# I thought it was really easy to understand but is it efficient?

#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#	it returns true if the value is in the safety attribute of an entry on the list,
#   otherwise false
def searchforsafety(cars, safety):
    for i in cars:
        if i.carSafety == safety:
            return True
        else:
            return False

# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
   eval1 = CarEvaluation("Ford", "High", 2)
   eval2 = CarEvaluation("GMC", "Med", 4)
   eval3 = CarEvaluation("Toyota", "Low", 3)

   print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

   eval1.showEvaluation() #The Ford has a High price and it's safety is rated a 2
   eval2.showEvaluation() #The GMC has a Med price and it's safety is rated a 4
   eval3.showEvaluation() #The Toyota has a Low price and it's safety is rated a 3

   L = [eval1, eval2, eval3]

   print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
   print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
   print searchforsafety(L, 2); #true
   print searchforsafety(L, 1); #false
