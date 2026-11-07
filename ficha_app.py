"""[Docstring del módulo: una sola línea que diga qué hace el programa.]"""

from typing import Final

# Añadid aquí las importaciones que necesitéis.
import sys
from decimal import Decimal, ROUND_HALF_UP
from typing import Final



# ---------------------------------------------------------------------------
# Datos de la aplicación. Sustituid los del ejemplo APP-00 por los vuestros.
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-06"
NOMBRE: Final[str] = "Recetas Rápidas"
PAQUETE: Final[str] = "es.cocina.recetasrapidas"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 2, 8, 4
TAMANO_APK: Final[int] = 57_671_680          # bytes
DESCARGAS: Final[int] = 18_200
PRECIO: Final[float] = 1.99                  # euros, IVA incluido
VALORACIONES: Final[int] = 1_200
ESTRELLAS: Final[int] = 5_340                # suma de todas las valoraciones
PERMISOS: Final[int] = 0b1000101
COLOR_ICONO: Final[int] = 0xFFD84315         # ARGB

# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "[usuario] · [usuario]"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 44
COMISION: Final[float] = 0.15
PORCENTAJE: Final[int] = 100
MB: Final[int] = 1_000_000
MIB: Final[int] = 1_048_576
BITS_MENOR: Final[int] = 8
BITS_MAYOR: Final[int] = 16
BITS_ALFA: Final[int] = 24
MASCARA: Final[int] = 0xFF
PERMISO_INTERNET: Final[int] = 0b0000001
PERMISO_NOTIFICACIONES: Final[int] = 0b0000010
PERMISO_CAMARA: Final[int] = 0b0000100
PERMISO_UBICACION: Final[int] = 0b0001000
PERMISO_CONTACTOS: Final[int] = 0b0010000
PERMISO_MICROFONO: Final[int] = 0b0100000
PERMISO_ALMACENAMIENTO: Final[int] = 0b1000000


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------

def mostrar(nombre: str, dato: object) -> None:
    print(f"{nombre:<20} {dato}")


def obtener_version() -> str:
    return f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"


def calcular_media() -> float:
    return ESTRELLAS / VALORACIONES

# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """Muestra los datos de la aplicación."""
    version = obtener_version()
    mostrar("Código:", CODIGO)
    mostrar("Nombre:", NOMBRE)
    mostrar("Paquete:", PAQUETE)
    mostrar("Versión:", version)


def opcion_2_tamano() -> None:
    """Calcula el tamaño del APK."""
    mb = TAMANO_APK / MB
    mib = TAMANO_APK / MIB
    diferencia = (mb - mib) / mb * PORCENTAJE
    print("TAMAÑO DEL APK")
    mostrar("Bytes:", f"{TAMANO_APK} B")
    mostrar("En la tienda:", f"{mb:.2f} MB")
    mostrar("En el móvil:", f"{mib:.2f} MiB")
    mostrar("Diferencia:", f"{diferencia:.1f} %")


def opcion_3_ingresos() -> None:
    """Calcula los ingresos de la aplicación."""
    bruto = DESCARGAS * PRECIO
    comision = bruto * COMISION
    neto = bruto - comision
    print("INGRESOS")
    mostrar("Descargas:", DESCARGAS)
    mostrar("Precio:", f"{PRECIO:.2f} €")
    mostrar("Ingresos brutos:", f"{bruto:.2f} €")
    mostrar("Comisión tienda:", f"{comision:.2f} €")
    mostrar("Ingresos netos:", f"{neto:.2f} €")


def opcion_4_version() -> None:
    """Calcula y descompone el versionCode."""
    codigo = (VERSION_MAYOR << BITS_MAYOR) | (VERSION_MENOR << BITS_MENOR)
    codigo = codigo | VERSION_PARCHE
    mayor = codigo >> BITS_MAYOR
    menor = (codigo >> BITS_MENOR) & MASCARA
    parche = codigo & MASCARA
    print("VERSIONCODE")
    mostrar("Versión:", obtener_version())
    mostrar("versionCode:", codigo)
    mostrar("En hexadecimal:", f"0x{codigo:06X}")
    mostrar("Desempaquetado:", f"{mayor}.{menor}.{parche}")

def opcion_5_permisos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_6_color() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_7_tipos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_8_redondeo() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_9_ficha() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_10_acerca_de() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


# ---------------------------------------------------------------------------
# Función principal y punto de entrada. Vienen hechos: no los modifiquéis.
# ---------------------------------------------------------------------------
def main() -> None:
    """Ejecuta las diez opciones, una detrás de otra."""
    print("--- Opción 1. Identificación de la app ---")
    opcion_1_identificacion()
    print("\n--- Opción 2. Tamaño del APK ---")
    opcion_2_tamano()
    print("\n--- Opción 3. Ingresos ---")
    opcion_3_ingresos()
    print("\n--- Opción 4. versionCode ---")
    opcion_4_version()
    print("\n--- Opción 5. Permisos ---")
    opcion_5_permisos()
    print("\n--- Opción 6. Color del icono ---")
    opcion_6_color()
    print("\n--- Opción 7. Tipos de datos ---")
    opcion_7_tipos()
    print("\n--- Opción 8. Redondeo de la valoración ---")
    opcion_8_redondeo()
    print("\n--- Opción 9. Ficha completa ---")
    opcion_9_ficha()
    print("\n--- Opción 10. Acerca de ---")
    opcion_10_acerca_de()


if __name__ == "__main__":
    main()
