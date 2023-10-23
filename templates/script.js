/*  Dark Mode */
const body = document.querySelector('body');

// Dark Mode Action
let darkMode = localStorage.getItem("darkMode");
const darkModeToggle = document.querySelector('.dark-mode-button');
const darkModeToggleFooter = document.querySelector('footer .dark-mode-button');

// Enable Dark Mode
const enableDarkMode = () => {
    body.classList.add("dark-mode");
    localStorage.setItem("darkMode", "enabled")
}

// Disable Dark Mode
const disableDarkMode = () => {
    body.classList.remove("dark-mode");
    localStorage.setItem("darkMode", null)
}

if (darkMode == "enabled") {
    enableDarkMode();
}

// Desktop Button
darkModeToggle.addEventListener('click', () => {
    darkMode = localStorage.getItem("darkMode");
    if (darkMode !== "enabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
})

// Footer button, optional. This is for if you have a second dark mode toggle button
//in the footer, just make sure the button is inside the footer tag, and it will be
//linked to this function.

    darkModeToggleFooter.addEventListener('click', () => {
        darkMode = localStorage.getItem("darkMode");
        if (darkMode !== "enabled") {
            enableDarkMode();
        } else {
            disableDarkMode();
        }
    })
// Function to load CSS styles
function loadStyles(filename) {
    const link = document.querySelector('link[rel="stylesheet"]');
    link.href = "{{ url_for('static', filename='') }}" + filename; // Generate the URL for the CSS file
}

function sendMessage() {
    var userAnswer = document.getElementById('user_answer').value;
    document.getElementById('chat').innerHTML += "<p>User: " + user_answer + "</p>";
    document.getElementById('user_answer').value = "";

    // Send userAnswer to the server using POST method
    $.ajax({
        type: "POST",
        url: "/send_answer",
        data: { user_answer: userAnswer },
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