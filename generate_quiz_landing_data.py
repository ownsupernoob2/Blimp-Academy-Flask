
import pathlib

from matplotlib import pyplot
from qiskit.visualization import plot_bloch_vector

from models.quiz_landing import QuizLanding

bloch_sphere_0 = plot_bloch_vector([0, 0, 1])
fname = pathlib.Path(f"static/images/home/home.png")
fname=pathlib.Path(str(pathlib.Path(__file__).parent)+"/static/images/home/home.png")
pathlib.Path("static/images/home")
#pathlib.Path("static/images/home").mkdir(exist_ok=True)
bloch_sphere_0.savefig(fname, format="png", transparent=True)
pyplot.close(bloch_sphere_0)

quiz_landing_data = QuizLanding(
    bloch_sphere=fname
)