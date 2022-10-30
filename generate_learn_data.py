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
        progression=1,
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
            """<button type = \"submit\" id = \"productIdeaButton\" class =\"btn btn-primary\" > Tell about the product </button>""",
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
        progression=2,
        alias="",
        title="More About the Seller",
        response_title="",
        text=[],
        question=[
            """<label for =\"sellerInfo\" class =\"form-label\">  <b>RecoBot:</b> <b>Recobot:</b> Interesting! Now, tell me some more details about the seller of the product. </label>""",
            """<input type = \"text\" class =\"form-control\" id=\"sellerInfo\" name=\"sellerInfo\" placeholder=\"Enter some key information about you, the seller\" >""",
            """<input type = \"hidden\" name = \"form2\" value = \"form2\">""",
            """<button type = \"submit\" id = \"sellerInfoButton\" class =\"btn btn-primary\" > Tell about the seller </button>""",
        ],
        response="",
        media=captioned_spheres,
        prev_page="/learn/1",
        prev_name="Previous",
        next_page="/learn/3",
        next_name="Picking Your Segment"
    )

    global learn3

    learn3 = LearnData(
        learn_id="3",
        progression=3,
        alias="",
        title="Picking Your Segment",
        response_title="",
        text=["""Please type in the type of customer you want to sell to :""",
              ],
        question=["""<b>RecoBot:</b> Alright - based on your motives and product, \
          Please pick a segment you want to focus on!""",
          """<input type = \"text\" class =\"form-control\" id=\"focusSegment\" name=\"focusSegment\" placeholder=\"Enter the desired focus segment\" >""",
          """<input type = \"hidden\" name = \"form3\" value = \"form3\">""",
          """<button type = \"submit\" id = \"focusSegmentButton\" class =\"btn btn-primary\" > Select Focus Segment     </button>""",

        ],
        response="",
        media=captioned_spheres,
        prev_page="/learn/2",
        prev_name="Previous",
        next_page="/learn/4",
        next_name="Picking Your Differentiator"
    )

    global learn4

    learn4 = LearnData(
        learn_id="4",
        progression=4,
        alias="",
        title="Picking Your Differentiator",
        response_title="",
        text=[ ],
        question=["""<b>RecoBot:</b> Now let's learn about what makes your product unique. \
              Please elaborate!""",
                  """<input type = \"text\" class =\"form-control\" id=\"productDifferentiator\" name=\"productDifferentiator\" placeholder=\"Enter the your product differentiator\" >""",
                  """<input type = \"hidden\" name = \"form4\" value = \"form4\">""",
                  """<button type = \"submit\" id = \"productDifferentiatorButton\" class =\"btn btn-primary\" > Predict the Price </button>""",

                  ],
        response="",
        media=captioned_spheres,
        prev_page="/learn/3",
        prev_name="Previous",
        next_page="/learn/5",
        next_name="Predict the Price"
    )


    empty_circuit = QuantumCircuit(1)
    sv = Statevector.from_instruction(empty_circuit)
    bloch_sphere_0 = plot_bloch_multivector(sv)

    pyplot.close(bloch_sphere_0)

    global learn_data
    learn_data = [
        learn1,
        learn2,
        learn3,
        learn4,
    ]

    learn_data = {
        k.learn_id: k for k in learn_data
    }

    return learn_data