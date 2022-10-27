
function generate_tiny_circuit(gates){

    let circuit_container = $("<div class='circuit-container tiny-circuit-container'>")
    let circuit_line = $("<div class='circuit-line tiny-circuit-line'>")
    let gate_slots = $("<ul class='gate-slots'>")
    let measure = $("<img src='/static/images/measure.png' class='measure tiny-measure'>")

    // Compose these together
    circuit_container.append(circuit_line)
    circuit_container.append(gate_slots)
    circuit_container.append(measure)

    // Add gates onto circuit
    add_gates(gates, gate_slots, false)

    // Make gates tiny
    gate_slots.find("li").each(function() {
        $(this).addClass("tiny-gate")
    })
    return circuit_container
}


function attach_submit_button(question_id){
    $(".submit-button").click(function(){

        // Read the choice from the radio button
        let gate_slots = $(".gate-slots")
        let gates_list = get_gates_list(gate_slots)
        let data = {"gates": gates_list}
        let url = "/quiz/" + question_id + "/verify/"

        // Disable submit button
        $(".submit-button").prop("disabled", true)

        $.ajax({
            type: "POST",
            url: url,
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data),
            success: function(result){
                if (result.answer_right){
                    $(".result").text("Correct!")
                    $(".result").addClass("pos-feedback")
                } else {

                    let feedback_div = $("<div>")
                    let incorrect_span = $("<span>Incorrect.</span>")
                    incorrect_span.addClass("neg-feedback")

                    console.log(result.correct_answer)
                    feedback_div.html(incorrect_span[0].outerHTML +
                        " The correct answer is")

                    let correct_circuit = generate_tiny_circuit(result.correct_answer.gates)

                    $(".result").append(feedback_div)
                    $(".result").append(correct_circuit)
                }

                $(".quiz-next-button").prop("disabled", false)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    })
}

function setup_page_circuit_quiz(quiz_data) {
    update_data("quiz")
    // add_gates(learn_data["media"]["learn_circuit"]["gates"], $(".gate-slots"))
    console.log(quiz_data["bloch_sphere"])
    add_bloch_sphere("/" + quiz_data["bloch_sphere"], $(".bloch-image"))
    generate_tray()

    let bloch_update_url = "/quiz/" + quiz_data["question_id"] + "/circuit"
    console.log(bloch_update_url)
    make_gate_slots_sortable(bloch_update_url)

    droppable_trash(bloch_update_url) 

    attach_submit_button(quiz_data.question_id)

    $(".quiz-next-button").prop("disabled", true)
}
