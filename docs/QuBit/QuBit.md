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

- ```__init__(alpha: complexe=1, beta: complexe=0) -> None```

  initiates the qubit

- ```is_intricated() -> bool```

  returns the value of __intricated

- ```get_MuBit() -> None```

  returns the MuBit in wich the QuBit is intricated. If not intricated, rerurns None

- ```__str__() -> str```

  returns a string representation of the list of __state

- ```__apply(m: Matrix) -> None```

  takes a Matrix and modifies the QuBit according the matrix

- ```observe() -> list[int]```

  forces the QuBit in a state, where the probabilities are given throught __state. Returns the new __state obtained.


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
