document.addEventListener('DOMContentLoaded', function () {
  if (document.getElementById('image-carousel')) {
    const carousel = new Splide('#image-carousel', {
      type: 'loop',
      gap: '1rem',
    });
    carousel.mount();
  }
});

const articleBody = document.querySelector('.article-body');

document.querySelector('.article-section .reading-time').textContent = `Reading time: ~${Math.ceil(
  articleBody.textContent.split(' ').length / 200
)} minutes`;
