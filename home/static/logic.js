const buttons = document.querySelectorAll('.btn_counter');

buttons.forEach((btn) => {
    let count = 0;
    const info = btn.nextElementSibling;


    const span = btn.parentElement.querySelector('.click-display');

    btn.addEventListener('click', () => {
        count++;
        span.textContent = "Click " + count + " Times";
    });


    btn.addEventListener('mouseenter', () => {
        span.style.display = 'inline';
    });


    btn.addEventListener('mouseleave', () => {
        span.style.display = 'none';
    });
});

const swiper = new Swiper(".mySwiper", {
    loop: true,
    autoplay: {
        delay: 3000,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});



document.addEventListener('DOMContentLoaded', () => {
    const { on } = interact;

    document.querySelectorAll('.image-container').forEach(container => {
        const img = container.querySelector('.main-image');
        const imgLeft = container.dataset.imgLeft;
        const imgRight = container.dataset.imgRight;
        const imgCenter = container.dataset.imgCenter;
        const imgDefault = container.dataset.imgDefault;

        interact(container)
            .pointerEvents({ holdDuration: 0 })
            .on('pointermove', event => {
                const rect = container.getBoundingClientRect();
                const x = event.clientX - rect.left;
                const w = rect.width;

                if (x < w * 0.33) img.src = imgLeft;
                else if (x > w * 0.66) img.src = imgRight;
                else img.src = imgCenter;
            })
            .on('pointerleave', () => img.src = imgDefault);
    });
});

document.addEventListener('DOMContentLoaded', function () {
  const button = document.querySelector('#api-mount-button');
  const input = document.querySelector('#options-per-view-input');
  const glideContainer = document.querySelector('#options-per-view');
  const maxSlides = glideContainer.querySelectorAll('.glide__slide').length;

  let initialValue = parseInt(input.value) || 3;

  const glide = new Glide('#options-per-view', {
    type: 'carousel',
    perView: initialValue,
    gap: 20,
    focusAt: 'center'
  });

  glide.mount();

  button.addEventListener('click', function () {
    let val = parseInt(input.value);
    if (isNaN(val) || val < 1 || val > maxSlides) {
      val = 1;
    }
    glide.update({ perView: val });
  });

  input.addEventListener('input', function (event) {
    const newValue = parseInt(event.target.value);
    if (glide && newValue >= 1 && newValue <= maxSlides) {
      glide.update({ perView: newValue });
    }
  });
});

