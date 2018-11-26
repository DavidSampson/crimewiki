
const visibility = value => e => e.style.visibility = value=='toggle' ?  ['hidden','visible'].filter(v => v!=e.style.visibility)[0] : value;
const hideEl = e => e.style.visibility = 'hidden';
const showEl = e => e.style.visibility = 'visible';
const getToggledValue = v => v === 'visible' ? 'hidden' : 'visible';
const toggleEl = e => e.style.visibility = getToggledValue(e.style.visibility);

const deleteChildren = e => {e.innerHTML = ''; return e};

const getTemplateContent = t => document.importNode(document.getElementById(t).content, true);
