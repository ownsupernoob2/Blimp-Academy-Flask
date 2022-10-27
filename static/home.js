

// Assumes circuit_funcs has been included in layout.html

function populate_complete_sections(home_data){

    let sections = [$("#qubits-done"), $("#program-qubits-done"), $("#quiz-done")]
    let links = [$("#home-qubits-link"), $("#home-program-qubits-link"), $("#home-quiz-link")]
    let complete_secs = sections.slice(0, home_data.complete_sections)
    let disabled_links = links.slice(home_data.complete_sections + 1)
    $.each(complete_secs, function(index, sect){
        sect.addClass("section-done")
        let img = $("<img class='qubert-tiny' src='/static/images/qubert/qubert_happy.png'>")

        sect.append(img)
        sect.append($("<div>Complete!</div>"))
    })

    $.each(disabled_links, function (index, link){
        link.addClass("home-link-disabled")
        link.click(function(){  // Disable clicking
            return false
        })
    })


}

function setup_page(home_data){

    add_gates(home_data["media"]["learn_circuit"]["gates"], $(".gate-slots"), false)
    add_bloch_sphere(home_data["media"]["bloch_sphere"], $(".bloch-image"))
    generate_tray()
    let bloch_update_url = "/home/circuit"
    // make_gate_slots_sortable(bloch_update_url)

    droppable_trash(bloch_update_url)
    populate_complete_sections(home_data)
}
