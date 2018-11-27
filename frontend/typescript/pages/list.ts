 let formSelect: HTMLElement = document.getElementById('page-type-select');

showButton.addEventListener('click', _ => {
  deleteChildren(editForm);
  editForm.appendChild(getTemplateContent(`${ (<HTMLInputElement>formSelect).value}-form`));
  showEl(editForm);
});
