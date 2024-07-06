document.getElementById('pettyCashForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form values
    const id = document.getElementById('id').value;
    const name = document.getElementById('name').value;
    const frequency = document.getElementById('frequency').value;

    // Valiid form values
    if (!id || !name || !frequency) {
        alert('Please fill in all fields');
        return;
    }

    // Create a new table row
    const table = document.getElementById('pettyCashTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    // Insert cells into the new row
    const idCell = newRow.insertCell(0);
    const nameCell = newRow.insertCell(1);
    const frequencyCell = newRow.insertCell(2);

    // Set cell values
    idCell.textContent = id;
    nameCell.textContent = name;
    frequencyCell.textContent = frequency;

    // Clear form fields
    document.getElementById('id').value = '';
    document.getElementById('name').value = '';
    document.getElementById('frequency').value = '';
});
