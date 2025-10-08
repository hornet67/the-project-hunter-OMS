document.getElementById('toggle-btn').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('collapsed');
  });

  // Initialize all toasts
  const toastElList = [].slice.call(document.querySelectorAll('.toast'));
  toastElList.map(function(toastEl) {
    return new bootstrap.Toast(toastEl, { delay: 3000 }).show();
  });


   const searchInput = document.getElementById('searchInput');
  searchInput.addEventListener('input', function() {
    const filter = searchInput.value.toLowerCase();
    const rows = document.querySelectorAll('#itemsTable tbody tr');
    rows.forEach(row => {
      row.style.display = row.textContent.toLowerCase().includes(filter) ? '' : 'none';
    });
  });

  // Form submit (just frontend for now)
  const addItemForm = document.getElementById('addItemForm');
  addItemForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const itemName = document.getElementById('itemName').value;
    const itemCategory = document.getElementById('itemCategory').value;

    const table = document.getElementById('itemsTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    newRow.innerHTML = `
      <td>${table.rows.length}</td>
      <td>${itemName}</td>
      <td>${itemCategory}</td>
      <td>
        <button class="btn btn-sm btn-warning">Edit</button>
        <button class="btn btn-sm btn-danger">Delete</button>
      </td>
    `;

    // Reset form and close modal
    addItemForm.reset();
    const modal = bootstrap.Modal.getInstance(document.getElementById('addItemModal'));
    modal.hide();
  });