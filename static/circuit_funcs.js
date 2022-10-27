function feedback_gate(gate){
    gate.hover(function(){
        console.log("yo")
        $(this).css("background-color", "gray")
    }, function(){
        $(this).css("background-color", "")
    })
}

function generate_tray(){
    let tray_container = $(".tray-container")
    tray_container.empty()
    let gates = ["X", "I", "H"]
    $.each(gates, function(index, value){
        let tray_gate = $("<li class='gate tray-gate'>")
        tray_gate.text(value)
        feedback_gate(tray_gate)
        draggable_gates(tray_gate)
        tray_container.append(tray_gate)
    })
    let trash_can = $("<i class='fas fa-trash trash'>")
    tray_container.append(trash_can)
}

function draggable_gates(gate){
    gate.draggable({
        connectToSortable: ".gate-slots",
        revert: "invalid",
        helper: function(){
            let class_list = $(gate).attr("class").split(/\s+/)
            console.log(class_list)
            if ($.inArray("tray-gate", class_list) != -1){
                console.log("cloning")
                let clone_gate = gate.clone()
                feedback_gate(clone_gate)
                draggable_gates(clone_gate)  // Need to add draggable handlers to the gate again
                return clone_gate
            } else {
                console.log("returning self")
                // feedback_gate(clone_gate)
                // draggable_gates(gate)
                return gate
            }
        },
        revertDuration: 0,
        start: function(){
            console.log("hello")
            $(".trash").css("color", "black")
            // if ($.inArray("tray-gate", class_list)){
            //     generate_tray()
            // }
        },
        stop: function(){
            $(".trash").css("color", "")
        }
    })

   gate.hover(function(event){
        $(this).css("cursor", "move")
    }, function(event){
        $(this).css("cursor", "")
    })
}



function droppable_trash(bloch_update_url){
    $(".trash").droppable({
        drop: function(event, ui){
            let class_list = $(ui.draggable).attr("class").split(/\s+/)

            // If not a tray gate, remove the element
            if ($.inArray("tray-gate", class_list) == -1) {
                console.log("Not a tray gate - deleting")
                $(ui.draggable.remove())
                update_bloch_sphere($(".gate-slots"), bloch_update_url)
            } else {
                console.log("A tray gate - keeping")
            }
        }
    })
}

function add_gates(gates, gate_slots, draggable = true){


    $.each(gates, function(index, gate){
        let gate_li = $("<li class='gate circuit-gate ui-state-default'>")

        gate_li.text(gate)
        if (draggable) {
            draggable_gates(gate_li)
            feedback_gate(gate_li)
        }
        gate_slots.append(gate_li)
    })
}

function get_gates_list(gate_slots){

    let gates_list = []
    console.log(gate_slots)
    gate_slots.find("li").each(function(){
        // console.log(li.textContent)
      gates_list.push($(this).text())
    })
    console.log(gates_list)
    return gates_list
}

function update_bloch_sphere(gate_slots, url){

    if(typeof url == 'undefined') {
        console.log("Not updating bloch sphere because there was no valid bloch update url")
        return
    }
    // gate_slots should be a <ul>
    let gates_list = get_gates_list(gate_slots)

    $.ajax({
        type: "POST",
        url: url,
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(gates_list),
        success: function(result){
            console.log("blah")

            let image = $(".bloch-image")
            add_bloch_sphere("/" + result.bloch_sphere, image)
            console.log("added")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


function add_bloch_sphere(image_path, image){
    console.log(image_path)

    d = new Date()
    image.attr("src", image_path + "?" +d.getTime())
}

function make_gate_slots_sortable(bloch_update_url, onUpdate){
    console.log("ry")
    console.log(bloch_update_url)
    $(".gate-slots").sortable({
        placeholder: 'gate-outline',
        beforeStop: function (event, ui) {
            let gate = ui.item
            gate.removeClass("tray-gate")
            gate.addClass("circuit-gate")
            console.log(gate.attr("class"))

            console.log(ui.item)
        },
        update: function(event, ui){
            console.log("dropped into sortable")
            update_bloch_sphere($(this), bloch_update_url)
            console.log("updated bloch_sphere!")
            console.log(onUpdate)
            if (onUpdate != null){
                onUpdate()
            }
        }
    })
}

function update_data(data_type){
    let url = "/get_data/"+data_type

    $.get(url);
}
