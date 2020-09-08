#Super Organized data(mini data)
#Fast as hell(constant time)
#curly brackets
dictionary={"banana":45,"redbeef":32}
print(dictionary["banana"])
print(dictionary.get("hello")) #even if you don't hVE THAT KEY IT Won't return error
#string is the key and the integer will be the value pertaining to the key
contact=(
'joe':["phone":1234555,"email":"ew@ghj.com"]
"bui":1234554
)
#save name and contact details
#adding element to the dictionary
contact["hari"]=56789
print(contact)
print(contact["bui"])
#word_count(
#basically you manually add items to the lists
)
3 methods in python for dictionaries.
#dict.items() # basically dict.item convert dictionary into tuples example
contact={"joe":({"phone":1234555},{"email":"ew@ghj.com"}),
"bui":1234554}
#save name
print(contact["bui"])
#word_count(
#basically you manually add items to the lists
#3 methods in python for dictionaries.
#dict.items[]
print(contact.items())
print(list(contact.items()))
print(list(contact.items[])
#dict.keys() returns only keys
print(contact.keys())
print(list(contact.keys()))
#dict.values()
print(contact.values())
print(list(contact.values()))
#Pop function dict.pop("key")
print(contact.pop("joe"))
print(contact)
contact.pop("joe")
print(contact)
#popitem dict.popitem()
#pops the last item
print(contact)
contact.popitem("joe")
print(contact.popitem("joe"))
print(contact)

#dict.clear()will basically clear the dictionary.
#If I am using Python 3.7 and onwards, dictionaries are ordered by default
#incase if it is unordered then try
From collections import ordereddict
#Casting towards a list from dictionary
list(contact.values())
print(sorted(list(contact.values()))

#dictionary comprehension
