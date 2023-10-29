import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from QElephant.QuBit import *

class Circuit:
    def __init__(self, n: int, instructions=[]):
        self.__instr = instructions
        self.__n = n
        self.__mubit = MuBit(self.__n)
        self.__mubit._MuBit__callBack = self.__recv
    
    def __recv(self, gate: str, target: int, neighbor: list[int]):
        self.__instr.append((gate, target, neighbor))
    
    def __rect(self, q_i: int, i: int, txt: str, size: int) -> None:
        rec = Rectangle((q_i-0.25, i-0.25), 0.5, 0.5, fill=False)
        if len(txt) >= 4:
            plt.text(q_i, i, txt, size=min(int(40/size), int(40/self.__n)), ha='center', va='center')
        else:
            plt.text(q_i, i, txt, size=min(int(70/size), int(70/self.__n)), ha='center', va='center')
        plt.gca().add_patch(rec)
    
    def __line(self, A, B) -> None:
        plt.plot([A[0], B[0]], [A[1], B[1]], color='Black')
    
    def __circle(self, x: float, y: float, radius: float) -> None:
        circ = Circle((x, y), radius, fill=True, color='Black')
        plt.gca().add_patch(circ)
    
    def draw(self) -> None:
        n = len(self.__instr)
        plt.yticks(range(self.__n), [f"QuBit {i}" for i in range(self.__n)])
        plt.xticks(range(1, n+1), [f"Step {i+1}" for i in range(n)])

        i = 0
        while i < n:
            txt, index, neigbhor = self.__instr[i]
            for q_i in range(self.__n):
                self.__line((i+0.5, q_i), (i+0.75, q_i))
                self.__line((i+1.25, q_i), (i+1.5, q_i))

                if q_i == index:
                    self.__rect(i+1, q_i, txt, n)
                    for neig in neigbhor:
                        self.__circle(i+1, neig, 0.05)
                        if neig > q_i:
                            self.__line((i+1, q_i+0.25), (i+1, neig))
                        elif neig < q_i:
                            self.__line((i+1, q_i-0.25), (i+1, neig))
                        else:
                            raise ValueError("Cannot apply gate twice on the same QuBit")
                else:
                    self.__line((i+0.75, q_i), (i+1.25, q_i))
            i += 1
        plt.show()

if __name__=="__main__":
    c = Circuit(3, [("CS", 0, [1]), ("CX", 2, [0]), ("TX", 1, [0, 2])])
    c.draw()