const BOXES = document.querySelectorAll("#biblioteka")
const TITLES = document.querySelectorAll(".admin-library > h1")
for (let index = 0; index < BOXES.length; index++) {
    if (BOXES[index].childElementCount < 1) {
        BOXES[index].remove()
        TITLES[index].remove()
    }
}