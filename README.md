# 🎓 Proyecto Académico - Introducción a Desarrollo Web

📊 Estado del proyecto:

✅ Completado - Fines educativos

---

## 📌 Descripción
Proyecto desarrollado como parte de formación académica para introducción al desarrollo web con Django. Incluye configuración básica para conexión con base de datos Oracle.

📑 Este proyecto incluye:

- ⚙️ Configuración básica de Django 
- 🧩 Modelos de ejemplo 
- 🖥️ Vistas basadas en funciones 
- 🔑 Sistema de autenticación estándar

---
## 🛠️ Tecnologías 

| Área          | Tecnologías |
|---------------|-------------|
| **Backend**   | [![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/) |
| **Base de Datos** | [![Oracle](https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white)](https://www.oracle.com/database/) |
| **Frontend**  | [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML) [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) |
| **Driver DB** | [![OracleDB](https://img.shields.io/badge/oracledb-F80000?style=flat-square&logo=oracle&logoColor=white)](https://pypi.org/project/oracledb/) |

---


## ⚙️ Instalación

1) Clonar repositorio ```git clone https://github.com/tu-usuario/proyecto-django.git```
2) Navegar al directorio: ```cd proyecto-django```
3) Configurar entorno virtual: ```python -m venv venv```
4) Activar entrorno virtual: ```.\venv\Scripts\activate```
5) Instalar dependencias: ```pip install -r requirements.txt```

---

## 🔧 Configuración de Base de Datos

Editar proyectoUno/settings.py:

```
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'localhost:1521/XE',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'OPTIONS': {
            'threaded': True,
            'encoding': 'UTF-8'
        }
    }
}
```
---

## 🚀 Ejecución

1) Aplicar migraciones: ```python manage.py migrate```
2) Iniciar el proyecto: ```python manage.py runserver```
3) Acceder al proyecto: ```http://localhost:8000```

---

## 📂 Estructura de directorios
```
proyectoUno/
├── __init__.py
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py
web/  # App principal
├── migrations/
├── templates/
├── admin.py
├── models.py
└── views.py
```
---
### 📦 Dependencias (requirements.txt)

```python
asgiref==3.8.1
cffi==1.17.1
cryptography==45.0.4
Django==5.2.3
oracledb==3.1.1
pycparser==2.22
sqlparse==0.5.3
tzdata==2025.2
```
