import pathlib
from qiskit.visualization import plot_bloch_vector
from matplotlib import pyplot

from models.learn_data import GateLearnData
from models.home_data import HomeData
from models.circuit import LearnCircuit


bloch_sphere_0 = plot_bloch_vector([0, 0, 1])
fname = pathlib.Path(f"static/images/home/home.png")
fname=pathlib.Path(str(pathlib.Path(__file__).parent)+"/static/images/home/home.png")
bloch_sphere_0.savefig(fname, format="png", transparent=True)
pyplot.close(bloch_sphere_0)

home_data = HomeData(
    title="Meet Recobot!",
    text="RecoBot is a doting and helpful Artificial assistant, built with the purpose of helping you reach your buyers by giving you practical advice on placement, customer segments, and more. "
         "Simply click ‘START’ to launch a conversation with RecoBot, and launch your business with a bang!",
    media=GateLearnData(
        learn_circuit=LearnCircuit(
            gates=["X"],
            learn_circuit_id="home",
        ),
        bloch_sphere=fname,
    ),
)

