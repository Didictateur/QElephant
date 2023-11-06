from QElephant.QuBit import *
import pytest

## MuBit
mq = MuBit(2)
q = mq[1]

X(q)
assert mq._MuBit__state == [0, 1, 0, 0]
H(q)
assert mq._MuBit__state == [1/math.sqrt(2), -1/math.sqrt(2), 0, 0]
CX(mq, 0, 1)
assert mq._MuBit__state == [1/math.sqrt(2), -1/math.sqrt(2), 0, 0]
Bell(mq, 0, 1, "phi+")
assert mq._MuBit__state == [1/math.sqrt(2), 0, 0, 1/math.sqrt(2)]
Bell(mq, 0, 1, "phi-")
assert mq._MuBit__state == [1/math.sqrt(2), 0, 0, -1/math.sqrt(2)]
Bell(mq, 0, 1, "psi+")
assert mq._MuBit__state == [0, 1/math.sqrt(2), 1/math.sqrt(2), 0]
Bell(mq, 0, 1, "psi-")
assert mq._MuBit__state == [0, 1/math.sqrt(2), -1/math.sqrt(2), 0]

mq = MuBit(3)
H(mq[1])
CZ(mq, 1, 2)
GHZ(mq)
assert mq._MuBit__state == [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 1/math.sqrt(2)]
W(mq)
assert mq._MuBit__state == [0, 1/math.sqrt(3), 1/math.sqrt(3), 0, 1/math.sqrt(3), 0, 0, 0]

## QuBit
q = QuBit()

X(q)
assert q._QuBit__state == [0, 1]
H(q)
assert q._QuBit__state == [1/math.sqrt(2), -1/math.sqrt(2)]
SQRTX(q)
assert q._QuBit__state == [complex(0, 1/math.sqrt(2)), -complex(0, 1/math.sqrt(2))]
Y(q)
assert q._QuBit__state == [-1/math.sqrt(2), -1/math.sqrt(2)]
Z(q)
assert q._QuBit__state == [-1/math.sqrt(2), 1/math.sqrt(2)]
S(q)
assert q._QuBit__state == [-1/math.sqrt(2), complex(0, 1/math.sqrt(2))]
T(q)
assert q._QuBit__state == [-1/math.sqrt(2), complex(0, 1/math.sqrt(2))*math.e**(complex(0, math.pi/4))]
