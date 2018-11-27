let editForm: HTMLElement = document.getElementById('edit-form');
let showButton: HTMLElement = document.getElementById('show-button');
let comments: HTMLElement = document.getElementById('comments');
const hideEl = (e: HTMLElement) => e.style.display = 'none';
const showEl = (e: HTMLElement) => e.style.display = 'block';
const getToggledValue = (v: string) => v === 'none' ? 'block' : 'none';
const toggleEl = (e: HTMLElement) => e.style.display = getToggledValue(e.style.display);

const deleteChildren = (e: HTMLElement) => {e.innerHTML = ''; return e};

const getTemplateContent = (t: string) => document.importNode((<HTMLTemplateElement>document.getElementById(t)).content, true);

async function fetchComments(type: string, _id: number): Promise<string> {
  let res = await fetch(`/comments/${type}/${_id}`);
  let data = await res.text();
  return data
}
