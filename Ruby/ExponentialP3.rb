puts "Insert 3 numbers separated by space:\n"
numbers = gets.split.map(&:to_i)

numbers.each do |num|
    puts num**3
end
