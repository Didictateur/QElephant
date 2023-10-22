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
