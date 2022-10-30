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
        response_title="",
        text=[
            """Please tell me about the product you want to market: """,
        ],
        question=[
            """<b>RecoBot:</b> Hi there, nice to meet you! I understand your need to get your startup off the ground, and I’d be happy to help!""",
            """<label for =\"productIdea\" class =\"form-label\">  <b>RecoBot:</b> First, though, I’ll probably have to gather some information about the ideas you have for your new company. What product are you planning to sell?</label>""",
            """<input type = \"text\" class =\"form-control\" id=\"productIdea\" name=\"productIdea\" placeholder=\"Enter product idea\" >""",
            """<input type = \"hidden\" name = \"form1\" value = \"form1\">""",
            """<button type = \"submit\" id = \"productIdeaButton\" class =\"btn btn-primary\" > Submit </button>""",
        ],
        response="",
        media=captioned_spheres,
        prev_page="/",
        prev_name="Home",
        next_page="/learn/2",
        next_name="Next: About You"
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
        response_title="Product Description",
        text=["""<b>Measuring a qubit is the quantum analogue of reading a bit</b>. 
            If we measure a qubit in the 0 state, 
            then we will get 0, with probability 100%. Similarly, if we measure a qubit in the 1 state, 
            then we will get 1, with probability 100%. This is the same as a classical bit. """,
          """On the other hand, <b>if we measure a qubit that is between 0 and 1, we will get a 0 or 1 with probability 
          proportional to where the arrow is pointing</b>. For example, if the arrow is pointing at the equator,
          then the probability of measuring a 0 is 50%""", ],
        question=[
            "What topic do you want to get blog ideas on Learn 1?"
            #"<label for =\"blogTopic\" class =\"form-label\"> What topic do you want to get blog ideas on? </label>"
        ],
        response=[
            """THIS IS A DEFAULT RESPONSE """,
        ],
        media=captioned_spheres,
        prev_page="/learn/1",
        prev_name="Previous",
        next_page="/",
        next_name="Home"
    )

    empty_circuit = QuantumCircuit(1)
    sv = Statevector.from_instruction(empty_circuit)
    bloch_sphere_0 = plot_bloch_multivector(sv)

    pyplot.close(bloch_sphere_0)

    global learn_data
    learn_data = [
        learn1,
        learn2
    ]

    learn_data = {
        k.learn_id: k for k in learn_data
    }

    return learn_data