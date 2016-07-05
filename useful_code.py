a = ('Product', '500.00', '1200.00')
a = list(a)
a.insert(3, 'foobar')
a = tuple(a)
print a

>> ('Product', '500.00', '1200.00', 'foobar')





http://stackoverflow.com/questions/14931769/how-to-get-all-combination-of-n-binary-value
import itertools


lst = list(map(list, itertools.product([0, 1], repeat=n)))
# OR
lst = [list(i) for i in itertools.product([0, 1], repeat=n)]

# [a[b] for a,b in zip([(1,10),(2,20),(3,30)],[0,1,0])]



#len((1,2,3))    3
# (1,2,3)[0]     1
# max(1,2,3)     3


#(0,0.99999) (1,1.99999)