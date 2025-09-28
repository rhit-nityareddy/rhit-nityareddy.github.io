
/** DOM elements
 * https://www.w3schools.com/jsref/prop_html_innerhtml.asp
 */

let navbar = `
  <div>
    <a href="index.html">Main</a>
    <a href="resume.html">Resume</a>
    <a href="portfolio.html">Portfolio</a>
  </div> 
`;

let footbar = `
  <div>
    <a href="https://www.linkedin.com/in/nitya-reddy-926a21380/">Linkedin</a>
  </div> 
`;

window.addEventListener("load", function() {
  document.getElementsByClassName("nav")[0].innerHTML = navbar;
  document.getElementsByClassName("foot")[0].innerHTML = footbar;
})



/** Collapsible 
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







