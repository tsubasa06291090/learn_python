#リストの使い所

seat = []
min = 0
max = 5

print(min <= len(seat) < max)

seat.append('p')
print(seat)
print(min <= len(seat) < max)

seat.append('p')
seat.append('p')
print(seat)
print(min <= len(seat) < max)

seat.append('p')
print(seat)
print(min <= len(seat) < max)

seat.append('p')
print(seat)
print(min <= len(seat) < max) #５人以上は座れない

seat.pop()
print(seat)
print(min <= len(seat) < max) #１人減ったから座れる