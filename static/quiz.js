
function confirmExit() {
    return "You are leaving a quiz page."
}

function quizExitPopup(){
    $(window).bind('beforeunload', function(e){
        
        // $.confirm({
        //     'title' : 'Did You Save Your Changes?',
        //     'message'   : 'It seems as if you have made changes but didn\'t click Save.\nAre you sure you want to leave the page?',
        //     'buttons'   : {
        //         'OK'    : {
        //             'class' : 'gray',
        //             // 'action': function(){}  // Nothing to do in this case. This can be omitted if you prefer.
        //         }
        //     })
        // }
        //$.confirm("Are you sure you want to leave this quiz?")

        $('confirm text').dialog(
            {
                modal:true, //Not necessary but dims the page background
                buttons:{
                    'Save':function() {
                        //Whatever code you want to run when the user clicks save goes here
                     },
                     'Delete':function() {
                         //Code for delete goes here
                      }
                }
            }
        );

        e.preventDefault();

        //return "Are you sure you want to leave this quiz?";
        
    });

    // $(window).on('beforeunload', function(e){
    //     return "Are you sure you want to leave this quiz?";
    // }


}