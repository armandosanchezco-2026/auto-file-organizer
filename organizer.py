import os
import shutil
import argparse
from datetime import datetime

# Tipos de archivo por categoría
FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "audio": [".mp3", ".wav", ".aac", ".flac"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def get_category(extension):
    extension = extension.lower()
    for category, ext_list in FILE_TYPES.items():
        if extension in ext_list:
            return category
    return "others"

def organize_folder(path):
    if not os.path.isdir(path):
        print("❌ La ruta no es una carpeta válida.")
        return

    log = []

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        if os.path.isdir(full_path):
            continue

        _, ext = os.path.splitext(filename)
        category = get_category(ext)

        target_folder = os.path.join(path, category)
        os.makedirs(target_folder, exist_ok=True)

        new_path = os.path.join(target_folder, filename)
        shutil.move(full_path, new_path)

        log.append(f"{filename} → {category}")

    # Guardar log
    log_path = os.path.join(path, "organizer_log.txt")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n--- {datetime.now()} ---\n")
        for line in log:
            f.write(line + "\n")

    print("✔ Organización completada.")
    print(f"📄 Log guardado en: {log_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organizador automático de archivos")
    parser.add_argument("path", help="Ruta de la carpeta a organizar")
    args = parser.parse_args()

    organize_folder(args.path)
