require 'prime'

puts "Enter a value: "
limit = gets.chomp.to_i

Prime.each(limit) do |prime|
  puts prime
end