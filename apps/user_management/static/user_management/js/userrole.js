const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Open modal to add role
function openAddModal() {
    document.getElementById('addRoleModalLabel').innerText = 'Add New Role';
    document.getElementById('roleSubmitBtn').innerText = 'Add Role';
    document.getElementById('formAction').value = 'add';
    document.getElementById('roleId').value = '';
    document.getElementById('roleName').value = '';
    new bootstrap.Modal(document.getElementById('addRoleModal')).show();
}

// Open modal to edit role
function openEditModal(id, name) {
    document.getElementById('addRoleModalLabel').innerText = 'Update Role';
    document.getElementById('roleSubmitBtn').innerText = 'Update Role';
    document.getElementById('formAction').value = 'update';
    document.getElementById('roleId').value = id;
    document.getElementById('roleName').value = name;
    new bootstrap.Modal(document.getElementById('addRoleModal')).show();
}

// Handle form submit (Add / Update)
document.getElementById('roleForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('roleName').value.trim();
    const action = document.getElementById('formAction').value;
    const id = document.getElementById('roleId').value;

    if (!name) return alert('Role name is required.');

    let url = '/user/userrole/';
    let method = 'POST';

    if (action === 'update') {
        url += `${id}/`;
        method = 'PUT';
    }

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ role: name })
    })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                updateTableRow(action, id, name);
                new bootstrap.Modal(document.getElementById('addRoleModal')).hide();
            } else {
                alert('Error: ' + (data.message || JSON.stringify(data)));
            }
        })
        .catch(err => console.error(err));
});

// Update table dynamically
function updateTableRow(action, id, name) {
    if (action === 'add') {
        const tableBody = document.getElementById('rolesTableBody');
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td>${id || 'New'}</td>
            <td>${name}</td>
            <td>
                <button class="btn btn-sm btn-warning edit-btn" onclick="openEditModal('${id}', '${name}')">Edit</button>
                <button class="btn btn-sm btn-danger delete-btn" onclick="deleteRole('${id}')">Delete</button>
            </td>
        `;
        tableBody.appendChild(newRow);
    } else if (action === 'update') {
        const rows = document.querySelectorAll('#rolesTableBody tr');
        rows.forEach(row => {
            if (row.querySelector('.edit-btn').getAttribute('onclick').includes(`'${id}'`)) {
                row.cells[1].innerText = name;
                row.querySelector('.edit-btn').setAttribute('onclick', `openEditModal('${id}', '${name}')`);
            }
        });
    }
}

// Delete role
function deleteRole(id) {
    if (!confirm('Are you sure you want to delete this role?')) return;

    fetch(`/user/userrole/${id}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json'
        }
    })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                const rows = document.querySelectorAll('#rolesTableBody tr');
                rows.forEach(row => {
                    if (row.querySelector('.delete-btn').getAttribute('onclick').includes(`'${id}'`)) {
                        row.remove();
                    }
                });
            } else {
                alert('Failed to delete role.');
            }
        })
        .catch(err => console.error(err));
}
