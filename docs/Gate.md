# Gates

Here is the list of all the main gates in quantum algorithm available in the library. In the following formulas, `i` represents the complex number.

## H(q: QuBit) -> None
`Hadamard's gate`. 

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
\frac {1} {\sqrt 2} & \frac {1} {\sqrt 2}\\
\frac {1} {\sqrt 2} & -\frac {1} {\sqrt 2}
\end{pmatrix}
```

## X(q: QuBit) -> None
`Pauli-X gate` or `NOT gate`. Inplementes a rotation aroud the x-axis of $\pi$ radians.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
```

## Y(q: QuBit) -> None
`Pauli-Y gate`. Inplementes a rotation aroud the y-axis of $\pi$ radians.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
0 & -i\\
i & 0
\end{pmatrix}
```

## Z(q: QuBit) -> None
`Pauli-Z gate`. Inplementes a rotation aroud z-axis of $\pi$ radians.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}
```

## S(q: QuBit) -> None
`NOT gate`. Invert the state |0> and |1> of the QuiBit q.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
1 & 0\\
0 & i
\end{pmatrix}
```

## T(q: QuBit) -> None
`NOT gate`. Invert the state |0> and |1> of the QuiBit q.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
1 & 0\\
0 & e^{i\frac\pi4}
\end{pmatrix}
```

## Rx(q: QuBit, phi: float) -> None
`NOT gate`. Inplementes a rotation aroud x-axis of $\phi$ radians.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
\cos(\frac\phi2) & -\sin(\frac\phi2)\\
\sin(\frac\phi2) & \cos(\frac\phi2)
\end{pmatrix}
```

## Ry(q: QuBit, phi: float) -> None
`NOT gate`. Inplementes a rotation aroud y-axis of $\pi$ radians.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
e^{-i\frac\phi2} & 0\\
0 & e^{i\frac\phi2}
\end{pmatrix}
```

## R1(q: QuBit, phi: float) -> None
`NOT gate`. Invert the state |0> and |1> of the QuiBit q.

- q: the qubit manipulated by the gate. This function is in-place.

- matrix:
```math
\begin{pmatrix}
1 & 0\\
0 & e^{i\frac\phi2}
\end{pmatrix}
```

## CNOT(q: MuBit, n1: int, n2: int) -> None
`X-controlled gate`. Invert the state |0> and |1> of the QuiBit in n2 if the state of the QuBit in n1 is 1.

- q: the qubit manipulated by the gate. This function is in-place.
- n1: the first QuBit to manipualte.
- n2: the second QuBit to manipulate

- matrix:
```math
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0
\end{pmatrix}
```

## SWAP(q: MuBit, n1: int, n2: int) -> None
`NOT gate`. Invert the state |0> and |1> of the QuiBit q.

- q: the qubit manipulated by the gate. This function is in-place.
- n1: the first QuBit to manipualte.
- n2: the second QuBit to manipulate

- matrix:
```math
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
```

## Cu(q: MuBit, u: list[list[float]], n1: int, n2: int) -> None
`controlled-u gate`. Applies the gate u to the QuBit in n2 if the Qubit in n1 is 1.

- q: the qubit manipulated by the gate. This function is in-place.
- the list respresentation of a matrix of the size 2 by 2.
- n1: the first QuBit to manipualte.
- n2: the second QuBit to manipulate

- matrix:
```math
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & u_{00} & u_{01}\\
0 & 0 & u_{10} & u_{11}
\end{pmatrix}
```
