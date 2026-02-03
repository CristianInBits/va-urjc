# Visión Artificial (URJC) — Prácticas

Repositorio de prácticas de la asignatura **Visión Artificial** usando **Python + OpenCV**.

---

## ✅ Requisitos

- **Windows 11**
- **Git Bash**
- **Python 3.x** (recomendado: 3.13+)
- (Opcional) **VS Code**

Comprueba Python:

```bash
python --version
py -V
````

---

## 📦 Setup del entorno (primera vez)

Desde la raíz del repo:

```bash
bash scripts/setup.sh
```

Después, activa el entorno virtual:

```bash
source ./activate.sh
```

> Nota: el script `setup.sh` crea `.venv` e instala dependencias, pero **no puede dejar el entorno activado** al terminar. Por eso se activa con `source ./activate.sh`.

---

## 🔁 Uso diario (cada vez que abras terminal)

1. Entra al repo:

```bash
cd ruta/a/va-urjc
```

1. Activa el entorno:

```bash
source ./activate.sh
```

1. Ejecuta scripts:

```bash
python src/p00_hola_opencv/main.py
```

Salir del entorno:

```bash
deactivate
```

---

## 🧪 Ejecutar la práctica 00 (Hola OpenCV)

1. Mete una imagen en:

```bash
src/p00_hola_opencv/data/
```

1. Asegúrate de que el script apunta al nombre correcto, por ejemplo:

```py
img_path = DATA / "foto.png"
```

1. Ejecuta:

```bash
python src/p00_hola_opencv/main.py
```

Salidas:

- Se muestran imágenes (original / gris / bordes)
- Se guardan resultados en:

```bash
src/p00_hola_opencv/output/
```

---

## 📁 Estructura del repositorio

```bash
va-urjc/
  activate.sh
  requirements.txt
  scripts/
    setup.sh
  src/
    p00_hola_opencv/
      main.py
      data/
      output/
```

- `data/`: entrada (imágenes, vídeos)
- `output/`: salidas generadas (resultados)

---

## 🧷 Dependencias

Las dependencias se fijan en `requirements.txt`.

Actualizar dependencias (si añades nuevas):

```bash
pip freeze > requirements.txt
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```
