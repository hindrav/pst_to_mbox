import os
import subprocess
import sys

def convert_pst_to_mbox(pst_file, results_folder):
    try:
        subprocess.run(["readpst", "-o", results_folder, pst_file], check=True)
        print(f"Se han convertido los correos electrónicos de {pst_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir los correos electrónicos en {pst_file}: {e}")
        sys.exit(1)

    # Renombrar archivos de salida a .mbox
    for root, dirs, files in os.walk(results_folder):
        for file in files:
            if file.endswith(".contacts"):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, os.path.splitext(file)[0] + ".mbox")
                os.rename(old_path, new_path)
                print(f"Renombrado: {old_path} -> {new_path}")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python app.py")
        sys.exit(1)

    inputs_folder = "inputs_folder"  # Carpeta que contiene los archivos PST
    results_folder = "results_folder"  # Carpeta donde se guardarán los archivos MBOX

    if not os.path.exists(inputs_folder):
        print(f"La carpeta de entrada '{inputs_folder}' no existe.")
        sys.exit(1)

    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    pst_files = [f for f in os.listdir(inputs_folder) if f.endswith('.pst')]
    if not pst_files:
        print("No se encontraron archivos PST en la carpeta de entrada.")
        sys.exit(1)

    for pst_file in pst_files:
        convert_pst_to_mbox(os.path.join(inputs_folder, pst_file), results_folder)

    print("done!")
