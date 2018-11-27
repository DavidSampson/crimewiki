showButton.addEventListener('click', e => toggleEl(editForm));

(async ()=> {
  let contents = await fetchComments(comments.dataset.type, parseInt(comments.dataset.id));
  comments.innerHTML = contents;
  let commentsButton = document.getElementById('add-comment-button');
  let commentForm = document.getElementById('add-comment-form');
  commentsButton.addEventListener('click', ()=>showEl(commentForm));
})();
