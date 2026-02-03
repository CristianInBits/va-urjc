import cv2
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).parent / "data"
OUTPUT = Path(__file__).parent / "output"

def main():
    # Cambia el nombre por el archivo que metas en /data
    img_path = DATA / "foto.png"

    img_bgr = cv2.imread(str(img_path))
    if img_bgr is None:
        raise FileNotFoundError(f"No se pudo leer: {img_path}. ¿Existe el archivo?")

    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    # Guardar salida
    out_path = OUTPUT / "edges.png"

    # Guardar salidas
    out_original = OUTPUT / "original.png"
    out_gray = OUTPUT / "gray.png"
    out_edges = OUTPUT / "edges.png"

    if not cv2.imwrite(str(out_original), img_bgr):
        raise RuntimeError(f"No se pudo guardar: {out_original}")

    if not cv2.imwrite(str(out_gray), gray):
        raise RuntimeError(f"No se pudo guardar: {out_gray}")

    if not cv2.imwrite(str(out_edges), edges):
        raise RuntimeError(f"No se pudo guardar: {out_edges}")

    print(f"✅ Guardadas:\n- {out_original}\n- {out_gray}\n- {out_edges}")



    # Mostrar (matplotlib)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.title("Original (RGB)")
    plt.imshow(img_rgb)
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Gris")
    plt.imshow(gray, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Bordes (Canny)")
    plt.imshow(edges, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    print(f"✅ Guardado: {out_path}")

if __name__ == "__main__":
    main()
