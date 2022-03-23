// Adding Anchors to nav links
const navLinks = document.querySelector(".nav__links")

navLinks.addEventListener("click", (e) => {
    e.preventDefault()
    if (e.target.hasAttribute("href")){
        let id = e.target.getAttribute("href")
        const section = document.querySelector(`${id}`)
        let coordinates = section.getBoundingClientRect()
        let yAxis = window.scrollY + coordinates.y
        console.log(yAxis)
        window.scrollTo({
            left:coordinates.x,
            top:yAxis,
            behavior:"smooth"
    });
}})

// Adding active state to nav links

navLinks.addEventListener("mouseover", (e)=> {
    if (e.target.hasAttribute("href")){
        const navTabs = document.querySelectorAll(".nav__link")
        navTabs.forEach( el => el.style.opacity = "0.3" )
        e.target.style.opacity= "1"
    }
})

navLinks.addEventListener("mouseleave", (e)=> {
    document.querySelectorAll(".nav__link")
    .forEach( el => el.style.opacity = "1")
})

// Adding scroll to Learn More button

const learnMoreBtn = document.querySelector(".btn--scroll-to")

learnMoreBtn.addEventListener("click",(e) => {
    const section = document.querySelector("#section--1")
    let coordinates = section.getBoundingClientRect()
        window.scrollTo({
            left:coordinates.x,
            top:coordinates.y,
            behavior:"smooth"
    });

})


// Changing Tabs on the Operations Section
const showTab = function (e) {
    if (e.target.classList.contains("operations__tab")){
    let tabClass = Array.from(e.target.classList)
    .find(el => el.startsWith("tab_"))
    const tabSection = document.querySelector(`.content_${tabClass}`)
    const allSections = document.querySelectorAll(".operations__content")
    allSections.forEach(el => el.classList.remove("is--active"))
    tabSection.classList.add("is--active")
    }
}

// Button Animation
const animateButton = function(e) {
    if (e.target.classList.contains("operations__tab")){
    let allTabs = document.querySelectorAll(".operations__tab")
    allTabs.forEach(el => el.classList.remove("btn--animate"))
    e.target.classList.add("btn--animate")
    }
}

// Using event Delegation to listen to all click events on the child elements
const tabsListener = document.querySelector("#section--2 .operations")

tabsListener.addEventListener("click",showTab)
tabsListener.addEventListener("click",animateButton)

// Using the Intersection observer API for activating the sticky header and other scroll
// dependent effect.

const makeSticky = (entries) => {
    const headerNav = document.querySelector("nav")
    const images = document.querySelectorAll(".feature_img")
    if(!entries[0].isIntersecting){
    headerNav.classList.add("sticky")
    }
    else{
    headerNav.classList.remove("sticky")
    }
}

const headerSection = document.querySelector("header")

const options = {
    root:null,
    threshold:0
}

const observerNav = new IntersectionObserver(makeSticky,options)
observerNav.observe(headerSection)

const allSections = document.querySelectorAll("section")

const revealSection = (entries,observer) => {
    const entry = entries[0]
    if (!entry.isIntersecting) return
    entry.target.classList.remove("section__hidden")
    observer.unobserve(entry.target)
}

const observerSections = new IntersectionObserver(revealSection,{
    root:null,
    threshold:0.20
})

allSections.forEach(el => {
    el.classList.add("section__hidden")
    observerSections.observe(el)
})


// Lazy loading images 

const blurredImages = document.querySelectorAll(".feature_img")

const lazyLoad = (entries, observer) => {
    const [entry] = entries
    if(entry.isIntersecting){
        entry.target.src = entry.target.dataset.src
        observer.unobserve(entry.target)
    }
    entry.target.addEventListener("load", () => {
        entry.target.classList.add("img__unblur")
    })
}

const observerImages = new IntersectionObserver(lazyLoad,
    {
    root:null,
    threshold:0.1,
    rootMargin:'200px',
    })

blurredImages.forEach( el => {
    observerImages.observe(el)
})

// Building  the testimonials slider

const testimonials = document.querySelectorAll(".slide")
const btnLeft =document.getElementById("slide-left");
const btnRight =document.getElementById("slide-right");

let currTab = 0

const switchTab = () => {
    testimonials.forEach((el,i) => {
        let percent = i * 100 - currTab*100
        el.style.transform = `translateX(${percent}%)`
        el.style.opacity = "0";
    })
    let testimonial = testimonials[currTab]
    testimonial.style.opacity = "100"
}

const slideTab = (direction) => {
    if(direction === "left"){
        currTab <= 0 ? currTab=0 : currTab--
    }else{
        currTab === testimonials.length - 1 ? currTab=0 : currTab++
    }
    switchTab()
}

const slideTabLeft = () => slideTab("left")
const slideTabRight = () => slideTab("right")

btnLeft.addEventListener("click",slideTabLeft)
btnRight.addEventListener("click",slideTabRight)


