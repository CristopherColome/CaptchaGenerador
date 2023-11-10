## Generador de Captchas

Este es un simple generador de captchas en Python que utiliza la biblioteca PIL (Pillow) para crear imágenes con texto distorsionado y ruido. Estas imágenes pueden ser utilizadas para propósitos de verificación y autenticación.

### Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas antes de utilizar el generador:

```bash
pip install Pillow matplotlib numpy
```

### Estructura del Proyecto

- **fonts**: Directorio que contiene archivos de fuente utilizados para el texto en los captchas.

- **captcha_image_generator.py**: El script principal que define la clase `CaptchaImageGenerator`.

### Uso

```python
import glob
import os
import string
import random
import matplotlib.pyplot as plt

FONTS_DIR = "/content/drive/MyDrive/fonts"
DEFAULT_FONTS = glob.glob(os.path.join(FONTS_DIR, "*.*"))

CHARACTERS = string.digits + string.ascii_lowercase

generator = CaptchaImageGerator(fonts = DEFAULT_FONTS)

fig = plt.figure(figsize=(15, 5))
columns = 2
rows = 2

for i in range(1, columns * rows + 1):
    captcha_text = "".join(random.choice(CHARACTERS) for _ in range(5))
    captcha_image = generator.generate(captcha_text)
    fig.add_subplot(rows, columns, i)
    plt.imshow(captcha_image)

plt.show()
```

### Parámetros del Generador

- `width`: Ancho de la imagen captcha (por defecto: 150).
- `height`: Altura de la imagen captcha (por defecto: 50).
- `fonts`: Lista de rutas a archivos de fuente (por defecto: todas las fuentes en el directorio `fonts`).

### Método `generate(text)`

Genera una imagen captcha con el texto proporcionado. Retorna la imagen en formato PIL.

### Métodos de Modificación de Imagen

- `add_noise(image)`: Agrega puntos de ruido y aplica un desenfoque gaussiano.

- `add_text(image, text)`: Agrega el texto al centro de la imagen con una fuente aleatoria.

### Contribuciones

¡Siéntete libre de contribuir! Puedes agregar nuevas funcionalidades, mejorar la calidad del código o proponer ideas para hacer que este generador de captchas sea aún mejor.

### Atribuciones

- Este generador de captchas utiliza la biblioteca [Pillow](https://pillow.readthedocs.io/) para el procesamiento de imágenes.

---

Espero que esta documentación te sea útil. ¡Diviértete generando captchas!
