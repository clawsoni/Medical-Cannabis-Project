# type = kind

## NEED TO ADD function to look for name of product, displayTerpenes, own list 

class Weed:
  def __init__(self, kind, strain, name, potency, effects, weight, price, withTax, terpenes, notes, own, dispensary):
    self.kind = kind
    self.strain = strain
    self.name = name
    self.potency = potency
    self.effects = effects
    self.weight = weight
    self.price = price
    self.withTax = withTax
    self.terpenes = terpenes
    self.notes = notes
    self.own = own
    self.dispensary = dispensary
#This class is to store each product at dispensaries. Not all fields are applicable in every instance yet. 


class Dispensary:
  def __init__(self, name, listOfThings):
      self.name= name
      self.listOfThings = listOfThings
#to store the information from different dispensaries. Has the name of the dispensary, and a list of Weed objects with all the products that dispendsary offers 


def makeList(file):
  itemList = []
  spread = open(file, "r")
  next(spread) #skips header 
  lines = spread.read().split('\n')
  for line in lines:  
    criteria = line.split(',')
    entry = Weed(criteria[0], criteria[1], criteria[2], criteria[3], criteria[4], criteria[5], criteria[6], criteria[7], criteria[8], criteria[9], criteria[10], "greenlight")
    itemList.append(entry)
    #entryD = Dispendsary("greenlight", dispensaryList)
  return itemList

def checkTerpenes(listW, many, look):
  print('\n')
  terpenesList = []
  if many == "no":
    look = look[0].lower()
    for entry in listW:  
      if look in entry.terpenes.lower():
        print(entry.name)
        terpenesList.append(entry)
  else:
    lookList = look.split(',')
    for entry in listW: 
      for item in lookList: 
        if item.lower() in entry.terpenes.lower():
          x = True
        else:
          x = False
      if x == True:
        print(entry.name)
        terpenesList.append(entry)
  print('\n')
  return terpenesList

#this function takes in a list of Weed ojects and displays the effects of each products
def displayEffects(listW):
  print('\n')
  for item in listW:
    print(item.name + " effects are " + item.effects)

#this function takes in a list of Weed objects and a list of effects and looks for specific effects
def checkEffects(listW, effectsList):
  itemList = []
  eList = {}
  for item in listW:
    for effect in effectsList:
      if item.name not in itemList:
        if effect in item.effects:
          itemList.append(item.name)
          eList[item.name] = item.effects
          print(item.name)
        
  next = input("Would you like to know the other effects of these strains? ")
  if next != "no":
    for item in eList.items():
      print(item) #format more later

#this function takes in a list of Weed ojects and displays the potency of each products
def displayPotency(listW):
  for item in listW:
    print(item.name + " has " + item.potency)

#this function takes in a list of Weed objects looks for the one with the highest potency
#need to work on formatting the csv first!!
def hightestPotency(listW):
  highest = 0
  strain = ''
  for item in listW:
    percents = item.potency.split(" ")
    num = float(percents[0].strip("%"))
    if num > highest:
      highest = num
      strain = item.name
  print(strain + " has the highest potency. It is " + item.potency)
  return strain

#this function takes in a list of Weed ojects and displays the strain of each products
def displayStrain(listW):
  for item in listW:
    print(item.name + " : " + item.strain)

#this function takes in a list of Weed objects and either "sativa", "indica", or "hybrid". It returns all the products of that strain
def specificStrain(listW, strain):
  strainList = []
  for item in listW: 
    #item is a list of weed objects
    for entry in item:
    #print(item)
      if strain in entry.strain:
        strainList.append(entry)
        print(entry.name)
  return strainList

#this function takes in a list of Weed objects and displays the amount for each (mg, oz, g)
def displayAmount(listW):
  for item in listW:
    print(item.name + "  is  " + item.weight)

#this function takes in a list of Weed objects and a specific amount, and a unit and then returns a list of the products that are sold in that amount
##!! make this work so that 3.5 g = 1/8 oz
def specificAmount(listW, amount, measurement):
  amountList = []
  for item in listW:
    num, unit = item.weight.split(" ")
    if unit.lower() == measurement.lower():
      if num == amount:
        amountList.append(item)
        print(item.name + " is " + item.weight)
  return amountList

#this function takes in a list of Weed objects and a string of "yes" or "no". it displays the prices with or without tax 
def displayPrice(listW, tax):
  for item in listW:
    if tax == "no":
      print(item.name + " costs " + item.price)
    else:
      print(item.name + " costs " + item.withTax)

#this function takes in a list of Weed objects and a number and displays products that are less than that price
def underPrice(listW, price, tax):
  priceList = []
  if "$" in price:
    price = price[1:] 
  for item in listW:
    if tax == "no":  
      if float(item.price[1: ]) < float(price):
        priceList.append(item)
        print(item.name + " costs " + item.price)
    else:
      if float(item.withTax[1: ]) < float(price):
        priceList.append(item)
        print(item.name + " costs " + item.withTax)
  return priceList

#this function takes in a list of Weed objects and either "yes" or "no". It returns the products that have or have not been tried
#return a list
def checkOwn(listW, tried):
  itemList = []
  for item in listW:
    for entry in item:
      print(entry.tried)
      if tried == "don't have":
        if entry.own == "no":
          itemList.append(item)
          print(entry.name)
      else:
        if entry.own == "yes":
          itemList.append(item)
          print(entry.name)
    if itemList == []:
      print("No Results")
  return itemList
 

#this function takes in a list of Weed objects and lists the notes for those products
def getNotes(listW):
  for item in listW:
    print(item.name + " notes: " + item.notes)

#this function takes in a list of Weed objects and returns what type they are
def displayTypes(listW):
  for item in listW:
    print(item.name + " : " + item.kind)

#this function takes in a list of Weed objects and either "flower", "disposable pen", "pre roll", "edible", or "concentrate". It returns the products of that type
def checkType(listW, kind):
  kindList = []
  for item in listW:
    if item.kind == kind:
      kindList.append(item)
      print(item.name)
  return kindList


def own(listW, have):
  ownList = []
  for item in listW:
    if item.own == "have":
      ownList.append(item)
      print(item.name)
  return ownList


#checkType(makeList("tester.csv"), "disposable pen")
