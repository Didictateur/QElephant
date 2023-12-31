# QElephant

QElephant is a small library without pretention. It simulates the behavior of a quantum computer. The syntaxe is simple and can be used in any code in Python.

## Installation
You can install the latest version of QElephant with :

```
pip install QElephant
```

## Dependencies

In order to work, QElephant is using the following libraries:
- `math`
- `random`
- `numpy`

They are automatically managed when installing QElephant.

## Contains
This library contains three main object : `QuBit`, `Matrix` and `Circuit`.

### QuBit
This is the specificity of a quantum algorithm: using QuBit which can have two states: `|0>` and `|1>`. To create one, simply use:

```
q = QuBit(alpha, beta)
```
$\alpha$ and $\beta$ are optional complex arguments. When specified, initiate the QuBit in the state $\alpha$ |0> + $\beta$ |1>.

> [!IMPORTANT]
> Because the value of $\alpha$ and $\beta$ gives the probability of each states, it is essential that $|\alpha|²+|\beta|²=1$. On the other case, the QuBit cannot be created.

To simulate entangled QuBit, `MuBit` are used. As for `QuBit`, they are initalized like this:

```
mq = MuBit(n)
q = mq[0]
```

`n` gives the number of entangled QuBit. When created, a MuBit is in the state with only zeros.

`mq[0]` returns a QuBit, here the first one, wich can be manipulated. Because of the intrication, manipulating a entangled QuBit implies that other QuBits are manipulated too.

### Matrix
`Matrix` are used to manipulate the state of the QuBit. For example, the QuBit 

$\alpha$ |0> + $\beta$ |1> 

is represented by 

```math
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
```

So, the operation corresponding of the inversion of the value of $\alpha$ and $\beta$ is

```math
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
\times
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
=\begin{pmatrix}
\beta\\
\alpha
\end{pmatrix}
```

In theory, the users don't need to use them, the main quantum gates are already implemented.

### Circuit

A `Circuit` is an object contaning a MuBit. When manipulating it, it send to the `Circuit` a signal in order to keep in memory when a gate is used, and on which QuBit.

So, it is simply used like a `MuBit` :
```
# a Circuit with 3  entangled SuBit is created
c = Circuit(3)

# get the MuBit in this circuit
mb = c.get_MuBit()

# manipulate le MuBit
List_of_QuBit = [mb[i] for i in range(3)]
```

### Quantum Gate

The quantum gates are the different operations applying to the QuBits. The one behind is the gate `X`. It is simply used like any function:

```
# a QuBit is created
q = QuBit() 

# the values of the QuBit are inverted
X(q)

# q is now in the state 0 |0> + 1 |1>
```

the complete list can be find in the [docs](docs).

Some gates need a `MuBit` in entry. This is the case for the controlled gate. In such a case, multiple QuBit are manipulated at the same time. The following QuBit must be specified:

```
mq = Mubit(2)
# in the state |00>

X(mq[0])
# now in the state |10>

SWAP(mq, 0, 1)
# the two first quibit are inverted, mq is finally in the state |01>
```

Finally, a gate can be simply apply on all the `QuBit` of a `MuBit`:
```
mb1 = MuBit(7)
mb2 = MuBit(7)

H(mb2)

for i in range(7):
    H(mb2[i])

# at the end, the two MuBit are in the exact same state
```

> [!NOTE]
> Only a single qubit gate can be apply to all the `QuBit` at the same time.
> For a `Circuit`, maust be apply to the `QuBit`, and not to the circuit

## Docs

A doc is availaibale [here](docs) where all objects and gates are displayed.


## Others

> [!WARNING]
> Because this library is only a simulation of a qantum computer, lot of calculation are made. Manipulating n entangled qubits means manipulating matrices of size 2^n. So, it demandes much more time to calculate than a real qantum computer.
