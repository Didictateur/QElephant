## Matrix

Matrix(l: list[list[complexe]])

- l: representation of the matrix in a list

### Attributes

- ```__m: list[list[complexe]]```

  the values contained in the matrix.

- ```__size: tuple[int, int]```

  the size of the matrix

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
\frac1\sqrt 2 & \frac1\sqrt 2\\
\frax1\sqrt 2 & -\frac1\sqrt 2
\end{pmatrix}
```
