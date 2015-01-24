def roll_call_dwarves(dwarves):
    result = ""
    for index,dwarf in enumerate(dwarves):
        result += "{}. {}".format(index+1,dwarf)
        if index != len(dwarves)-1:
            result+= " | "
    return result

def summon_captain_planet(forces):
    return [force.upper()+"!" for force in forces]

def long_planeteer_calls(planteer_calls):
    return [call for call in planteer_calls if len(call)>4]

def find_the_cheese(potentially_cheesy_items):
    cheeses = ["cheddar", "gouda", "cambert"]

    return [cheese for cheese in potentially_cheesy_items
            if cheese.lower() in cheeses]

def calculate_dollar_amount(receipt):
    return [str(item.count("$")) for item in receipt]

dwarves = ["Larry","Curly","Moe"]

print(roll_call_dwarves(dwarves))

forces = ["Earth","Wind","fire"]
print(summon_captain_planet(forces))

print(long_planeteer_calls(forces))

potential_cheese = ["James","cheddar", "CAMbert", "Guido", "flatiron"]

print (find_the_cheese(potential_cheese))

receipt = ["$$", "$", "$$$"]

print (calculate_dollar_amount(receipt))

