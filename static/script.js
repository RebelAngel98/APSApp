

// A $( document ).ready() block.
$( document ).ready(function() {
    console.log( "ready!" );

    $("dark-mode-button").on("click", () => {
        alert("pressed")
    })


});



// /*  Dark Mode */
// const body = document.querySelector('body');

// // Dark Mode Action
// let darkMode = localStorage.getItem("darkMode");
// const darkModeToggle = document.querySelector('.dark-mode-button');
// const darkModeToggleFooter = document.getElementById("PageFooter");


// // Enable Dark Mode
// const enableDarkMode = () => {
//     body.classList.add("dark-mode");
//     localStorage.setItem("darkMode", "enabled")
// }

// // Disable Dark Mode
// const disableDarkMode = () => {
//     body.classList.remove("dark-mode");
//     localStorage.setItem("darkMode", null)
// }

// if (darkMode == "enabled") {
//     enableDarkMode();
// }

// // Desktop Button
// darkModeToggle.addEventListener('click', () => {
//     darkMode = localStorage.getItem("darkMode");
//     if (darkMode !== "enabled") {
//         enableDarkMode();
//     } else {
//         disableDarkMode();
//     }
// })

// /* the footer button for Dark Mode */

//     darkModeToggleFooter.addEventListener('click', () => {
//         darkMode = localStorage.getItem("darkMode");
//         console.log("ello")
//         if (darkMode !== "enabled") {
//             enableDarkMode();
//         } else {
//             disableDarkMode();
//         }
//     })

//     // Function to load CSS styles
// function loadStyles(filename) {
//     const link = document.querySelector('link[rel="stylesheet"]');
//     link.href = "{{ url_for('static', filename='') }}" + filename; // Generate the URL for the CSS file
// }


function sendMessage() {
    var user_answer = document.getElementById('userAnswer').value;
    document.getElementById('chat').innerHTML += "<p>User: " + user_answer + "</p>";
    document.getElementById('userAnswer').value = "";

    // Send user_answer to the server using POST method
    $.ajax({
        type: "POST",
        url: "/send_answer",
        data: { "user_answer": user_answer },
        success: function(data) {
            document.getElementById('chat').innerHTML += "<p>System: " + data.status + "</p>";
        },
        error: function() {
            // Handle any errors here
        }
    });
}
//add a function for checkAnswer to double check the project name 
//copying the function sendMessage above, but want to turn it into a 'if you get this right, then move on to posting a comment
function checkAnswer(){
    var user_project_number = document.getElementById('project_number').value;
    document.getElementById('chat').innerHTML +="<p>Machine: " + project_number + "</p>";
    document.getElementById('project_number').value = "";
} 