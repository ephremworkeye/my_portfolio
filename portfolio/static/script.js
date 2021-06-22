const bannerHeader = document.querySelector('#banner-header');
const headers = document.querySelectorAll('h1');
const Images = document.querySelectorAll('img');

bannerHeader.addEventListener('mouseover', e => {
    e.target.style.color = 'green';

    setTimeout(function() {
        e.target.style.color = "";
      }, 500);
}, false);

headers.forEach(header => {
  header.addEventListener('mouseover', e => {
    e.target.style.color = 'green';

    setTimeout(function() {
      e.target.style.color = "";
    }, 500);
  }, false)
});

images.forEach(image => {
  image.addEventListener('mouseover', e => {
    currentWidth = image.clientWidth;
    e.target.style.width = (currentWidth * 1.5) + 'px';

    setTimeout(function() {
      e.target.style.width = '';
    }, 500);
  }, false);
})
