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
ANCHO_ETIQUETA = 26
ANCHO_DECIMAL = 3
ANCHO_PERMISOS = 7
ANCHO_CANAL_BINARIO = 8
ANCHO_CANAL_HEX = 2
ANCHO_ARGB_HEX = 8
ANCHO_RGB_HEX = 6

COMISION: Final[float] = 0.15
CERO_REAL = 0.0
PORCENTAJE: Final[int] = 100
MB: Final[int] = 1_000_000
MIB: Final[int] = 1_048_576
BITS_MENOR: Final[int] = 8
BITS_MAYOR: Final[int] = 16
BITS_ALFA: Final[int] = 24
MASCARA: Final[int] = 0xFF
MASCARA_BYTE = 0xFF
MASCARA_RGB = 0xFFFFFF
DESPLAZAMIENTO_ALFA = 24
DESPLAZAMIENTO_ROJO = 16
DESPLAZAMIENTO_VERDE = 8
DESPLAZAMIENTO_MAYOR = 16
DESPLAZAMIENTO_MENOR = 8
PORCENTAJE = 100
PERMISO_INTERNET: Final[int] = 0b0000001
PERMISO_NOTIFICACIONES: Final[int] = 0b0000010
PERMISO_CAMARA: Final[int] = 0b0000100
PERMISO_UBICACION: Final[int] = 0b0001000
PERMISO_CONTACTOS: Final[int] = 0b0010000
PERMISO_MICROFONO: Final[int] = 0b0100000
PERMISO_ALMACENAMIENTO: Final[int] = 0b1000000
SIN_BITS = 0


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------
def mostrar_fila(etiqueta: str, valor: object) -> None:
    """Muestra una etiqueta y su valor en columnas."""
    print(f"{etiqueta:<{ANCHO_ETIQUETA}}{valor}")


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
    """Muestra los permisos y calcula la máscara sin ubicación."""
    pide_internet = (PERMISOS & PERMISO_INTERNET) != SIN_BITS
    pide_notificaciones = (
        PERMISOS & PERMISO_NOTIFICACIONES
    ) != SIN_BITS
    pide_camara = (PERMISOS & PERMISO_CAMARA) != SIN_BITS
    pide_ubicacion = (PERMISOS & PERMISO_UBICACION) != SIN_BITS
    pide_contactos = (PERMISOS & PERMISO_CONTACTOS) != SIN_BITS
    pide_microfono = (PERMISOS & PERMISO_MICROFONO) != SIN_BITS
    pide_almacenamiento = (
        PERMISOS & PERMISO_ALMACENAMIENTO
    ) != SIN_BITS

    sin_ubicacion = PERMISOS & ~PERMISO_UBICACION

    print("PERMISOS")
    mostrar_fila("En binario:", f"{PERMISOS:0{ANCHO_PERMISOS}b}")
    mostrar_fila("Internet:", pide_internet)
    mostrar_fila("Notificaciones:", pide_notificaciones)
    mostrar_fila("Cámara:", pide_camara)
    mostrar_fila("Ubicación:", pide_ubicacion)
    mostrar_fila("Contactos:", pide_contactos)
    mostrar_fila("Micrófono:", pide_microfono)
    mostrar_fila("Almacenamiento:", pide_almacenamiento)
    mostrar_fila(
        "Sin ubicación:",
        f"{sin_ubicacion:0{ANCHO_PERMISOS}b}",
    )


