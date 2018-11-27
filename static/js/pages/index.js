let formSelect = document.getElementById('page-type-select');

showButton.addEventListener('click', _ => {
  deleteChildren(editForm);
  editForm.appendChild(getTemplateContent(`${formSelect.value}-form`));
  showEl(editForm);
});
