// Assumes circuit_funcs has been included in layout.html

function add_gate_to_text(gate){

    let text = $(".learn_text").html()
    let span_replace = $("<span>")
    let tiny_gate = $("<li class='gate tiny-gate'>" + gate + "</li>")
    span_replace.append(tiny_gate)
    let html = span_replace.html()
    console.log(html)

    let replaced = text.replace("{}", html)
    $(".learn_text").html(replaced)

}

function provideFeedback(){
    get_gates_list(gate_slots)
}

function setup_page_circuit(learn_data) {
    update_data("learn")
    //add_gates(learn_data["media"]["learn_circuit"]["gates"], $(".gate-slots"))
    add_bloch_sphere("/" + learn_data["media"]["bloch_sphere"], $(".bloch-image"))
    generate_tray()

    let bloch_update_url = "/learn/" + learn_data["learn_id"] + "/circuit"
    make_gate_slots_sortable(bloch_update_url,  function(){

        console.log("media", learn_data.media)
        if (learn_data.media.gate == null) {
            // if there is no learn gate for this page, don't provide feedback
            return
        }

        let gates = get_gates_list($(".gate-slots"))
        console.log("abcd")
        console.log(learn_data.media.gate)
        console.log(gates)
        if ($.inArray(learn_data.media.gate, gates) == -1){
            console.log("not in the array")
            $(".feedback").addClass("neg-feedback")
            let tiny_gate_span = $("<span>")
            let tiny_gate = $("<li class='gate tiny-gate'>" + learn_data.media.gate + "</li>")
            tiny_gate.css("color", "black")
            tiny_gate_span.append(tiny_gate)

            $(".feedback").html("Oops! The " + learn_data.media.gate + " gate looks like " + tiny_gate_span.html())
        } else{
            console.log("in the array")
            $(".feedback").html("")
        }

    })

    droppable_trash(bloch_update_url)

    add_gate_to_text(learn_data["media"]["gate"])

    if (learn_data.next_page == "/"){
        // ajax call that learning has been complete
        $.ajax({
            type: "POST",
            url: "/section_complete/2",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
        })
    }
}

function setup_page_bloch(learn_data) {
    if (learn_data.next_page == "/"){
        // ajax call that learning has been complete
        $.ajax({
            type: "POST",
            url: "/section_complete/1",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
        })
    }
}