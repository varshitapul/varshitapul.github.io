// Typing effect
document.addEventListener("DOMContentLoaded", () => {
    const typingElement = document.querySelector(".typing");
    const text = typingElement.getAttribute("data-text");
    let index = 0;
  
    function type() {
      if (index < text.length) {
        typingElement.innerHTML += text.charAt(index);
        index++;
        setTimeout(type, 100); // Adjust speed if needed
      }
    }
  
    type();
  });
  
  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth"
      });
    });
  });
  