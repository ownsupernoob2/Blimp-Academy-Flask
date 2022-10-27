function attach_submit_button(question_id){
    $(".submit-button").click(function(){

        // Read the choice from the radio button
        let choice = $("input[name='answer']:checked").val()
        let url = "/quiz/" + question_id + "/verify/"
        let data = {"answer": choice}

        // Disable radio buttons
        $(".radio-button").prop("disabled", true)

        // Disable submit button
        $(".submit-button").prop("disabled", true)

        $.ajax({
            type: "POST",
            url: url,
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data),
            success: function(result){
                let right_choice = $("input[value="+result.correct_answer+"]").parent()
                right_choice.addClass("right-answer")

                if (result.answer_right){
                    let correct_span = $("<span>Correct!</span>")
                    correct_span.addClass("pos-feedback")



                    let correct_answer_span = $("<span>"+result.correct_answer+"</span>")
                    correct_answer_span.addClass("pos-feedback")
                    $(".result").html(correct_span[0].outerHTML +
                        " The correct answer is " + correct_answer_span[0].outerHTML)

                } else {
                    let wrong_choice = $("input[name='answer']:checked").parent()
                    wrong_choice.addClass("wrong-answer")

                    let correct_answer_span = $("<span>")
                    correct_answer_span.addClass("pos-feedback")
                    correct_answer_span.html(result.correct_answer)

                    let incorrect_span = $("<span>Incorrect.</span>")
                    incorrect_span.addClass("neg-feedback")
                    $(".result").html(incorrect_span[0].outerHTML +
                        " The correct answer is " + correct_answer_span[0].outerHTML)
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

function enable_submit_button_on_selection(){
    $("input[name='answer']").click(function(){
        console.log("selected")
        $(".submit-button").prop("disabled", false)
    })
}

function setup_page_multiple_choice_quiz(quiz_data) {
    /*let quiz_next_button = document.querySelector(".quiz_next_button");*/

    console.log(quiz_data)
    attach_submit_button(quiz_data.question_id)
    add_gates(quiz_data.name_media.gates, $(".gate-slots"), false)
    if(quiz_data.multiple_choice.answers_type == "circuit"){
        
        $.each(quiz_data.multiple_choice.answers_media, function(idx, el){
            console.log(el)
            add_gates(el.gates, $("#gate-slots-"+idx), false)
        })
    }
    enable_submit_button_on_selection()
    $(".submit-button").prop("disabled", true)
            // Disable submit button
    $(".quiz-next-button").prop("disabled", true)

    /*quiz-next-button.disabled = true;*/



    
}

function setup_multiple_choice_answers(quiz_data){
    
}