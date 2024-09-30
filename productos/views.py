from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templateApp/index.html')

def usuario(request):
    data = {
        "id": "12345", 
        "nombre": "Itallo Benedetti",
        "email": "itallo.benedetti@gmail.com",
        "imagen_url": "/static/img/usuario.png"
    }

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <title>Información de Usuario</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Supermercado</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/">Inicio</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/productos/">Productos</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/usuario/">Usuario</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <h1 class="text-center"><strong>Información de Usuario</strong></h1>
            <div class="row justify-content-center">
                <div class="col-md-6 text-center">
                    <img src="{data['imagen_url']}" alt="Imagen de Usuario" class="img-fluid" width="300">
                    <ul class="list-group mt-3">
                        <li class="list-group-item"><strong>ID:</strong> {data['id']}</li>
                        <li class="list-group-item"><strong>Nombre:</strong> {data['nombre']}</li>
                        <li class="list-group-item"><strong>Email:</strong> {data['email']}</li>
                    </ul>
                    <a href="/" class="btn btn-success mt-3">VOLVER</a>
                </div>
            </div>
        </div>

        <footer class="bg-light text-center text-lg-start mt-5">
            <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
                © 2024 Supermercado:
                <a class="text-dark" href="#">jumbo.cl</a>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+JZxYF9E2c1OjuhKU7fIvaBjsENl4" crossorigin="anonymous"></script>
    </body>
    </html>
    """

    return HttpResponse(html_content)


def productos(request):
    productos_data = [
        {"nombre": "Pack 12 un. Bebida Láctea Chamyto Frutilla 80 ml", "valor": "$3.000", "imagen_url": "/static/img/producto1.webp", "descripcion": "Bebida láctea Chamyto Frutilla, es una bebida láctea con probióticos sabor frutilla para una protección diaria de los niños, no requiere preparación y se debe mantener refrigerado de 2 a 8 ° C. Formato multipack 12 unidades de 80ml. Con probióticos. 0% grasas totales."},
        {"nombre": "Leche Soprole Sin Lactosa Semidescremada 1 L", "valor": "$1.339", "imagen_url": "/static/img/producto2.webp", "descripcion": "Leche sin lactosa semidescremada 100% natural de la zona centro y sur de Chile. Envase con tapa. Leche 100% natural, certificado por el INTA. Sin lactosa, sin azúcar añadida y libre de sellos. Envase 100% reciclable con tapa. Perfecto para tus desayunos y colaciones"},
        {"nombre": "Yogurt Colun Sin Azúcar Frutilla 120 g", "valor": "$329", "imagen_url": "/static/img/producto3.webp", "descripcion": "Delicioso y sin azúcar, con el dulce sabor natural de la frutilla, perfecto para un snack saludable. Yoghurt Sin Azúcar. 0% grasa total. Sin lactosa. Libre de Gluten "}
    ]
    
    return render(request, 'templateApp/productos.html', {'productos': productos_data})

def descripcion_producto(request, producto_id):
    productos_data = [
        {"nombre": "Pack 12 un. Bebida Láctea Chamyto Frutilla 80 ml", "valor": "$3.000", "imagen_url": "/static/img/producto1.webp", "descripcion": "Bebida láctea Chamyto Frutilla, es una bebida láctea con probióticos sabor frutilla para una protección diaria de los niños, no requiere preparación y se debe mantener refrigerado de 2 a 8 ° C. Formato multipack 12 unidades de 80ml. Con probióticos. 0% grasas totales."},
        {"nombre": "Leche Soprole Sin Lactosa Semidescremada 1 L", "valor": "$1.339", "imagen_url": "/static/img/producto2.webp", "descripcion": "Leche sin lactosa semidescremada 100% natural de la zona centro y sur de Chile. Envase con tapa. Leche 100% natural, certificado por el INTA. Sin lactosa, sin azúcar añadida y libre de sellos. Envase 100% reciclable con tapa. Perfecto para tus desayunos y colaciones"},
        {"nombre": "Yogurt Colun Sin Azúcar Frutilla 120 g", "valor": "$329", "imagen_url": "/static/img/producto3.webp", "descripcion": "Delicioso y sin azúcar, con el dulce sabor natural de la frutilla, perfecto para un snack saludable. Yoghurt Sin Azúcar. 0% grasa total. Sin lactosa. Libre de Gluten "}
    ]

    producto = productos_data[producto_id]
    
    return render(request, 'templateApp/descripcion.html', {'producto': producto})