console.log('Hello please work');

const veganButton = document.querySelector("#vegan");

const veganCheck = () => {
  veganButton.classList.add("vegan-change");
}

veganButton.addEventListener("click", veganCheck);
