# CER2 - Fundación Patrimonio Vivo

Aplicación web en Django para el catálogo digital de lugares patrimoniales de Chile.
##administrador
**Administrador:** `admin` / `Admin2026*`
## Instalación de dependencias

```
python -m venv venv
venv\Scripts\activate          (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

## Configuración de la base de datos

Se usa SQLite (viene incluida en Django, no requiere instalar nada más).

```
python manage.py makemigrations catalogo
python manage.py migrate
python manage.py createsuperuser
```

## Ejecutar la aplicación

```
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Cargar datos y usuarios

Entrar a http://127.0.0.1:8000/admin/ con el superusuario y:

1. Crear Categorías (ej: Edificios históricos, Monumentos, Murales).
2. Crear Lugares patrimoniales (en `imagen` pegar una URL, ej: https://picsum.photos/seed/moneda/800/500).
3. Crear un usuario `editor` (clave: `Patrimonio2026*`) y en "Permisos de usuario" agregar:
   `catalogo | lugar patrimonial | Can add` y `Can change`.
4. Crear un usuario `lector` (clave: `Patrimonio2026*`) sin permisos.

## Secciones según tipo de usuario

- Anónimo: Inicio, Catálogo, Detalle, filtro por categoría, Iniciar sesión.
- Autenticado: además ve Gestión y Cerrar sesión.
- Autenticado con permisos: además puede agregar y editar lugares.
- Sin permisos que intente entrar a /gestion/agregar/ o /gestion/editar/<id>/ recibe error 403.
