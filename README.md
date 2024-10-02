# Password_Manager
> Proyecto propio de Gestor de contraseñas
---
## ¿Preguntas?
-  Cómo funciona un gestor de contraseñas?
-  Qué funciones serían necesarias para encriptar correctamente las contraseñas
-  Cómo hacemos el login con contraseña maestra de forma segura? Tanto almacenarla como a la hora de iniciar sesión
-  Sería posible agrupar de alguna forma sobre un sitio o URL todas las entradas disposinibles?
-  
## Tareas
- Necesitamos una BBDD SQLite para el almacenaje de la información
- Empezaremos haciendo la app para CLI --> interfaz básica para CLI
- Hashear contraseñas
- Login con contraseña maestra
- Generar contraseñas seguras aleatorias
- 
## Requisitos
- Queremos que el usuario pueda incluir información como: nombre del sitio web/app, URL, descripción...
- Poder buscar contraseñas por el nombre del sitio o por la URL
- Guardar contraseñas en la BBDD cifradas
- Poder conseguir las contraseñas de la BBDD
- Alguna función para copiarla directamente con algún shortcut o algo.

---
## Funcionalidades/Implementación
### Login
- Contraseña maestra
- Una vez se pasa por el login que se despliegue algún tipo de menú de opciones en la CLI para elegir qué se quiere realizar
- 
### Añadir entradas
- Datos a añadir para la entrada:
  - Nombre del sitio
  - URL
  - Email
  - Username
  - Contraseña
  - Descripción ?
- Guardar los datos relevantes en la BBDD encriptados
-  
### Consultar entradas
- Tenemos que poder buscar/filtrar la contraseña por:
  - Nombre del sitio
  - URL
  - Email
  - Username
- Desplegar todas las opciones que cumplen con el requisito del filtro
- En caso de que se quiera recuparar la contraseña de alguna de las opciones, preguntar de nuevo por la contraseña maestra
- Añadir algún tipo de flag para que copie la password en la clipboard directamente sin mostrarla en pantalla
- 
### Eliminar entradas
- Debe existir la opción de eliminar alguna entrada seleccionada con alguna flag o algo así
- Para confirmar la acción pedir de nuevo contraseña maestra
- Eliminar los datos de la BBDD relativos a esa entrada
- 