// Establish WebSocket connection
const ws = new WebSocket("ws://localhost:6789");

// Elements
const onTimeInput = document.getElementById("onTime");
const offTimeInput = document.getElementById("offTime");
const statusText = document.getElementById("statusText");

// Update status text
function updateStatus(message) {
    statusText.textContent = message;
    statusText.style.color = message === "Connected" ? "#4CAF50" : "#ff9800";
}

// When WebSocket opens, update status to 'Connected'
ws.onopen = function () {
    updateStatus("Connected");
};

// When WebSocket is closed, update status to 'Disconnected'
ws.onclose = function () {
    updateStatus("Disconnected");
};

// Handle WebSocket errors
ws.onerror = function (error) {
    console.log("WebSocket Error: ", error);
    updateStatus("Error");
};

// Function to send schedule to the server via WebSocket
function sendSchedule() {
    const onTime = onTimeInput.value;
    const offTime = offTimeInput.value;

    if (onTime && offTime) {
        const schedule = {
            onTime: onTime,
            offTime: offTime
        };

        // Send schedule as JSON string via WebSocket
        if (ws.readyState === WebSocket.OPEN) {
            ws.send(JSON.stringify(schedule));
            console.log("✅ Sent schedule:", schedule);
        } else {
            console.log("❌ WebSocket not connected.");
        }
    } else {
        alert("Please fill in both ON and OFF times.");
    }
}
