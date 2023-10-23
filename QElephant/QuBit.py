import math
import random as rd

from QElephant.Matrix import *

I = complex(0, 1)

## Classes

class MuBit:
    def __init__(self, n: int=2) -> None:
        self.__n = n
        self.__state: list[complex] = [0]*(2**self.__n)
        self.__state[0] = 1
    
    def get_size(self) -> int:
        return self.__n
    
    def __str__(self) -> str:
        def next(N: str) -> str:
            if N == "":
                return ""
            if N[-1] == "0":
                return N[:-1]+"1"
            else:
                return (next(N[:-1]))+"0"
        
        txt = ""
        N = "0"*self.__n
        for i in range(2**self.__n):
            txt += f"{round(self.__state[i], 3)} |{N}>\n"
            N = next(N)
        return txt
    
    def __set(self, i: int, value: int) -> None:
        """Set the nth QuBit into value"""
        assert(value in {0, 1})

        M = Matrix([[1]])
        for j in range(self.__n):
            if j == i:
                M *= Matrix([[1-value, 0], [0, value]])
            else:
                M *= Matrix([[1, 0], [0, 1]])
        self.__state = M._Matrix__apply(self.__state)
        norm = math.sqrt(sum([abs(x)**2 for x in self.__state]))
        self.__state = [x/norm for x in self.__state]
    
    def __iter__(self):
        return iter([IQuBit(i, self) for i in range(self.__n)])
    
    def __getitem__(self, item: int) -> "QuBit":
        return IQuBit(item, self)

    def __apply(self, i: int, matrix: Matrix) -> None:
        M = Matrix([[1]])

        for j in range(self.n):
            if j == i:
                M *= matrix
            else:
                M *= Matrix.I()
        
        self.__state = M._Matrix__apply(self.__state)
    
    def __mapply(self, matrix: Matrix, i: int) -> None:
        M = Matrix([[1]])
        j = 0
        while j < self.__n:
            if j == i:
                M *= matrix
                j += 2
            else:
                M *= Matrix.I()
                j += 1
        self.__state = M._Matrix__apply(self.__state)
    
    def __getProb(self, i: int) -> float:
        """Probs for i to be zero"""
        M = Matrix([[1]])

        for j in range(self.__n):
            if j == i:
                M *= Matrix([[1, 0], [0, 0]])
            else:
                M *= Matrix.I()
        
        l = M._Matrix__apply(self.__state)
        return sum([abs(x)**2 for x in l])

    def observe(self) -> list[int]:
        l = []
        for i in range(self.__n):
            l.append(IQuBit(i, self).observe())
        return l
    
class QuBit:
    def __init__(self, alpha: complex=1, beta: complex=0):
        if abs(alpha)**2 + abs(beta)**2 != 1:
            raise Exception("The initial state must be normalized")
        self.__state = [alpha, beta]
        self.__intricated = False
    
    def is_intricated(self) -> bool:
        return self.__intricated
    
    def get_Mubit(self) -> None:
        return None
    
    def __str__(self) -> str:
        return f"{round(self.__state[0], 3)} |0> + {round(self.__state[1], 3)} |1>"
    
    def __apply(self, matrix: Matrix) -> None:
        self.__state = matrix._Matrix__apply(self.__state)
    
    def observe(self) -> list[int]:
        r = rd.random()
        if r < abs(self.__state[0])**2:
            self.__state = [1, 0]
            return 0
        self.__state = [0, 1]
        return 1

class IQuBit(QuBit):
    def __init__(self, n: int, mb: MuBit) -> None:
        super().__init__()
        self.__n = n
        self.__muBit = mb
        self.__intricated = True
    
    def is_intricated(self) -> bool:
        return self.__intricated
    
    def get_Mubit(self) -> tuple[MuBit, int]:
        return (self.__muBit, self.__n)
    
    def __str__(self) -> str:
        p = self.__muBit._MuBit__getProb(self.__n)
        return str(QuBit(math.sqrt(p), math.sqrt(1-p)))
    
    def __apply(self, matrix: Matrix) -> None:
        self.__muBit._MuBit__apply(self.__n, matrix)
    
    def observe(self) -> int:
        r = rd.random()
        if r < self.__muBit._MuBit__getProb(self.__n):
            self.__muBit._MuBit__set(self.__n, 0)
            return 0
        self.__muBit._MuBit__set(self.__n, 1)
        return 1





