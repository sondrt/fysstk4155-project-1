from numpy import *

a = 2
b = a
a = 3
print(b)

a_list = [1]
a_array = ones(1)

print(a_array,a_list)

a_list_var = a_list[0]
a_array_var = a_array[0]

a_list_var = 2
a_array_var = 2


print(a_array,a_list)

def test(tekst):
	dict_bokstaver_til_tall = {
	"a":2 ,
	"b":2 ,
	"c":2 ,
	"d":3 ,
	"e":3 ,
	"f":3 ,
	"g":4 ,
	"h":4 ,
	"i":4 ,
	"j":5 ,
	"k":5 ,
	"l":5 ,
	"m":6 ,
	"n":6 ,
	"o":6 ,
	"p":7 ,
	"q":7 ,
	"r":7 ,
	"s":7 ,
	"t":8 ,
	"u":8 ,
	"v":8 ,
	"w":9 ,
	"x":9 ,
	"y":9 ,
	"z":9,
	" ":" "}
	for i in tekst:
		print(dict_bokstaver_til_tall[i],end="")

test("mikael kiste")