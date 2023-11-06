from QElephant.QuBit import *
import pytest

q = QuBit(0, 1)

assert q._QuBit__state == [0, 1]
assert q._QuBit__entangled == False
assert q.is_entangled() == False
assert str(q) == "0 |0> + 1 |1>"
q._QuBit__apply(Matrix([[1, 2], [3, 4]]))
assert q._QuBit__state == [2, 4]
q.reset()
assert q._QuBit__state == [1, 0]

mq = MuBit(2)

assert mq._MuBit__state == [1, 0, 0, 0]
assert mq._MuBit__n == 2
assert mq.get_size() == 2
assert str(mq) == "1 |00>\n0 |01>\n0 |10>\n0 |11>\n"
mq._MuBit__state = [0.5]*4
mq._MuBit__set(1, 1)
assert mq._MuBit__state == [0, 1/math.sqrt(2), 0, 1/math.sqrt(2)]

q = mq[0]
assert q._IQuBit__n == 0
assert q._IQuBit__muBit == mq
assert q._IQuBit__entangled == True
assert q.is_entangled() == True
assert q.get_Mubit() == (mq, 0)
assert str(q) == "0.707 |0> + 0.707 |1>"
q._IQuBit__apply(Matrix([[1, 1], [1, -1]]))
assert mq._MuBit__state == [0, 2/math.sqrt(2), 0, 0]
q.reset()
assert str(q) == "1.0 |0> + 0.0 |1>"

mq._MuBit__state = [1, 1, 1, 1]
mq.reset()
assert mq._MuBit__state == [1, 0, 0, 0]
mq._MuBit__apply(Matrix([[0, 1], [1, 0]]), 0)
assert mq._MuBit__state == [0, 0, 1, 0]
mq._MuBit__mapply(Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 2, 0]]), 0)
assert mq._MuBit__state == [0, 0, 1, 2]
mq._MuBit__state = [0.5, 1, 2, 0]
assert mq._MuBit__getProb(0) == 1.25
mq._MuBit__SWITCH(0)
assert mq._MuBit__state == [0.5, 2, 1, 0]
mq = MuBit.intricateThem(QuBit(1,0), QuBit(0,1), QuBit(1,0), QuBit(0,1))
assert mq._MuBit__state == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]