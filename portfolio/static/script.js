const bannerHeader = document.querySelector('#banner-header');

bannerHeader.addEventListener('mouseover', e => {
    e.target.style.color = 'green';

    setTimeout(function() {
        e.target.style.color = "";
      }, 500);
}, false)