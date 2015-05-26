def roll_call_dwarves dwarf_array
  dwarf_array.each_with_index {|name,i| puts "#{i + 1}. #{name}"}
end

def summon_captain_planet calls_array
  calls_array.map{|e| e.capitalize + "!"}
end

def long_planteer_calls calls
  !calls.select{|e| e.length > 4 }.empty?
end

def find_the_cheese list
  cheese_types = ["cheddar", "gouda", "camembert"]
  i = list.index{|e| cheese_types.include?(e) }
  i ? list[i] : nil
end