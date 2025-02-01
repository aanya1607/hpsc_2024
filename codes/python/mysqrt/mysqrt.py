x=2.0
s=1.0
from numpy import sqrt
for k in range(10):
    s=0.5 * (s + x/s)
print(s)
