# Quantum Computing — Foundations Recap
### Lessons 1–6, the way you learned them

The whole spine in one line: **qubit → measurement → gates → two qubits → entanglement → building it.**

---

## Lesson 1 — What a qubit is
A classical bit is 0 or 1. A **qubit** can be a blend of both — that blend is **superposition**.

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

- α, β are **amplitudes** — the "how much |0⟩ / how much |1⟩" of the qubit.
- **The one rule:** $|\alpha|^2 + |\beta|^2 = 1$ (squares sum to 1).

**The trap you beat:** ½|0⟩ + ½|1⟩ is *invalid* — ¼ + ¼ = ½, not 1. It's the **squares** that must sum to 1, not the amplitudes.

Famous state: $|+\rangle = \tfrac{1}{\sqrt2}|0\rangle + \tfrac{1}{\sqrt2}|1\rangle$ (equal blend).

---

## Lesson 2 — Measurement
You can't read α and β directly. You can only **measure**, and measuring is destructive.

- Outcome `0` with probability $|\alpha|^2$; outcome `1` with probability $|\beta|^2$. *(This is why squares sum to 1 — they're the odds.)*
- **Collapse:** the instant you measure, the blend is destroyed. Get `0`, and the qubit *becomes* |0⟩. Measure again → `0` forever.
- One shot = one bit + blend gone. To learn the odds, prepare fresh and measure many times (**shots**).

**Worked example you did:** $\tfrac35|0\rangle + \tfrac45|1\rangle$ → 9/25 = 36% zeros, 16/25 = 64% ones. Measure once, get `0`, measure again → still `0` (collapsed).

---

## Lesson 3 — Gates
A gate moves a qubit to a new state. Two to know:

- **X (flip / NOT):** swaps |0⟩ and |1⟩. On a blend, swaps the two amplitudes.
- **H (Hadamard / blend-maker):** turns a definite state into an equal superposition. $H|0\rangle = |+\rangle$. This is the gate that *creates* superposition.

**Every gate is reversible** (unlike classical AND/OR — no info lost until you measure).

**The big idea — interference:** apply H twice → back to |0⟩ (prints `{'0': 1000}`). The paths to `1` carry opposite signs and **cancel**; paths to `0` **reinforce**. Randomness can't be undone; a superposition can — because amplitudes have signs, and signs cancel. *Every quantum speedup is engineered interference.*

**The trap you beat:** X|+⟩ = |+⟩ (unchanged) — swapping two *equal* amplitudes does nothing.

---

## Lesson 4 — Two qubits
Two qubits → **four** basis states: |00⟩, |01⟩, |10⟩, |11⟩ (left symbol = qubit A, right = qubit B).

$$|\psi\rangle = c_{00}|00\rangle + c_{01}|01\rangle + c_{10}|10\rangle + c_{11}|11\rangle, \qquad \sum |c|^2 = 1$$

- **Tensor product (⊗):** glue two qubits by multiplying every amplitude by every amplitude.
- **The power:** each qubit doubles the amplitude count — n qubits = 2ⁿ amplitudes, all processed at once.
- **The catch:** measuring n qubits still gives only n bits (one random bitstring). Algorithms use interference so the bitstring you get is the answer.

**Example you did:** put H on both qubits of |00⟩ → |++⟩ = ½(|00⟩+|01⟩+|10⟩+|11⟩), all four outcomes ~25% each.

---

## Lesson 5 — Entanglement
**The magic coins:** two coins that always land the *same* way. Separate them by any distance — look at one, and you instantly know the other, for certain. That linkage is entanglement.

**Bell state:**
$$\tfrac{1}{\sqrt2}|00\rangle + \tfrac{1}{\sqrt2}|11\rangle$$

- Read it as a **list of allowed outcomes**: only both-0 or both-1. No |01⟩, no |10⟩ → the qubits **never disagree**.
- Measure one → the other snaps to a definite value instantly. (No faster-than-light *messaging*, but the correlation is real. Nobel Prize 2022.)
- **Entangled = can't be split** into (qubit A) ⊗ (qubit B). Independent states factor; entangled ones refuse.

**How to spot it:** read which joint outcomes are in the state. Locked into a pattern (all agree / all disagree) = entangled. $\tfrac{1}{\sqrt2}(|01\rangle+|10\rangle)$ = "always opposite" = also entangled.

---

## Lesson 6 — CNOT + building the Bell state
**CNOT** = a quantum if-statement on two qubits (one **control**, one **target**):

> If control = 1, flip the target. If control = 0, do nothing.

| Input | Output |
|:---:|:---:|
| \|00⟩ | \|00⟩ |
| \|01⟩ | \|01⟩ |
| \|10⟩ | \|11⟩ |
| \|11⟩ | \|10⟩ |

**Build the Bell state (the #1 two-gate combo in quantum computing):**

1. **H** on the left qubit: |00⟩ → ½√2 (|00⟩ + |10⟩) — left is a blend, not linked yet.
2. **CNOT** (control = left, target = right): the 0-term does nothing, the 1-term flips → $\tfrac{1}{\sqrt2}(|00\rangle + |11\rangle)$. **Linked.**

Recipe in one breath: **H on one qubit, then CNOT onto the other.**

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)                    # blend
qc.cx(0, 1)                # link (cx = CNOT)
qc.measure([0, 1], [0, 1])

counts = AerSimulator().run(qc, shots=1000).result().get_counts()
print(counts)              # ~ {'00': 500, '11': 500} — only agreements, never 01 or 10
```

Seeing only `00` and `11` (never `01`/`10`) *is* entanglement in hard data.

---

## The whole toolkit you now own
| Piece | What it does |
|---|---|
| **Qubit** | α\|0⟩ + β\|1⟩, with \|α\|² + \|β\|² = 1 |
| **Measurement** | random bit (odds = squared amplitudes), then collapse |
| **X** | flip 0 ↔ 1 |
| **H** | make (and un-make) superposition; source of interference |
| **Tensor product** | combine qubits; n qubits → 2ⁿ amplitudes |
| **CNOT** | quantum if-statement; links two qubits |
| **Entanglement** | magic coins — measuring one determines the other |

**Next step:** quantum teleportation — uses this exact Bell state to "send" a qubit's state across a distance. You already have every piece it needs.