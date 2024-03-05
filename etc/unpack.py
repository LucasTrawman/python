def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins1 = [100, 50, 25]
# the * makes it that the list "coins" is unpacked and then will fill galleons, sickles and knuts. the same way as split works
print(total(*coins1), "Knuts")

coins2 = {"knuts": 25, "sickles": 50, "galleons": 100}
# to work for dictionaries the same way as it does with list, You will have to use ** instead of *
print(total(**coins2), "Knuts")
# the key from the dictionary needs to have the same name as the variable on the function total() to work