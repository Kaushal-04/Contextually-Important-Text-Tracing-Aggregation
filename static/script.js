document.getElementById('startButton').addEventListener('click', function() {
    // Redirect to processing page or send an API request to start summarizing
    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            action: 'start_summarizing'
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Processing complete: ' + JSON.stringify(data));
        // You can now update the UI or redirect to another page to show results
    })
    .catch(error => console.error('Error:', error));
});
