import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guardar el inventario en un archivo CSV."""
    if not inventario:
        print("Inventario vacío. No se puede guardar.")
        return
    
    try:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            campos = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            if incluir_header:
                escritor.writeheader()
            for p in inventario:
                escritor.writerow(p)
        print(f"Inventario guardado en: {ruta}")
    except PermissionError:
        print("No tienes permisos para guardar en esa ubicación.")
    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta):
    """Cargar inventario desde CSV"""
    inventario_cargado = []
    filas_invalidas = 0
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            if lector.fieldnames != ["nombre", "precio", "cantidad"]:
                print("Archivo inválido: encabezado incorrecto.")
                return [], 0
            for fila in lector:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                try:
                    producto = {
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    }
                    if producto["precio"] < 0 or producto["cantidad"] < 0:
                        filas_invalidas += 1
                        continue
                    inventario_cargado.append(producto)
                except ValueError:
                    filas_invalidas += 1
                    continue
        return inventario_cargado, filas_invalidas
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return [], 0
    except UnicodeDecodeError:
        print("Error de codificación al leer el archivo.")
        return [], 0
    except Exception as e:
        print("Error inesperado al cargar:", e)
        return [], 0
