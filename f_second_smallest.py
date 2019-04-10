
f_min=100
s_min=100
list = [ 10, 40, 50, 20, 30]

for x in list:
    if x < f_min:
        f_min = x

print "First Min Number - ", f_min

for y in list:
    if y < s_min and y > f_min :
        s_min = y

print "Second Min - ", s_min
