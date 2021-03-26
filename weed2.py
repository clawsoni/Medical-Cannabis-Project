from weed import Weed, Dispensary
from weed import makeList, checkEffects, checkTerpenes, checkOwn, checkType, displayAmount, displayEffects, displayPotency, displayStrain, displayStrain, displayTypes, hightestPotency, specificAmount, specificStrain, displayPrice, underPrice, getNotes, own

#need to work on what lists are being used as parameters, and returned 
#check tried and own
#make this the code for the user prompts

def welcomeStart():
  stores = input("\nWhich dispensaries do you want to look at?\n(comma separated) \n")
  storeList = stores.split(",")
  dispensaryList = []
  for store in storeList:
    if store[0] == " ":
      store = store[1:]
    csv = store + ".csv"
    itemList = makeList(csv)
    dispensaryList.append(Dispensary(store, itemList))

  lookAt = input("What would you like to look at? \n \nYou can filter based on: \n terpenes -> terp \n effects -> effects\n type -> type\n highest potency -> potency\n specific amounts -> amount \n sativa/indica/hybrid -> sih \n under a certain price -> price\n")

  return dispensaryList, lookAt

#restructure to put for loop of stores in helper function. use storeList as a parameter instead of store.listOfThings
def toStart(storeList, lookAt):
  for store in storeList:
    newList = []
    print("\nAt " + store.name + ": ")
    if lookAt == "terp":
      many = input("Are you looking for more than one terpene? ")
      look = input("what terpene are you looking for? ")
      result = checkTerpenes(store.listOfThings, many, look)
    elif lookAt == "effects":
      effectsList = input("what effects are you looking for? \n (comma separated)\n ")
      effectsList = effectsList.split(",")
      result = checkEffects(store.listOfThings, effectsList)
    elif lookAt == "type":
      typeW = input("Would you like to look at flower, edibles, prerolls, or disposable pen? ")
      result = checkType(store.listOfThings, typeW)
    elif lookAt == "potency":
      result = hightestPotency(store.listOfThings)
    elif lookAt == "amount":
      measurement = input("By what measurement? (oz, g, mg) ")
      amount = input("What amount are you looking for? ")
      result = specificAmount(store.listOfThings, amount, measurement)
    elif lookAt == "sih":
      kind = input("Would you like to look at indica, hybrid, or sativa? ")
      result = specificStrain(store.listOfThings, kind)
    elif lookAt == "price":
      maxP = input("What price would you like the product be under? ")
      tax = input("with taxes? ")
      result = underPrice(store.listOfThings, maxP, tax)
    elif lookAt == "own":
      own2 = input("Do you want to look at waht you own or don't own? ")
      result =own(store.listOfThings, own2)
    newList.append(result)
    store.listOfThings = newList
  return storeList
''''
def nextThing(dispensaryList):
  more = input("Would you like to filter more? ")
  if more == "no":
    info = input("Would you like more information on these products? ")
    if info != "no":
      #call another method that displayStrain
      x = True
      while x == True:
        nextLook = input("What more information would you like to know? \n \nYou can filter based on: \n terpenes -> terp \n effects -> effects\n type -> type\n highest potency -> potency\n specific amounts -> amount \n sativa/indica/hybrid -> sih \n under a certain price -> price\n if owned -> own \n If you want to filter more enter 'filter' followed by what you want to filter by \n")
        if "filter" in nextLook:
          x = False
          return toStart(dispensaryList, nextLook.split(" ")[1])
        else: 
          displayThings(dispensaryList, nextLook)
      
  else:
    nextLook = input("What more would you like to filter by? \nYou can filter based on: \n terpenes -> terp \n effects -> effects\n type -> type\n highest potency -> potency\n specific amounts -> amount \n sativa/indica/hybrid -> sih \n under a certain price -> price\n if it is a product we own\n If you want more information on this products enter 'info'\n")
    if nextLook == "info":

    else:
      return toStart(dispensaryList, nextLook)
'''

def displayThings(listW, lookAt):
  print('nanan')



#would you like to cross reference with something else? Would you like to know more about these results? 



def nextThing(dispensaryList):
  x = True
  while x == True:
    more = input("\nIf you would like more information on these products type 'info' followed by what you want to display\n Otherwise you can filter more based on: \n \nYou can filter based on: \n terpenes -> terp \n effects -> effects\n type -> type\n highest potency -> potency\n specific amounts -> amount \n sativa/indica/hybrid -> sih \n under a certain price -> price\n if owned -> own \n If you want to filter more enter 'filter' followed by what you want to filter by \n if you want to quit type 'quit'\n")
    if "info" in more:
      return displayThings(dispensaryList, more.split(" ")[1])
    elif "quit" in more:
      x = False
    else: 
      toStart(dispensaryList, more)

storeList, lookAt = welcomeStart()
take2 = toStart(storeList, lookAt)
nextThing(take2)