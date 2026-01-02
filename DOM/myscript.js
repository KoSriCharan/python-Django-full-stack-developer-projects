var headOne = document.querySelector('#One');
var headTwo = document.querySelector('#Two');
var headThree = document.querySelector('#Three');

headOne.addEventListener('mouseover', function() {
    headOne.textContent = 'You hovered over the first heading!';
    headOne.style.color = 'red';
})

headOne.addEventListener('mouseout', function() {
    headOne.textContent = 'HOVER OVER ME!';
    headOne.style.color = 'black';
})

headTwo.addEventListener('click', function() {
    headTwo.textContent = 'You clicked the second heading!';
    headTwo.style.color = 'green';
})

headThree.addEventListener('dblclick', function() {
    headThree.textContent = 'You double-clicked the third heading!';
    headThree.style.color = 'blue';
})