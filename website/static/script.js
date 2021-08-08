// modal
const infoButton = document.querySelector('#button1');
const closeButton = document.querySelector('#button1close');
const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');

infoButton.addEventListener('click', () => {
    modal.classList.add('is-active');
    console.log('modal is active');
})

modalBg.addEventListener('click', () => {
    modal.classList.remove('is-active');
    console.log('modal is not active');
})

closeButton.addEventListener('click', () => {
    modal.classList.remove('is-active');
    console.log('modal is not active');
})