players= ["Mongraal", "Mr Savage", "veno", "Peterbot", "Bugha"]

for p in players:
    print(p)

# here we are using the len function to create a dynamic range so that it can change size depending on the length of the list
for p in range(len(players)):
    print(p + 1, players[p])

players_region = {"Mongraal":"EU", 
                  "Mr Savage":"EU", 
                  "veno":"EU", 
                  "Peterbot":"NA", 
                  "Bugha":"NA",
                  "Cooper":"NA"}

print(players_region["Mongraal"])

for x in players_region:
    print(x, players_region[x],sep=" - ")


# here you can see that you can create multiple dictionaries within a list to make a sort of data base that can store multiple keys and values
students_database = [
    {"Name":"Mongraal", "Region":"EU", "Input":"MKB"},
    {"Name":"Mr Savage", "Region":"EU", "Input":"MKB"},
    {"Name":"Veno", "Region":"EU", "Input":"MKB"},
    {"Name":"Peterbot", "Region":"NA", "Input":"MKB"},
    {"Name":"Bugha", "Region":"NA", "Input":"MKB"},
    {"Name":"Cooper", "Region":"NA", "Input":"MKB"},
]

# although they are seperate lists, thier key names are the same which means they can all be called at once
for y in students_database:
    print(y["Name"], y["Region"], y["Input"], sep=" - ")

