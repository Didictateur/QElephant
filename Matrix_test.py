from QElephant.Matrix import *

m = Matrix([[1, 2, 3], [4, 5, 6]])

assert m._Matrix__m == [[1, 2, 3], [4, 5, 6]]
assert m._Matrix__size == (2, 3)
m_ = m * Matrix([[1, 1], [0, 0]])
assert m_._Matrix__m == [
    [1, 1, 2, 2, 3, 3],
    [0, 0, 0, 0, 0, 0],
    [4, 4, 5, 5, 6, 6],
    [0, 0, 0, 0, 0, 0],
    ]
m_ = m._Matrix__apply([1, 2, 3])
assert m_ == [14, 32]
assert str(m) == "[[1, 2, 3], [4, 5, 6]]"
assert m.to_list() == [[1, 2, 3], [4, 5, 6]]