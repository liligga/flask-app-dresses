let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const slideContainer = document.querySelector('.slides');
const slideCount= slides.length;
const intervalTime = 2500; 

function nextSlide() {
  currentSlide = (currentSlide + 1)% slideCount;
  updateSlide();
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + slideCount) % slideCount;
  updateSlide();
}
  
function updateSlide() {
  slideContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Автоматическая прокрутка слайдов
if (slideCount > 1) {
  setInterval(nextSlide, intervalTime);
}
