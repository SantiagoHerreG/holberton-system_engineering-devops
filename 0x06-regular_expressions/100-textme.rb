#!/usr/bin/env ruby
""" REGEX pattern matching project in Ruby
"""
input = ARGV[0]
varA = input.scan(/\[from:[^ ]+/).join
varB = input.scan(/\[to:[^ ]+/).join
varC = input.scan(/\[flags:[^ ]+/).join

result = ""

if varA
	result += varA.scan(/[^(\[from:)][^\]]+/).join + ","
end
if varB
	result += varB.scan(/[^(\[to:)][^\]]+/).join + ","
end
result += varC.scan(/[^(\[flags:)][^\]]+/).join

puts result
