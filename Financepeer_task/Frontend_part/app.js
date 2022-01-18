let data=fetch("http://127.0.0.1:8000/api/")
console.log(data);
data.then(res=>{
    console.log(res);
    return res.json();
}).then(data=>{
    console.log(data)
    const products=data.map(product=>{
        return `
        <div class="product">
        <center>
        
        <h3> userId: ${product.userId}</h3>
        </center>
        
        <p>Title:${product.title}</p>
        <p>Body: ${product.body}</p>
        </div>
        `;
    }).join("");
    console.log(products);
    document.querySelector("#app").innerHTML=products;
})
