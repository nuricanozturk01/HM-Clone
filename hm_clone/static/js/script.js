$(document).ready(function () {
    $('.slick-slider').slick({
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: $('.slick-prev'),
        nextArrow: $('.slick-next'),
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('search-button').addEventListener('click', function () {
        const searchTerm = document.querySelector('.form-control').value.trim();
        window.location.href = `/search/by/keyword?keyword=${searchTerm}`;
    });
});

function changeButtonColor(buttonId, location) {
    const buttons = document.querySelectorAll('.btn')
    buttons.forEach(function (btn) {
        btn.classList.remove('btn-selected')
    });

    document.getElementById(buttonId).classList.add('btn-selected')

    window.location.href = location
}

const handleCategoryClick = (keyword, category) => {
    window.location.href = `/search/by/category?keyword=${keyword}&category=${category}`
}

const clickProductHandle = id => window.location.href = `/find/product-detail?id=${id}`