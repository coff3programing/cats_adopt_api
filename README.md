# CATS ADOPTION API

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)

## Descripción

Bienvenido a la API de Adopción de Gatitos, donde el poder de Django Rest Framework se combina con el amor por los felinos. Cada endpoint es un puente entre corazones peludos y hogares cálidos. Con solo unas líneas de código, conectamos a familias con nuevos compañeros peludos, creando historias de adopción que laten con emoción y ronroneos. Adopta el amor en su forma digital. Adopta con nuestra API. 🐾💙 #AdoptaAmor #DRF #GatosFelices

## Sigueme a través de estos Pasos

1. Preparativos:
   Asegúrate de tener Python instalado en tu sistema `python --version`
2. Activar el Entorno Virtual (Opcional):
   Para activar hagalo desde el shell de windows con el comando `venv\Scripts\activate`
3. Instalación de Dependencias
   Instala las dependencias necesarias utilizando el archivo requirements.txt `pip install -r requirements.txt`
4. Ejecutar el Servidor `py manage.py runserver`

## Explorar la API

cada ruta es una puerta a la ternura y la posibilidad de encontrar un compañero peludo. Explora nuestros encantadores endpoints💘:

### Obtener Lista de Gatitos 🐾

- **Método:** `GET`
- **Ruta:** `/adopt/api/v1/cats/`
- **Descripción:** Descubre una lista mágica de gatitos esperando ser adoptados. Cada endpoint es como una ventana a un mundo de ronroneos y narices curiosas.

### Crear Nuevo Gatito ✨

- **Método:** `POST`
- **Ruta:** `/adopt/api/v1/cats/`
- **Descripción:** Da vida a la magia creando un nuevo perfil para un adorable gatito. ¡Cada POST es como un hechizo que agrega una nueva chispa a nuestro refugio virtual!

### Detalles de un Gatito Especial 💖

- **Método:** `GET`
- **Ruta:** `/adopt/api/v1/cats/{id}/`
- **Descripción:** Sumérgete en la historia de un gatito único. Este endpoint te lleva a un viaje encantador lleno de detalles y encantos felinos.

### Actualizar Historia de Gatito 📝

- **Método:** `PUT`
- **Ruta:** `/adopt/api/v1/cats/{id}/`
- **Descripción:** Da un toque personal a la historia de un gatito. Con el poder de un PUT, puedes actualizar la narrativa y hacer que cada cola tenga un final aún más feliz.

### Actualización Mágica del Gatito 🌟

- **Método:** `PATCH`
- **Ruta:** `/adopt/api/v1/cats/{id}/`
- **Descripción:** ¡Transforma la realidad de un gatito con un toque de magia! Utiliza el PATCH para actualizar detalles específicos y hacer que cada uno sea especial a su manera.

### Eliminar Hechizo del Gatito 🪄

- **Método:** `DELETE`
- **Ruta:** `/adopt/api/v1/cats/{id}/`
- **Descripción:** A veces, es necesario deshacer un hechizo. Con el DELETE, puedes decir adiós a la entrada de un gatito, pero su magia perdura en nuestros corazones digitales.

Explora estos encantadores endpoints y descubre la magia de la adopción de gatitos en cada solicitud.

## Nota Importante: Cambio de Base de Datos

---

Durante el desarrollo en localhost, estamos utilizando SQLite para mantener las cosas sencillas y mágicas. Sin embargo, al subir a producción, hacemos la transición a PostgreSQL para ofrecer un rendimiento robusto y confiable. ¡La magia continúa en ambos casos!

Para explorar más detalles y realizar pruebas interactivas, accede a nuestra [documentación en vivo](http://127.0.0.1:8000/adopt/docs/). ¡Que cada rincón de tu código resuene con el suave murmullo de patitas y la calidez de hogares recién encontrados! 🌈🐱 #AdoptaMagia #APIdeGatitos

![Michi Navideño](https://c0.wallpaperflare.com/preview/755/291/651/nice-cat-animal-portrait.jpg)
