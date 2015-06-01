# Define the four functions: roll_call_dwarves, summon_captain_planet, 
# long_planeteer_calls, and find_the_cheese

def roll_call_dwarves(dwarf_array):
  # dwarf_array.each_with_index {|name,i| puts "#{i + 1}. #{name}"}
    for i, name in enumerate(dwarf_array):
        print("%d. %s"%(i+1, name))

def summon_captain_planet(calls_array):
    return list(map(lambda call: call.capitalize() + "!", calls_array))

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(list_of_possible_cheeses):
    cheese_types = ["cheddar","gouda","camembert"]
    # return next((item for item in list_of_possible_cheeses if item in cheese_types), None)
    return next(filter(lambda item: item in cheese_types, list_of_possible_cheeses), None)