## Fonctions

def H(q: QuBit) -> None:
    if type(q) == IQuBit:
        q._IQuBit__apply(Matrix.H())
    elif type(q) == QuBit:
        q._QuBit__apply(Matrix.H())

def X(q: QuBit) -> None:
    if type(q) == IQuBit:
        q._IQuBit__apply(Matrix.X())
    elif type(q) == QuBit:
        q._QuBit__apply(Matrix.X())

def Y(q: QuBit) -> None:
    if type(q) == IQuBit:
        q._IQuBit__apply(Matrix.Y())
    elif type(q) == QuBit:
        q._QuBit__apply(Matrix.Y())

def Z(q: QuBit) -> None:
    if type(q) == IQuBit:
        q._IQuBit__apply(Matrix.Z())
    elif type(q) == QuBit:
        q._QuBit__apply(Matrix.Z())

def S(q: QuBit) -> None:
    if type(q) == IQuBit:
        q._IQuBit__apply(Matrix.S())
    elif type(q) == QuBit:
        q._QuBit__apply(Matrix.S())

def T(q: QuBit) -> None:
    if type(q) == IQuBit:
        q._IQuBit__apply(Matrix.T())
    elif type(q) == QuBit:
        q._QuBit__apply(Matrix.T())

def Rx(q: QuBit, phi: float) -> None:
    if type(q) == QuBit:
        q._QuBit__apply(Matrix.Rx(phi))
    elif type(q) == IQuBit:
        q._IQuBit__apply(Matrix.Rx(phi))

def Ry(q: QuBit, phi: float) -> None:
    if type(q) == QuBit:
        q._QuBit__apply(Matrix.Ry(phi))
    elif type(q) == IQuBit:
        q._IQuBit__apply(Matrix.Ry(phi))

def Rz(q: QuBit, phi: float) -> None:
    if type(q) == QuBit:
        q._QuBit__apply(Matrix.Rz(phi))
    elif type(q) == IQuBit:
        q._IQuBit__apply(Matrix.Rz(phi))

def R1(q: QuBit, phi: float) -> None:
    if type(q) == QuBit:
        q._QuBit__apply(Matrix.R1(phi))
    elif type(q) == IQuBit:
        q._IQuBit__apply(Matrix.R1(phi))

def CNOT(q: MuBit, n1: int, n2: int) -> None:
    SWAP(q, 0, n1)
    SWAP(q, 1, n2)
    q._MuBit__mapply(Matrix.CNOT(), 0)
    SWAP(q, 0, n1)
    SWAP(q, 1, n2)

def SWAP(q: MuBit, n1: int, n2: int) -> None:
    nmin = min(n1, n2)
    nmax = max(n1, n2)
    for i in range(nmin, nmax):
        q._MuBit__mapply(Matrix.SWAP(), i)
    for i in range(nmax-2, nmin-1, -1):
        q._MuBit__mapply(Matrix.SWAP(), i)

def Cu(q: MuBit, u: list[list[complex]], n1: int, n2: int) -> None:
    SWAP(q, 0, n1)
    SWAP(q, 1, n2)
    q._MuBit__mapply(Matrix.Cu(u), 0)
    SWAP(q, 0, n1)
    SWAP(q, 1, n2)

def test(q: QuBit) -> None:
    varName = None

    for name, value in locals().items():
        if value == q:
            varName = name
    print(varName)

if __name__=="__main__":
    q = MuBit(3)
    s = q[1].get_Mubit()