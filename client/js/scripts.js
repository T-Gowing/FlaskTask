const fruitSection = document.getElementById('fruits')

async function fetchFruits(){
    fruitSection.textContent = ''
    try {
        const response = await fetch("http://127.0.0.1:8000/api/fruits");
        const fruits = await response.json();

        fruits.forEach(fruit => {
            const para = document.createElement('p');
            para.textContent = fruit.fruit;
            fruitSection.appendChild(para)
        })
    } catch (err) {
        console.error(err);
    }
}
