document.getElementById('pettyCashForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form values
    const date = document.getElementById('date').value;
    const description = document.getElementById('description').value;
    const amount = document.getElementById('amount').value;

    // Validate form values
    if (!date || !description || !amount) {
        alert('Please fill in all fields');
        return;
    }

    // Create a new table row
    const table = document.getElementById('pettyCashTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    // Insert cells into the new row
    const dateCell = newRow.insertCell(0);
    const descriptionCell = newRow.insertCell(1);
    const amountCell = newRow.insertCell(2);

    // Set cell values
    dateCell.textContent = date;
    descriptionCell.textContent = description;
    amountCell.textContent = amount;

    // Clear form fields
    document.getElementById('date').value = '';
    document.getElementById('description').value = '';
    document.getElementById('amount').value = '';
});
