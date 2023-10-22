## Matrix

Matrix(l: list[list[complexe]])

- l: representation of the matrix in a list

### Attributes

- ```__m: list[list[complexe]]```

  the values contained in the matrix.

- ```__size: tuple[int, int]```

  the size of the matrix

### Methodes

- __init__(self, l: list[list[complex]]=[]) -> None

  initiates the matrix

- __mul__(self, __value: "Matrix") -> Matrix

  defines the natural multiplication as the Koeneger product for matrices

- __apply(self, x: list[complex]) -> list[complex]

  takes a list to represent a vector in a colonne, and return the proctuct of the matrix by this vector
