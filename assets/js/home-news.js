(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const rotationInterval = 6500;

  document.querySelectorAll("[data-news-carousel]").forEach((carousel) => {
    const slides = Array.from(carousel.querySelectorAll(".home-news__slide"));
    const dotsContainer = carousel.querySelector("[data-news-dots]");
    const previousButton = carousel.querySelector("[data-news-prev]");
    const nextButton = carousel.querySelector("[data-news-next]");
    const toggleButton = carousel.querySelector("[data-news-toggle]");

    if (slides.length <= 1) return;

    let index = Math.max(slides.findIndex((slide) => slide.classList.contains("is-active")), 0);
    let timer = null;
    let userPaused = false;

    carousel.classList.add("has-news-carousel");
    carousel.style.setProperty("--news-progress-duration", `${rotationInterval}ms`);

    const dots = slides.map((_, dotIndex) => {
      const dot = document.createElement("span");
      dot.className = "home-news__dot";
      if (dotIndex === index) dot.classList.add("is-active");
      dotsContainer.appendChild(dot);
      return dot;
    });

    function setSlideAccess(slide, active) {
      slide.setAttribute("aria-hidden", active ? "false" : "true");
      slide.querySelectorAll("a, button").forEach((element) => {
        if (active) {
          element.removeAttribute("tabindex");
        } else {
          element.setAttribute("tabindex", "-1");
        }
      });
    }

    function activate(nextIndex) {
      index = (nextIndex + slides.length) % slides.length;
      slides.forEach((slide, slideIndex) => {
        const active = slideIndex === index;
        slide.classList.toggle("is-active", active);
        setSlideAccess(slide, active);
        dots[slideIndex].classList.toggle("is-active", active);
      });
      restartProgress();
    }

    function stop() {
      window.clearInterval(timer);
      timer = null;
      updatePauseState();
    }

    function updatePauseState() {
      carousel.classList.toggle("is-paused", reduceMotion.matches || userPaused);
    }

    function restartProgress() {
      const activeDot = dots[index];
      dots.forEach((dot) => dot.classList.remove("is-running"));
      activeDot.getBoundingClientRect();
      updatePauseState();
      if (reduceMotion.matches || userPaused) return;
      activeDot.classList.add("is-running");
    }

    function start() {
      stop();
      if (reduceMotion.matches || userPaused) return;
      restartProgress();
      timer = window.setInterval(() => activate(index + 1), rotationInterval);
    }

    function setReducedMotionState() {
      carousel.classList.toggle("is-reduced-motion", reduceMotion.matches);
      stop();
      if (reduceMotion.matches) {
        slides.forEach((slide) => setSlideAccess(slide, true));
      } else {
        activate(index);
        start();
      }
    }

    previousButton.addEventListener("click", () => {
      activate(index - 1);
      start();
    });

    nextButton.addEventListener("click", () => {
      activate(index + 1);
      start();
    });

    toggleButton.addEventListener("click", () => {
      userPaused = !userPaused;
      toggleButton.setAttribute("aria-pressed", String(userPaused));
      toggleButton.textContent = userPaused
        ? toggleButton.dataset.labelPlay || "Play"
        : toggleButton.dataset.labelPause || "Pause";
      start();
    });

    if (typeof reduceMotion.addEventListener === "function") {
      reduceMotion.addEventListener("change", setReducedMotionState);
    }

    setReducedMotionState();
  });
})();
