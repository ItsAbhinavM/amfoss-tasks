def is_prime(n)
  return false if n <= 1

  (2..Math.sqrt(n)).each do |i|
    return false if n % i == 0
  end

  true
end

def find_primes_up_to(limit)
  primes = []
  (2..limit).each do |num|
    primes << num if is_prime(num)
  end
  primes
end

puts "Enter a number: "
user_input = gets.chomp.to_i

if user_input < 2
  puts "There are no prime numbers less than 2."
else
  prime_numbers = find_primes_up_to(user_input)
  puts "Prime numbers from 2 to #{user_input}: #{prime_numbers.join(', ')}"
end
