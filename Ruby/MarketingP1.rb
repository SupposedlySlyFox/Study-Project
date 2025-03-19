puts "Insert your complete name: "
Name = gets.chomp
puts "Age (Only Numbers):"
Age = gets.chomp
puts "Welcome, #{Name}, you kinda look young for being #{Age[0]} years old!"

#Age being is using used as it's due to the chance that the user might say something like "18 years old" or something like that.
#On line 9..10 is supposed to be a better and cleaner version of 1..5.
#fname, mname, lname, age = gets.split.map.with_index { |v, i| i == 3 ? v.to_i : v }
#puts "#{fname} #{lname}, #{age} Anos"
