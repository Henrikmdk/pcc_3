'''3-1 create a list with friends names and make print the one at the time'''
friends = ['Anders', 'Niels', 'Heidi', 'Ilja', 'Rasmus', 'Rasmus']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
print()

'''3-2 print a greeting to each freind'''
print(f"Hej, " + friends[0] + "!")
print(f"Hej, " + friends[1] + "!")
print(f"Hej, " + friends[2] + "!")
print(f"Hej, " + friends[3] + "!")
print(f"Hej, " + friends[4] + "!")
print(f"Hej, " + friends[5] + "!\n")

'''3-3 creating a list of vehicles that I would like to own and print out why'''
vehicles = ['Cityvan', 'Passat', 'Yamaha R1', 'Diving boat']
print('I would like to aquire a ' + vehicles[0] + ", because it's super versatile in usage!")
print('I would like to aquire a ' + vehicles[1] + ", because it's a fine car!")
print('I would like to aquire a ' + vehicles[2] + ", because it's a beautiful bike!")
print('I would like to aquire a ' + vehicles[3] + ", because I dive a lot and it's very giving to be on the water!\n")

'''3-4 (3-9)creating a list of ppl i would invite for dinner'''
guests = ['Marcus Aurelius', 'Jack Black', 'Donald Trump']
#3-9
print(f"Inviting {len(guests)}" + " guests")

print("Dear " + guests[0] + ", please come and eat, yes?")
print("Dear " + guests[1] + ", please come and eat, yes?")
print("Dear " + guests[2] + ", please come and eat, yes?\n")

'''3-5 (3-9)remove, replace and re-invite'''
#removing declinees
decline = guests.pop(1)
print("Dear " + decline + ", I'm sorry you're bailing out!\n")

#replacing
guests.insert(1, 'Elon Musk')

#3-9
print(f"Inviting {len(guests)}" + " guests")
#reinvite
print("Dear " + guests[0] + ", please come and eat, yes?")
print("Dear " + guests[1] + ", please come and eat, yes?")
print("Dear " + guests[2] + ", please come and eat, yes?\n")

'''3-6 (3-9)the Bigger Table -exercise '''
print("Dear " + guests[0] + ", I found a bigger table, so I'll add more ppl!")
print("Dear " + guests[1] + ", I found a bigger table, so I'll add more ppl!")
print("Dear " + guests[2] + ", I found a bigger table, so I'll add more ppl!\n")

#inserting in the beginning
guests.insert(0, 'Jojo Rabbit')

#finding the middle of the list
mid = len(guests)//2
guests.insert(mid, 'Django')

#inserting at the end
guests.append('Wolverine')

#3-9
print(f"Inviting {len(guests)}" + " guests")

#print
print("Dear " + guests[0] + ", please come and eat, yes?")
print("Dear " + guests[1] + ", please come and eat, yes?")
print("Dear " + guests[2] + ", please come and eat, yes?")
print("Dear " + guests[3] + ", please come and eat, yes?")
print("Dear " + guests[4] + ", please come and eat, yes?")
print("Dear " + guests[5] + ", please come and eat, yes?\n")

'''3-7 (3-9)shrinking the list'''

#remove from list and notify
removed = guests.pop(0)
print("Eeny, meeny, miny, moe... " + removed + " - Your'e out!")

removed = guests.pop(2)
print("Catch a tiger by the toe... " + removed + " - Your'e out!")

removed = guests.pop(2)
print("If he hollers let him go... " + removed + " - Your'e out!")

removed = guests.pop(1)
print("Eeny, meeny, miny, moe... " + removed + " - Your'e out!\n")

#3-9
print(f"Inviting {len(guests)}" + " guests")

print(guests[0] + ", You're still in!")
print(guests[1] + ", You're still in!\n")

#flushing the list
del guests[0]
del guests[-1]

#printing the empty list
print(f"List:  {guests}\n")

'''3-8 seeing the world'''
poi = ['A Blue Hole', 'Great Barrier Reef', 'Det Gule Rev', 'Bornholm', 'Den Undersøiske Mole']
print(poi)
print("\n")

#sorted print
print(sorted(poi))
print(poi)
print('\n')

#reverse sorted print
print(sorted(poi, reverse=True))
print(poi)
print('\n')

#reverse print
poi.reverse()
print(poi)
poi.reverse()
print(poi)
print('\n')

#sort print
poi.sort()
print(poi)
poi.sort(reverse=True)
print(poi)
print('\n')

'''3-10'''
#creating the list
menu = ["Thai Kylling", "Dansk Bøf", "Pasta Putanesca", "Kylling Danoise", "Fish'n'chips", "Bangers'n'mash", "Ribs'n'slaw"]

#sorting
print(menu)
print(f"Liste længde: {len(menu)}")
print(sorted(menu))
print(sorted(menu, reverse=True))
menu.sort()
print(menu)
menu.sort(reverse=True)
print(menu)

print("\n")

#adding
menu.insert(0, 'Dabba tilbyder')
menu.insert(len(menu)//2, 'Pølsemix')
menu.append('Marokansk kikærtegryde')
print(f"Liste længde: {len(menu)}")
print(menu)
print("\n")

#removing
popped = menu.pop(-1)
print(f"Liste længde: {len(menu)} sidste ret er fjernet {popped}")
print(menu)
print("\n")

menu.remove("Bangers'n'mash")
print(f"Liste længde: {len(menu)} slettet Bangers'n'mash")
print(menu)
print("\n")

del menu[1]
print(f"Liste længde: {len(menu)} slettet fra [1]")
print(menu)
print("\n")

#accessing values - tutorialspoint.com
print("menu[0]: ", menu[0])
print("menu[1:5]: ", menu[1:5])
print("\n")

#concatenating lists - tutorialspoint.com
sammensat_liste = menu + poi + guests
print(sammensat_liste)
print("\n")

#list iteration - tutorialspoint.com
for entry in sammensat_liste: print(entry)
print("\n")

#list compare - tutorialspoint.com
#result = cmp(poi, menu)
#print(result + '\n')



