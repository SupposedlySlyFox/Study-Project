puts "What is the equation you wanna do: (Ex: 10 - 3)\n"
equation = gets.split(" ")

a, b, c = equation[0].to_i, equation[1], equation[2].to_i

case b
when "+"
    puts "Answer: #{a + c}"
when "-"
    puts "Answer: #{a - c}"
when "*"
    puts "Answer: #{a * c}"
when "/"
    unless c == 0
        puts "Answer: #{a / c}"
    else
    puts "Error."
    end
else
    puts "Invalid."
end
