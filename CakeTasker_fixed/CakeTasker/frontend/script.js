
async function cargar(){
    const res = await fetch("http://localhost:5000/pedidos");
    const data = await res.json();
    document.getElementById("lista").innerHTML =
        data.map(p => `<p><b>${p.nombre}</b>: ${p.descripcion} [${p.estado}]</p>`).join("");
}
async function crearPedido(){
    const nombre = document.getElementById("nombre").value;
    const descripcion = document.getElementById("desc").value;

    await fetch("http://localhost:5000/pedidos",{
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body:JSON.stringify({nombre, descripcion})
    });

    cargar();
}
window.onload = cargar;
