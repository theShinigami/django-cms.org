/**
 *
 * Swiper config
 */

(function() {
	'use strict';

	function initSwiper() {
		const swiperElements = document.querySelectorAll('.swiper');

		swiperElements.forEach(elem => {
			const loop = (elem.dataset.loop) === 'true';
			const spaceBetweenSlides = parseInt(elem.dataset.spaceBetweenSlides);
			const autoplay = (elem.dataset.autoplay === 'true')
				? { delay: parseInt(elem.dataset.delay), disableOnInteraction: false }
				: false;

			new Swiper(`.logoSwiper-${elem.dataset.instanceId}`, {
				slidesPerView: 1,      // Mobile
				spaceBetween: spaceBetweenSlides,
				loop: loop,
				keyboard: {
					enabled: true,
					onlyInViewport: true,
				},
				autoplay: autoplay,
				navigation: {
					nextEl: `.btn-next-${elem.dataset.instanceId}`,
					prevEl: `.btn-prev-${elem.dataset.instanceId}`,
				},
				breakpoints: {
				    768: {
					slidesPerView: 3, // Tablet
					spaceBetween: 40
				    },
				    1024: {
					slidesPerView: 4, // Desktop
					spaceBetween: 60
				    }
				}
			});
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', initSwiper);
	} else {
		initSwiper();
	}

})();


