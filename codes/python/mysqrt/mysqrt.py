x=2.0
s=1.0
from numpy import sqrt
for k in range(10):
    print(f"at iteration {k} the value of s={s}")
    s=0.5 * (s + x/s)

