// Function to toggle dark mode
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-toggle'); // Toggle the 'dark-mode' class on the body element

    // Determine which styles to load based on the current mode
    if (body.classList.contains('dark-toggle')) {
        // If in dark mode, load dark styles
        loadStyles('dark-styles.css');
    } else {
        // If in light mode, load light styles
        loadStyles('styles.css');
    }
}

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