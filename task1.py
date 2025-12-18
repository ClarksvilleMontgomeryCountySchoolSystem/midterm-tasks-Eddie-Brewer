
slices = party_pizza_mini + large + medium
print(f"Number of slices:{slices}")

people = people + 1
share = slices // people
leftover = slices % people
print(f'Share: {share}')
print(f'Leftover: {leftover}')

people = people + 2 #Eric and Brandon are coming too.
share = slices // people
leftover = slices % people
print(f'Share: {share}')
print(f'Leftover: {leftover}')

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

people = people + 1
share = slices // people
leftover = slices % people
print(f'Share: {share}')
print(f'Leftover:{leftover}')
print("...for Mr. Hollow Leg")
