// ==============================
// AI Portfolio JavaScript
// ==============================

// Smooth scrolling for navigation links

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function(e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if(target){

            target.scrollIntoView({
                behavior: "smooth"
            });

        }

    });

});


// Hero button animation

const buttons = document.querySelectorAll(".btn");

buttons.forEach(btn => {

    btn.addEventListener("mouseenter", () => {

        btn.style.transform = "scale(1.08)";

    });

    btn.addEventListener("mouseleave", () => {

        btn.style.transform = "scale(1)";

    });

});


// Welcome message

console.log("Welcome to AI Portfolio 🚀");
// ==============================
// Scroll Animation
// ==============================

const sections = document.querySelectorAll("section");

function revealSections() {

    sections.forEach(section => {

        const sectionTop = section.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (sectionTop < screenHeight - 100) {

            section.style.opacity = "1";
            section.style.transform = "translateY(0)";

        }

    });

}

sections.forEach(section => {

    section.style.opacity = "0";
    section.style.transform = "translateY(40px)";
    section.style.transition = "all 0.8s ease";

});

window.addEventListener("scroll", revealSections);

revealSections();


// ==============================
// Navbar Shadow on Scroll
// ==============================

const navbar = document.querySelector("nav");

window.addEventListener("scroll", () => {

    if (window.scrollY > 50) {

        navbar.style.boxShadow = "0 4px 15px rgba(0,0,0,0.4)";

    } else {

        navbar.style.boxShadow = "none";

    }

});
// ==============================
// Active Navigation Link
// ==============================

const navLinks = document.querySelectorAll("nav ul li a");

window.addEventListener("scroll", () => {

    let current = "";

    document.querySelectorAll("section").forEach(section => {

        const sectionTop = section.offsetTop - 120;

        if (window.pageYOffset >= sectionTop) {
            current = section.getAttribute("id");
        }

    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        if (link.getAttribute("href") === "#" + current) {
            link.classList.add("active");
        }

    });

});


// ==============================
// Back To Top Button
// ==============================

const topButton = document.createElement("button");

topButton.innerHTML = "⬆";

topButton.style.position = "fixed";
topButton.style.bottom = "20px";
topButton.style.right = "20px";
topButton.style.padding = "12px 16px";
topButton.style.border = "none";
topButton.style.borderRadius = "50%";
topButton.style.background = "#38bdf8";
topButton.style.color = "#fff";
topButton.style.cursor = "pointer";
topButton.style.display = "none";
topButton.style.fontSize = "18px";
topButton.style.zIndex = "999";

document.body.appendChild(topButton);

window.addEventListener("scroll", () => {

    if (window.scrollY > 300) {
        topButton.style.display = "block";
    } else {
        topButton.style.display = "none";
    }

});

topButton.addEventListener("click", () => {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

});

console.log("AI Portfolio Loaded Successfully ✅");
