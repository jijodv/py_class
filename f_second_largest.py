
imax=0
s_max=0
list = [ 10, 40, 50, 20, 30]
for x in list:
    if x > imax:
        imax = x

for y in list:
    if y > s_max and y < imax:
        s_max = y

print "Second Max - ", s_max
