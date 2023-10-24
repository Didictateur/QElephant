## IQuBit

IQuBit(n: int, mb: MuBit)

IQuBit(QuBit)

- n: the position of the QuBit in the list of intricated QuBits
- mb: the MuBit which organises the intricated QuBit 

### Attributes

- ```__n: int```

  the position of the QuBit in the list of intricated QuBits

- ```__Mubit: MuBit```
 the MuBit which organises the intricated QuBit

- ```__intricated: bool```

  tells if the QuBit is intricated or not
  

### Methode

- ```__init__(n: int, mb: MuBit) -> None```

  initiates the qubit

- ```is_intricated() -> bool```

  returns the value of __intricated

- ```get_MuBit() -> MuBit```

  returns the MuBit in wich the QuBit is intricated.

- ```__str__() -> str```

  returns a string representation of the list of __state

- ```__apply(m: Matrix) -> None```

  takes a Matrix and modifies the QuBit according the matrix

- ```observe() -> list[int]```

  forces the QuBit in a state, where the probabilities are given throught __state. Returns the new __state obtained.

- ```reset() -> None```

  fixes the QuBit in the state |0>. This is irrevesible.