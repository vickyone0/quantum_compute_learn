from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)                    # Step 1: left qubit -> blend
qc.cx(0, 1)                # Step 2: CNOT, control=0, target=1  (cx = CNOT)
qc.measure([0, 1], [0, 1])

counts = AerSimulator().run(qc, shots=1000).result().get_counts()
print(counts)              # ~ {'00': 500, '11': 500}
