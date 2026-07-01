from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)          # |0> -> |+>   : now a 50/50 superposition
qc.h(0)          # |+> -> |0>   : back to certainty
qc.measure(0, 0)

counts = AerSimulator().run(qc, shots=1000).result().get_counts()
print(counts)    # ~ {'0': 1000} — all zeros