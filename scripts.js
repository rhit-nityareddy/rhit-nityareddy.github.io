
/*
* https://www.w3schools.com/jsref/dom_obj_pushbutton.asp
*/
let b = document.createElement("mainButton")
b.addEventListener("click", () => {
    
})


/**
 * https://www.w3schools.com/howto/howto_js_collapsible.asp
 */

let coll = document.getElementsByClassName("collapsible");
let i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("activeCollapsible");
    let content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}







