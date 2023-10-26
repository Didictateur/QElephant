from QElephant.QuBit import *

## for IQuBit
mq = MuBit(2)
q = mq[1]

X(q)
assert mq._MuBit__state == [0, 1, 0, 0]
H(q)
assert mq._MuBit__state == [1/math.sqrt(2), -1/math.sqrt(2), 0, 0]
CX(mq, 0, 1)
assert mq._MuBit__state == [1/math.sqrt(2), -1/math.sqrt(2), 0, 0]