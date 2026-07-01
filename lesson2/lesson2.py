from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

theta = 2 * np.arccos(3/5)   # ≈ 1.855 rad

qc = QuantumCircuit(1, 1)
##qc.h(0)              # the H gate builds |+> = (|0>+|1>)/√2 — we dissect H in Lesson 3
qc.ry(theta, 0) 
qc.measure(0, 0)     # collapse it, record the classical bit

sim = AerSimulator()
counts = sim.run(qc, shots=1000).result().get_counts()
print(counts)        # ~ {'0': 500, '1': 500}, jittering each run