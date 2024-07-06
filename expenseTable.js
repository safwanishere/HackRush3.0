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
    const dateCell = newRow.insertCell(1);
    const frequencyCell = newRow.insertCell(2);

    // Set cell values
    idCell.textContent = id;
    dateCell.textContent = name;
    frequencyCell.textContent = frequency;

    // Clear form fields
    document.getElementById('id').value = '';
    document.getElementById('name').value = '';
    document.getElementById('frequency').value = '';
});

document.getElementById('expenseForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form values
    const eid = document.getElementById('eid').value;
    const Date = document.getElementById('Date').value;
    const IdHead = document.getElementById('IdHead').value;
    const expenseAmount = document.getElementById('expenseAmount').value;
    const description = document.getElementById('description').value;

    // Create a new table row
    const table = document.getElementById('expenseTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    // Insert cells into the new row
    const eidCell = newRow.insertCell(0);
    const dateCell = newRow.insertCell(1);
    const IdHeadCell = newRow.insertCell(2);
    const expenseAmountCell = newRow.insertCell(3);
    const descriptioncell = newRow.insertCell(4);

    // Set cell values
    eidCell.textContent = eid;
    dateCell.textContent = Date;
    IdHeadCell.textContent = IdHead;
    expenseAmountCell.textContent = expenseAmount;
    descriptioncell.textContent = description

    // Clear form fields
    document.getElementById('eid').value = '';
    document.getElementById('date').value = '';
    document.getElementById('IdHead').value = '';
    document.getElementById('expenseAmount').value = '';
    document.getElementById('description').value = '';
});