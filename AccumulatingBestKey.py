#  Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for i in placement:
    if i not in d:
        d[i] = 0
    d [i] += 1
mini = min(d.values())
for i in d:
    if mini == d[i]:
        min_value = i



# Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.

product = "iphone and android phones"
lett_d = {}
for i in product:
    if i not in lett_d:
        lett_d[i] = 0
    lett_d[i] += 1
maxi = max(lett_d.values())
for i in lett_d:
    if maxi == lett_d[i]:
        max_value = i

