let editForm = document.getElementById('page-form');
let editButton = document.getElementById('add-page-enable');
let formSelect = document.getElementById('page-type-select');


function visibility(e, value='toggle'){
  e.style.visibility = value=='toggle' ?  ['hidden','visible'].filter(v => v!=e.style.visibility)[0] : value;
}
const deleteChildren = e => {e.innerHTML = ''; return e};

const getTemplateContent = t => document.importNode(document.getElementById(t).content, true);

function enableForm(e) {
  deleteChildren(editForm);
  editForm.appendChild(getTemplateContent(`${formSelect.value}-form`));
  visibility(editForm, 'visible');
}

editButton.addEventListener('click', enableForm);
