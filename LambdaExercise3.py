food = [("Satay",1500),("Fried Rice" ,5000),("Meatballs", 7000),("Soto" ,6500),("Tempe", 3500)]
print("Food list with price(Rp)\n",food,"\n")

food.sort(key = lambda x:x[1])
print("Food list from cheapest price(Rp)\n",food)