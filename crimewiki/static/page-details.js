let editForm = document.getElementById('edit-form');
let editButton = document.getElementById('edit-button');

function toggleVisibility(e) {
  let vis = editForm.style.visibility;
  editForm.style.visibility = vis == 'hidden' ? 'visible' : 'hidden';
};

editButton.addEventListener('click', toggleVisibility);
