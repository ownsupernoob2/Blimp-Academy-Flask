import pathlib
from qiskit.visualization import plot_bloch_vector
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from matplotlib import pyplot

from qiskit.visualization import plot_bloch_multivector
from models.learn_data import LearnData, CaptionedBlochSphere, GateLearnData
from models.circuit import Circuit, LearnCircuit

total_pages = 7
total_qubits_pages = 2
total_programming_pages = 5


def generate_learn_data():
    learn1_sphere_coords=[
        ([0, 0, 1], "A qubit in the 0 state"),
        ([0, 0, -1], "A qubit in the 1 state"),
        ([1, 0, 0], "A qubit halfway between 0 and 1")
    ]
    captioned_spheres = []
    for num, tup in enumerate(learn1_sphere_coords):
        learn1_img = plot_bloch_vector(tup[0])
        fname = pathlib.Path(f"static/images/learn1_media_{num}.png")
        fname = pathlib.Path(str(pathlib.Path(__file__).parent) + "/static/images/learn1_media_{num}.png")
        learn1_img.savefig(fname, format="png", transparent=True)
        pyplot.close(learn1_img)
        captioned_spheres.append(CaptionedBlochSphere(
            bloch_sphere=fname,
            caption=tup[1]
        ))
    global learn1
    learn1 = LearnData(
        learn_id="1",
        progression=1/total_qubits_pages,
        alias="Product",
        title="Product",
        text=[
            """Please tell me about the product you want to market: """,
        ],
        media=captioned_spheres,
        prev_page="/",
        prev_name="Home",
        next_page="/learn/2",
        next_name="Next: Seller"
    )

    learn2_sphere_coords=[
        ([0, 0, 1], "Measure 0, 100% of the time"),
        ([0, 0, -1], "Measure 0, 0% of the time"),
        ([1, 0, 0], "Measure 0, 50% of the time")
    ]
    captioned_spheres = []
    for num, tup in enumerate(learn2_sphere_coords):
        learn2_img = plot_bloch_vector(tup[0])
        fname = pathlib.Path(f"static/images/learn2_media_{num}.png")
        fname = pathlib.Path(str(pathlib.Path(__file__).parent) + "/static/images/learn2_media_{num}.png")
        learn2_img.savefig(fname, format="png", transparent=True)
        pyplot.close(learn2_img)
        captioned_spheres.append(CaptionedBlochSphere(
            bloch_sphere=fname,
            caption=tup[1]
        ))
    global learn2

    learn2 = LearnData(
        learn_id="2",
        progression=2/total_qubits_pages,
        alias="Bloch Sphere",
        title="Measurement",
        text=["""<b>Measuring a qubit is the quantum analogue of reading a bit</b>. 
            If we measure a qubit in the 0 state, 
            then we will get 0, with probability 100%. Similarly, if we measure a qubit in the 1 state, 
            then we will get 1, with probability 100%. This is the same as a classical bit. """,
          """On the other hand, <b>if we measure a qubit that is between 0 and 1, we will get a 0 or 1 with probability 
          proportional to where the arrow is pointing</b>. For example, if the arrow is pointing at the equator,
          then the probability of measuring a 0 is 50%""", ],
        media=captioned_spheres,
        prev_page="/learn/1",
        prev_name="Previous",
        next_page="/",
        next_name="Home"
    )

    empty_circuit = QuantumCircuit(1)
    sv = Statevector.from_instruction(empty_circuit)
    bloch_sphere_0 = plot_bloch_multivector(sv)


    # -----GATES-----
    fname = pathlib.Path(f"static/images/gate_learn/learn3.png")

    fname = pathlib.Path(str(pathlib.Path(__file__).parent) + "/static/images/learn3.png")
    bloch_sphere_0.savefig(fname, format="png", transparent=True)

    global learn3
    learn3 = LearnData(
        learn_id="3",
        progression=1/total_programming_pages,
        alias="Programming a Qubit",
        title="Programming a Qubit",
        text=["""<b>We program qubits by adding gates onto a circuit</b>. A circuit 
    always starts in the 0 state. On a circuit, gates are applied from left to right.
    """,
          """More gates than these three exist, but these are the important ones 
          that will get you started""",
        ],
        instruction="Feel free to drag and drop gates onto the circuit before continuing.",
        media=GateLearnData(
            learn_circuit=LearnCircuit(
                learn_circuit_id="learn3"
            ),
            bloch_sphere=fname,
        ),
        prev_page="/",
        prev_name="Home",
        next_page="/learn/4",
        next_name="Next: X Gate"
    )


    fname = pathlib.Path(f"static/images/gate_learn/learn4.png")

    fname = pathlib.Path(str(pathlib.Path(__file__).parent) + "/static/images/gate_learn/learn4.png")
    bloch_sphere_0.savefig(fname, format="png", transparent=True)

    global learn4
    learn4 = LearnData(
        learn_id="4",
        progression=2/total_programming_pages,
        alias="X Gate (NOT Gate)",
        title="X Gate (NOT Gate)",
        text="""The X gate {} rotates the arrow by 180 degrees about the X axis. 
        This is useful to switch a qubit from the 0 state to the 1 state (or vice versa).""",
        instruction="Drag and drop an X gate to the beginning of the circuit",
        media=GateLearnData(
            learn_circuit=LearnCircuit(
                learn_circuit_id="learn4",
            ),
            bloch_sphere=fname,
            gate="X",
        ),
        prev_page="/learn/3",
        prev_name="Previous",
        next_page="/learn/5",
        next_name="Next: I Gate"

    )

    fname = pathlib.Path(f"static/images/gate_learn/learn5.png")

    fname = pathlib.Path(str(pathlib.Path(__file__).parent) + "/static/images/gate_learn/learn5.png")
    bloch_sphere_0.savefig(fname, format="png", transparent=True)

    global learn5
    learn5 = LearnData(
        learn_id="5",
        progression=3/total_programming_pages,
        alias="I Gate (Identity Gate)",
        title="I Gate (Identity Gate)",
        text="""The I gate {} does not perform any rotations. It's like telling the qubit to wait.""",
        instruction="Add an I gate to the beginning of the circuit",
        media=GateLearnData(
            learn_circuit=LearnCircuit(
                learn_circuit_id="learn5"
            ),
            bloch_sphere=fname,
            gate="I",
        ),
        prev_page="/learn/4",
        prev_name="Previous",
        next_page="/learn/6",
        next_name="Next: H Gate"
    )

    fname = pathlib.Path(f"static/images/gate_learn/learn6.png")

    fname = pathlib.Path(str(pathlib.Path(__file__).parent) + "/static/images/gate_learn/learn6.png")
    bloch_sphere_0.savefig(fname, format="png", transparent=True)

    global learn6
    learn6 = LearnData(
        learn_id="6",
        progression=4/total_programming_pages,
        alias="H Gate",
        title="H Gate (Hadamard Gate)",
        text="""The H gate {} rotates the arrow 180 degrees about the axis 45 degrees above the X-axis. This gate is 
        useful for switching a qubit to halfway between 0 and 1.""",
        instruction="Add an H gate to the beginning of the circuit",
        media=GateLearnData(
            learn_circuit=LearnCircuit(
                learn_circuit_id="learn6"
            ),
            bloch_sphere=fname,
            gate="H",
        ),
        prev_page="/learn/5",
        prev_name="Previous",
        next_page="/learn/7",
        next_name="Next: Sandbox"
    )

    fname = pathlib.Path(f"static/images/gate_learn/learn7.png")

    fname = pathlib.Path(str(pathlib.Path(__file__).parent) + "/static/images/gate_learn/learn7.png")
    bloch_sphere_0.savefig(fname, format="png", transparent=True)

    # TODO: We will want to figure out how to add the challenge later.
    global learn7
    learn7 = LearnData(
        learn_id="7",
        progression=5/total_programming_pages,
        alias="Sandbox",
        title="Sandbox",
        text="There are four possible states you can make with these gates. Can you make them all?",
        instruction="Add as many gates as you like and play with the qubit",
        media=GateLearnData(
            learn_circuit=LearnCircuit(
                learn_circuit_id="learn7"
            ),
            bloch_sphere=fname,
        ),
        prev_page="/learn/6",
        prev_name="Previous",
        next_page="/",
        next_name="Home"
    )

    pyplot.close(bloch_sphere_0)

    global learn_data
    learn_data = [
        learn1,
        learn2,
        learn3,
        learn4,
        learn5,
        learn6,
        learn7,
    ]

    learn_data = {
        k.learn_id: k for k in learn_data
    }

    return learn_data