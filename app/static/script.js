document.getElementById('refreshBtn').addEventListener('click', function() {
    document.getElementById('status').textContent = "Data refreshed at " + new Date().toLocaleTimeString();
});
