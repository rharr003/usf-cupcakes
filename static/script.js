const cake_list = document.querySelector("ul");
const form = document.querySelector("form");


async function populate_cupcakes() {
  const cupcakes = await fetch("http://127.0.0.1:5000//api/cupcakes")
    .then((response) => response.json())
    .then((data) => data);
  console.log(cupcakes);
  for (let cake of cupcakes.cakes) {
    const html = `<li>flavor:${cake.flavor} ${cake.size} ${cake.rating}</li>`;
    cake_list.insertAdjacentHTML("beforeend", html);
  }
}

const header = {
    'Content-Type': 'application/json'
}

async function post_cupcake(data) {
    await fetch("http://127.0.0.1:5000//api/cupcakes", {
        method: 'POST',
        headers: header,
        body: JSON.stringify(data)
    })
    cake_list.innerHTML =''
    populate_cupcakes()


}

form.addEventListener("submit", function(e) {
  e.preventDefault();
  const data = {
    flavor: form.flavor.value,
    size: form.size.value,
    rating: form.rating.value,
    image: form.image.value,
  };
  post_cupcake(data)
  console.log(data);
});

populate_cupcakes();