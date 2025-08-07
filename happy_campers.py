#PYTHON LIST: consists of "[]" and a variable name with individual strings, floats and/or integers in it.
#Jason and RB will be going on a company vacation. A camping trip, and they'd need quite a few stuff

camping_stuff = ["Tent", "Sleeping_bags", "Camping_stove", "Water_bottles", "First_aid_kit", "Flashlights", "Warm_clothes", "Snacks", "Portable_table", "Camera", "Coffee_beans", "Espresso_machine", "Kettle", "Cups", "Hammock", "String_lights", "Bluetooth_speaker", "Inflatable_mattress", "Solar_power_bank", "Battery_packs", "Waterproof_cover", "Toolkit", "Silicone_mat", "Storage_bin"]

#They'd need campsite info too

camp_site = ["Ijebu-Ode, Onipe Village forest", 404, 89.3, True]
#The contents of camp_site are:
#The venue
#Starting point coordinates
#Temperature
#Is it dangerous?

# What if we want to add stuff to the list? We've got python methods to thank for that
# ".append()", ".extend()", and ".insert()" are a few examples of python methods
# ".append()" adds only one item to an already formed python list
# ".extend()" adds a bunch of items to an already formed python list
# There are other ways to also add to a list asides using methods:
# instead of using "camping_stuff.append("lorem")" or "camping_stuff.extend("lorem", "ipsum")" to add stuff you can use:
# camping_stuff = camping_stuff + ["lorem", "ipsum"]. This would be an alternate method for adding to python lists
# For ".insert()", it is used to add an item to a list wherever specifically we want to add them. Python lists are ordered in nature meaning when we do:
# me = camping_stuff[4]
# And then:
# print(me)
# It will return:
# First_aid_kit
# I know what you're thinking, but computer counts from zero, not one. Hence First_aid_kit being number 4 on the list
# So when you use the ".insert()", method:
camping_stuff.insert(0, "Bread")

# And...

print(camping_stuff)

# You'll get: ['Bread', 'Tent', 'Sleeping_bags', 'Camping_stove', 'Water_bottles', 'First_aid_kit', 'Flashlights', 'Warm_clothes', 'Snacks', 'Portable_table', 'Camera', 'Coffee_beans', 'Espresso_machine', 'Kettle', 'Cups', 'Hammock', 'String_lights', 'Bluetooth_speaker', 'Inflatable_mattress', 'Solar_power_bank', 'Battery_packs', 'Waterproof_cover', 'Toolkit', 'Silicone_mat', 'Storage_bin']



# We have methods to delete items from lists too
# ".clear()", ".remove()", and ".pop()" are examples
# ".clear()" will take out the whole list you made
# ".remove()" will delete a specific list item from that list, it has to be exactly the way that item is on the list else you'll get an error
# ".pop()" is interesting because it works like the delete counterpart of ".insert()". It uses the index number of items on a list to delete items. It can also return the value of what it has deleted, for example:

camping_stuff.pop(5)

# If I want to check what I deleted I can just:
print("Here's the item that was deleted: " + camping_stuff.pop(5))
# Check this out in your compiler and tell me what you think ;-)