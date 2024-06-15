# Assining crap
plaintext = str(input("What do you want encrypted? ")) # Get the plaintext
list = list(plaintext) # Convert to list
permlist = list # Used as permanent storage of the list
bs = 0 # Prepare variable
temp = "" # Temporary variable
print(list) # Just for testing purposes
testlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] 

# Subroutines
def listelong(list): # Don't even think of fucking touching this
    bs = len(list)
    while bs < 16:
        list.append("x")
        bs += 1

# The SubBytes step


# The ShiftRows step
list1 = list[0 : 3]
list2 = list[4 : 7]
list3 = list[8 : 11]
list4 = list[12 : 15]

def row2shift(list, temp):
	temp = list[0]
	list [0] = list[1]
	list [1] = list[2]
	list [2] = list[3]
	list [3] = temp
	
def row3shift(list, temp):
	row2shift(list, temp)

	
def row4shift(list, temp):
	temp = list[0]
	list [0] = list[1]
	list [1] = list[2]
	list [2] = list[3]
	list [3] = temp

# The MixColumns step
listelong(list)
row2shift(list2,temp)
print(list)
list = permlist
row3shift(list, temp)
print(list)

# The AddRoundKey