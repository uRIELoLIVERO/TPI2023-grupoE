![App Screenshot](https://i.imgur.com/Der7ZHp.jpg)

# Trabajo Práctico Integrador - Análisis de Sistemas de Información

**Alumnos:**

- Fermani, Julián.
- Anil, Facundo.
- Lelli, Matias.
- Massietti, Alexander.
- Olivero, Uriel.
- Doglio, Ramiro.

## Introducción

Este repositorio alberga el Trabajo Práctico Integrador desarrollado en el marco de la asignatura "Análisis de Sistemas de Información" de la Universidad Tecnológica Nacional - Facultad Regional Villa María. En este proyecto, hemos abordado el desafío de analizar, modelar y programar un sistema de información destinado a la gestión de la cantina de nuestra facultad.

## Objetivos

Los objetivos principales de este proyecto son los siguientes:

1. Realizar un análisis exhaustivo de los procesos operativos de la cantina.
2. Diseñar un modelo de datos que permita gestionar eficazmente las operaciones de la cantina, incluyendo el inventario de productos, la gestión de pedidos y el control de ventas.
3. Desarrollar una aplicación de software que implemente el modelo de datos y brinde a los usuarios la capacidad de realizar pedidos, consultar menús y administrar su cuenta.
4. Aplicar y la relacionar los contenidos desarrollados a lo largo del programa de la cátedra e integrar los conocimientos adquiridos en las materias verticales y horizontales.

## Previsualizacion
##### Laptop
https://github.com/uRIELoLIVERO/TPI2023-grupoE/assets/134315672/faf77dce-3410-4080-872f-9309e105ca48

##### Mobile
https://github.com/uRIELoLIVERO/TPI2023-grupoE/assets/134315672/70b6cfde-ef42-4f6a-b9f6-6a7c905f72bc

## Estructura del Repositorio

Este repositorio está organizado de la siguiente manera:

- 📁 `Modelados`: Aquí se encuentran los modelados y cualquier otra documentación relacionada con el diseño del sistema (BPMN, Caso de Uso, Plantillas y diagrama de clases).
- 📁 `HTML, CSS, JS`: Contiene el código fuente de la aplicación desarrollada para la cantina.
- 📁 `PaginaCantina`: Es el contenedor de el entorno donde se hostea la pagina web, aqui mismo podemos encontrar todas las vistas y la logica de las mismas.

## Tecnologías Utilizadas

Para la implementación del sistema, hemos utilizado las siguientes tecnologías:

- 📱 Interfaz de usuario: HTML, CSS, JavaScript.
- 💻 Funcionalidad del servidor: Django, Ajax, Python, MySQLite.
- 📦 Control de versiones: Git y GitHub.
- ✅ Gestion de tares de trabajo: Trello

* * *
 >[!NOTE]
 >
 >Como hostear el servidor de forma local:
 >Configuración inicial:

### 1. Clonar el repositorio

    git clone <URL_del_repositorio>

### 2. Crear un entorno virtual

    python -m venv nombre_del_entorno

En Windows: nombre_del_entorno\Scripts\activate.

En macOS/Linux: source nombre_del_entorno/bin/activate.

### 3.Instalar Django y otras dependencias

    pip install django
    pip install -r requirements.txt

>[!IMPORTANT]
>
>Configuración de Django y ejecución del servidor:

### 1. Configurar el proyecto
Configura la base de datos en settings.py.

Crea un archivo .env para variables de entorno si es necesario.

### 2. Aplicar migraciones

    python manage.py makemigrations
    python manage.py migrate

### 3. Crear un superusuario (no es necesario)

    python manage.py createsuperuser
La base de datos cuenta con un usuario admin y contraseña admin

### 4. Ejecutar el servidor

    python manage.py runserver

Visita http://127.0.0.1:8000/ o http://localhost:8000/ en tu navegador.
