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
    var userAnswer = document.getElementById('user-input').value;
    document.getElementById('chat').innerHTML += "<p>User: " + userAnswer + "</p>";
    document.getElementById('user-input').value = "";

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
