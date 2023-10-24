## MuBit

MuBit(n: int)

- n: number of intricated QuBits

### Attributes

- ```__n: int```

  the number of intricated QuBits represented by this MuBit

- ```__state: list[complexe]```

  list of the values for the state |0...0>, |0...01>, |0...010>, |0...011> etc...

### Methode

- ```__init__(n: int=2) -> None```

  initiates the mubit with n QuBits.

- ```get_size() -> int```

  return __n

- ```__str__() -> str```

  returns a string representation of the list of __state. Each state is named and draw in a new line.

- ```__set(i: int, value: int)```

  force the i-th QuBit of the MuBit to take the state value. Value must be 0 or 1.

- ```__iter__() -> Iterator[IQuBit]```

  creates an interator of __state.

- ```__getitem__(item: int) -> IQubIt```

  creates an intricated QuBit corresponding to the item-th QuBit.

- ```__apply(matrix: Matrix, i: int) -> None```

  takes a Matrix of size (2, 2) and modifies the i-th QuBits according the matrix.

- ```__mapply(matrix: Matrix, i: int) -> None```

  takes a Matrix aof size (4, 4) and modifies the i-th QuBit and le next one together according the matrix.

- ```__getProbs(i: int) -> float```

  returns the probability to get the i-th QuBit in the state |0>.

- ```__SWITCH(i: int) -> None```

  switches the i-th QuBit with the next one in __state.

- ```observe() -> list[int]```

  forces the QuBits in a state, where the probabilities are given throught __state. Returns the list of the state of each QuBit.

### Staticmethods

- ```intricateThem(*args: QuBit) -> MuBit```

  returns a new QuBit, independent of the args, but corresponding to the intrication of all given QuBits 