
const button = document.getElementById('addBtn');

button.addEventListener('click', () => {
    button.textContent = 'Added';
    button.disabled = true;

    setTimeout(() => {
        button.textContent = 'Add to Cart';
        button.disabled = false;
    }, 2000);
});