## QuBit

QuBit(alpha: complexe, beta: complexe)

- alpha: complexe value for |0>
- beta: complexe value for |1>

### Attributes

- ```__state: list[complexe]```

  list of the values for the state |0> and |1>

- ```__intricated: bool```

  tells if the qubit is intricated or not

### Methode

- ```__init__(l: list[list[complex]]=[]) -> None```

  initiates the matrix

- ```__mul__(__value: "Matrix") -> Matrix```

  defines the natural multiplication as the Koeneger product for matrices

- ```__apply(x: list[complex]) -> list[complex]```

  takes a list to represent a vector in a colonne, and return the proctuct of the matrix by this vector

- ```__str__() -> str```

  returns a string representation of the matrix


### Staticmethods

- ```I() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}
```

- ```H() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
\frac {1} {\sqrt 2} & \frac {1} {\sqrt 2}\\
\frac {1} {\sqrt 2} & -\frac{1} {\sqrt 2}
\end{pmatrix}
```

- ```X() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
```

- ```Y() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
0 & -i\\
i & 0
\end{pmatrix}
```

- ```Z() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}
```

- ```S() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & 0\\
0 & i
\end{pmatrix}
```

- ```T() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & 0\\
0 & e^{i\frac {\pi} {4}}
\end{pmatrix}
```

- ```Rx(phi: float) -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
\cos(\frac \phi 2) & -i\sin(\frac \phi 2)\\
-i\sin(\frac \phi 2) & \cos(\frac \phi 2)
\end{pmatrix}
```

- ```Ry(phi: float) -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
\cos(\frac \phi 2) & -\sin(\frac \phi 2)\\
\sin(\frac \phi 2) & \cos(\frac \phi 2)
\end{pmatrix}
```

- ```Rz(phi: float) -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
e^{-i\frac \phi 2} & 0\\
0 & e^{i\frac \phi 2}
\end{pmatrix}
```

- ```R1(phi: float) -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & p\\
0 & e^{i\phi}
\end{pmatrix}
```

- ```CNOT() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0
\end{pmatrix}
```

- ```SWAP() -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 0
\end{pmatrix}
```

- ```Cu(u: Matrix) -> Matrix```

  returns the matrix

```math
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & u_{00} & u_{01}\\
0 & 0 & u_{10} & u_{11}
\end{pmatrix}
```