def opcion_6_color() -> None:
    """Descompone el color ARGB y muestra su equivalente CSS."""
    alfa = (COLOR_ICONO >> DESPLAZAMIENTO_ALFA) & MASCARA_BYTE
    rojo = (COLOR_ICONO >> DESPLAZAMIENTO_ROJO) & MASCARA_BYTE
    verde = (COLOR_ICONO >> DESPLAZAMIENTO_VERDE) & MASCARA_BYTE
    azul = COLOR_ICONO & MASCARA_BYTE

    opacidad = alfa / MASCARA_BYTE * PORCENTAJE
    color_rgb = COLOR_ICONO & MASCARA_RGB

    print("COLOR DEL ICONO")
    mostrar_fila(
        "ARGB:",
        f"0x{COLOR_ICONO:0{ANCHO_ARGB_HEX}X}",
    )
    mostrar_fila(
        "Rojo:",
        f"{rojo:>{ANCHO_DECIMAL}} "
        f"{rojo:0{ANCHO_CANAL_BINARIO}b} "
        f"{rojo:0{ANCHO_CANAL_HEX}X}",
    )
    mostrar_fila(
        "Verde:",
        f"{verde:>{ANCHO_DECIMAL}} "
        f"{verde:0{ANCHO_CANAL_BINARIO}b} "
        f"{verde:0{ANCHO_CANAL_HEX}X}",
    )
    mostrar_fila(
        "Azul:",
        f"{azul:>{ANCHO_DECIMAL}} "
        f"{azul:0{ANCHO_CANAL_BINARIO}b} "
        f"{azul:0{ANCHO_CANAL_HEX}X}",
    )
    mostrar_fila("Opacidad:", f"{opacidad:.1f} %")
    mostrar_fila("Para CSS:", f"#{color_rgb:0{ANCHO_RGB_HEX}X}")


def opcion_7_tipos() -> None:
    """Muestra tipos y valores, incluidas conversiones de datos."""
    media = ESTRELLAS / VALORACIONES
    pide_camara = (PERMISOS & PERMISO_CAMARA) != SIN_BITS
    texto_descargas = str(DESCARGAS)

    mayor_desplazada = VERSION_MAYOR << DESPLAZAMIENTO_MAYOR
    menor_desplazada = VERSION_MENOR << DESPLAZAMIENTO_MENOR
    codigo = mayor_desplazada | menor_desplazada | VERSION_PARCHE

    # int + float produce un resultado float.
    descargas_float = DESCARGAS + 0.0

    print("TIPOS DE DATOS")
    mostrar_fila("NOMBRE:", f"{type(NOMBRE)} {NOMBRE}")
    mostrar_fila("DESCARGAS:", f"{type(DESCARGAS)} {DESCARGAS}")
    mostrar_fila("PRECIO:", f"{type(PRECIO)} {PRECIO}")
    mostrar_fila("media:", f"{type(media)} {media}")
    mostrar_fila("pide_camara:", f"{type(pide_camara)} {pide_camara}")
    mostrar_fila(
        "texto_descargas:",
        f"{type(texto_descargas)} {texto_descargas}",
    )
    mostrar_fila("codigo:", f"{type(codigo)} {codigo}")
    mostrar_fila(
        "descargas_float:",
        f"{type(descargas_float)} {descargas_float}",
    )


def opcion_8_redondeo() -> None:
    """Compara los dos tipos de redondeo."""
    media = calcular_media()
    decimal = Decimal(ESTRELLAS) / Decimal(VALORACIONES)
    escolar_1 = decimal.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    escolar_2 = decimal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print("REDONDEO DE LA VALORACIÓN MEDIA")
    mostrar("Valor exacto:", media)
    mostrar("round(), 1 dec.:", round(media, 1))
    mostrar("Escolar, 1 dec.:", escolar_1)
    mostrar("round(), 2 dec.:", round(media, 2))
    mostrar("Escolar, 2 dec.:", escolar_2)


def opcion_9_ficha() -> None:
    """Muestra juntas las primeras cuatro opciones."""
    print("=" * ANCHO)
    print(f"{'FICHA DE LA APLICACIÓN':^{ANCHO}}")
    print("=" * ANCHO)
    opcion_1_identificacion()
    print("-" * ANCHO)
    opcion_2_tamano()
    print("-" * ANCHO)
    opcion_3_ingresos()
    print("-" * ANCHO)
    opcion_4_version()
    print("=" * ANCHO)


def opcion_10_acerca_de() -> None:
    """Muestra los datos del programa."""
    print("ACERCA DE")
    print(__doc__)
    mostrar("Versión:", VERSION_PROGRAMA)
    mostrar("Autores:", AUTORES)
    mostrar("Python:", sys.version.split()[0])


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
