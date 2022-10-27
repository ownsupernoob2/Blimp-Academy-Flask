from qiskit import QuantumCircuit

from models.circuit import Circuit


def qiskit_circuit_from_circuit(circuit: Circuit):
    qc = QuantumCircuit(1)
    for gate in circuit.gates:
        if gate == "H":
            qc.h(0)
        elif gate == "X":
            qc.x(0)
        elif gate == "I":
            qc.i(0)
        else:
            raise ValueError("Gate unknown!")
    return qc
