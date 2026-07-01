from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.h(1)
qc.measure([0, 1], [0, 1])

counts = AerSimulator().run(qc, shots=1000).result().get_counts()
print(counts)   # ~ {'00': 250, '01': 250, '10': 250, '11': 250}