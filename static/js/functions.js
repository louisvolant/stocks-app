document.addEventListener('DOMContentLoaded', function() {
    var helloElement = document.getElementById('hello');
    helloElement.addEventListener('click', function() {
        this.style.color = this.style.color === 'red' ? 'black' : 'red';
    });
});
