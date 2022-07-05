function deleteNote(noteId) {
  let line = document.getElementById("linecut");
  let effect = document.getElementById("effect");
  line.style.textDecoration = "line-through";
  effect.classList.add("fadeout");
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
