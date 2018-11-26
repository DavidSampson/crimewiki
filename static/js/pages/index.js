let formSelect = document.getElementById('page-type-select');

editButton.addEventListener('click', _ => {
  deleteChildren(editForm);
  editForm.appendChild(getTemplateContent(`${formSelect.value}-form`));
  showEl(editForm);
});
