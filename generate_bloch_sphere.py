
from models.circuit import Circuit

from quantum_circuit import qiskit_circuit_from_circuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector


def generate_bloch_sphere_from_circuit(circuit: Circuit):
    """
    Returns a matplotlib figure. Save it with

    result = generate_bloch_sphere_from_circuit(circuit)
    result.savefig(out.png, format='png')
    """
    qc = qiskit_circuit_from_circuit(circuit)

    state = Statevector.from_instruction(qc)
    return plot_bloch_multivector(state)

