from flask import Flask, send_from_directory
from flask import render_template
from flask import Response, request, jsonify
import json
import copy
import ai_writer
import re

from matplotlib import pyplot
from qiskit.quantum_info import Statevector

from quantum_circuit import qiskit_circuit_from_circuit
from generate_home_data import home_data
from models.quiz_data import MultipleChoiceAnswer, QuizQuestion
from models.circuit import Circuit
from models.learn_data import LearnData
import generate_quiz_data
from generate_bloch_sphere import generate_bloch_sphere_from_circuit
from generate_learn_data import generate_learn_data
from models.bloch_sphere_update import BlochSphereUpdate
#from generate_result_data import quiz_result_data, re_initialize_result_data
from generate_quiz_data import total_questions, generate_quiz_data
from generate_quiz_landing_data import quiz_landing_data
from models.quiz_results import QuizResultData

import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

learn_data = generate_learn_data()
quiz_data = generate_quiz_data()
quiz_result_data = QuizResultData(total_questions=5, results=[0 for _ in range(5)])

# ========== JSON routes ===================
@app.route("/get_data/<data_type>", methods=["GET","POST"])
def getData(data_type):
    print(data_type)
    if data_type == "learn":
        global learn_data
        learn_data = generate_learn_data()
        return ('', 204)
    elif data_type == "quiz":
        global quiz_data
        quiz_data = generate_quiz_data()
        return ('', 204)


@app.route("/quiz/<question_id>/verify/", methods=["POST"])
def verify_answer(question_id=None):

    global quiz_result_data
    json_data = request.get_json()

    question: QuizQuestion = quiz_data[question_id]
    if question.is_multiple_choice:
        multiple_choice_answer = MultipleChoiceAnswer.parse_obj(json_data)
        correct = False
        if multiple_choice_answer.answer == question.multiple_choice.correct:
            quiz_result_data.results[int(question_id)-1] = 1
            quiz_result_data.correct = sum(quiz_result_data.results)
            correct = True
        return jsonify({
            "answer_right": correct,
            "correct_answer": question.multiple_choice.correct
        })
    elif question.is_circuit_draw:
        answer_circuit = Circuit.parse_obj(json_data)
        correct = False

        answer_statevector = Statevector.from_instruction(
            qiskit_circuit_from_circuit(answer_circuit)
        )
        correct_statevector = Statevector.from_instruction(
            qiskit_circuit_from_circuit(question.circuit_draw.correct)
        )

        if answer_statevector == correct_statevector:
            print("Question id = ", question_id)
            quiz_result_data.results[int(question_id)-1] = 1
            quiz_result_data.correct = sum(quiz_result_data.results)
            correct = True
        return jsonify({
            "answer_right": correct,
            "correct_answer": question.circuit_draw.correct.dict()
        })
    else:
        raise ValueError("Not multiple choice or circuit draw question!")


@app.route("/quiz/")
def display_quiz_landing_page():
    global quiz_result_data
    quiz_result_data = QuizResultData(total_questions=5, results=[0 for _ in range(5)])
    return render_template("quiz_landing.html", data=json.loads(quiz_landing_data.json()))

@app.route("/quiz/<quiz_id>")
def display_quiz_question(quiz_id=None):
    
    model = quiz_data[quiz_id]

    if model.is_multiple_choice:
        letters = ['A', 'B', 'C', 'D']
        return render_template("quiz_multiple_choice.html", quiz_data=json.loads(model.json()), options=letters)
    else: 
        return render_template("quiz_create_circuit.html", quiz_data=json.loads(model.json()))

@app.route("/quiz_result")
def display_quiz_result():
    global home_data
    home_data.complete_sections = 3  # If we are rendering this page, then they finished the quiz
    return render_template("quiz_result.html", data=json.loads(quiz_result_data.json()))


@app.route("/learn/<learn_id>/circuit", methods=["POST"])
def update_learn_circuit(learn_id=None):
    global learn_data

    data: LearnData = learn_data[learn_id]
    new_gates = request.get_json()
    data.media.learn_circuit.gates = new_gates
    plot = generate_bloch_sphere_from_circuit(data.media.learn_circuit)
    plot.savefig(data.media.bloch_sphere, format="png", transparent=True)
    pyplot.close(plot)

    model = BlochSphereUpdate(
        bloch_sphere=data.media.bloch_sphere
    )
    return model.json()

@app.route("/quiz/<question_id>/circuit", methods=["POST"])
def update_quiz_circuit(question_id=None):
    global quiz_data

    qq: QuizQuestion = quiz_data[question_id]
    new_gates = request.get_json()
    qq.circuit_draw.start.gates = new_gates
    plot = generate_bloch_sphere_from_circuit(qq.circuit_draw.start)
    if qq.bloch_sphere is not None:
        plot.savefig(qq.bloch_sphere, format="png", transparent=True)
        pyplot.close(plot)

    model = BlochSphereUpdate(
        bloch_sphere=qq.bloch_sphere
    )
    return model.json()

@app.route("/home/circuit", methods=["POST"])
def home_circuit():
    global home_data
    new_gates = request.get_json()
    home_data.media.learn_circuit.gates = new_gates
    plot = generate_bloch_sphere_from_circuit(home_data.media.learn_circuit)
    plot.savefig(home_data.media.bloch_sphere, format="png", transparent=True)
    pyplot.close(plot)

    return home_data.json()


@app.route("/section_complete/<section>", methods=["POST"])
def update_section_complete(section):
    global home_data
    home_data.complete_sections = max(home_data.complete_sections, int(section))
    return ("", 204)

# @app.route("/static/<path>")
# def static_dir(path):
#     return send_from_directory("static", path)


# ========== HTML routes ===================
@app.route("/learn/<learn_id>", methods=["GET", "POST"])
def display_learn(learn_id=None):
    model = learn_data[learn_id]
    global var_product_desc
    global var_seller_info
    global var_focus_segment

    if request.method == 'POST':
        if 'form1' in request.form:
            print(request.form)
            var_product_desc = request.form['productIdea']

            ai_response = ai_writer.product_observation(var_product_desc)
            print(ai_response)

            model.response = re.sub(r'^.*?AI:', 'RecoBot:', ai_response)
            model.response_title = "My Understanding About Your Product"
            #model.response = ai_response.replace('AI:', '<b>RecoBot:</b>')
            #model.response = ai_response.replace('\n', '<br>')

        if 'form2' in request.form:
            print(request.form)
            var_seller_info = request.form['sellerInfo']

            ai_response = ai_writer.segment_generator(var_product_desc, var_seller_info)
            print(ai_response)

            model.response = re.sub(r'^.*?AI:', 'RecoBot:', ai_response)
            model.response_title = "My Understanding About Your Product"

        if 'form3' in request.form:
            print(request.form)
            var_focus_segment = request.form['focusSegment']

            ai_response = ai_writer.segment_selector(var_product_desc, var_seller_info, var_focus_segment)
            print(ai_response)

            model.response = re.sub(r'^.*?AI:', 'RecoBot:', ai_response)
            model.response_title = "Focus Segment Insight"
    if isinstance(model.media, list):
        return render_template("bloch_learn_page.html", learn_data=json.loads(model.json()))
    else:
        return render_template("circuit_learn_page.html", learn_data=json.loads(model.json()))

@app.route("/")
def home():
   return render_template("home.html", home_data=json.loads(home_data.json()))

if __name__ == '__main__':
   app.run(debug=True)




