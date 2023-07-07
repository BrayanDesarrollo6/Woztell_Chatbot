# Librerias para el proceso del reporte horizontal
import pandas as pd
from xlsxwriter import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
from openpyxl import load_workbook
import sys

# Variables globales
# n_documento = sys.argv[1]

# Procesar mensaje
n_documento = "1026597187"
n_documento = n_documento.replace(" ", "%20")

# Perma Links
crear_empleado = "https://creatorapp.zohopublic.com/hq5colombia/compensacionhq5/xls/Reporte_de_Empleados_General/Tnq3UKDyevz83bx7VCdZBV1PYJ5HNVuHRKMSSvpTAR18R6aCOk32HZPNsWnRRHButMC9jAamCfBW5g6Js5z1GwNz0a34D18jvUwY"
aplicar_convocatorias = "https://creatorapp.zohopublic.com/hq5colombia/hq5/xls/APLICAR_CONVOCATORIAS_Report/D3GC1487tQ3axErQRgyRVQsdTkECTpaaF9XKHOz25UXv4Zd2RCAtBNG0VqRCr2eWxXGUh04fZsfRe3Z309RQP3sVx9qR9MKXXg2R"
hoja_vida = "https://creatorapp.zohopublic.com/hq5colombia/hq5/xls/HOJA_DE_VIDA_Report/TA0sfNwpGzfGRv0yTwVQgkn35KeyezDbaNKyk96mdHpO7DMTBgXDmQKXE59VRVPbrTEVR9ZHmVY0wzr9NeznTSdqgCnrSPQJ0wxF"

# Filters
filtro_documento_crear_empleado = "?Numero_de_Documento="
filtro_documento_aplicar_convocatorias = "?DOCUMENTO="
filtro_documento_hoja_vida = "?numero_documento_HV="

# Crear empleado
def consulta_crear_empleado():    
    print("Crear empleado")
    URL = crear_empleado + filtro_documento_crear_empleado + n_documento
    df = pd.read_excel(URL)
    df = pd.DataFrame(df)
    print(len(df))
    if df.empty == False:
        if len(df) == 1:
            nombre = df.iloc[0]['Nombre Completo']
            empresa = df.iloc[0]['Empresa']
            estado = df.iloc[0]['Estado Trabajador']
            print(nombre, empresa,estado)
            respuesta_consulta_registro()
    else:
        consultar_aplicar_convocatorias()

# Aplicar convocatorias
def consultar_aplicar_convocatorias():
    print("Aplicar convocatorias")
    URL = aplicar_convocatorias + filtro_documento_aplicar_convocatorias + n_documento
    df = pd.read_excel(URL)
    df = pd.DataFrame(df)
    print(len(df))
    if df.empty == False:
        if len(df) == 1:
            nombre = df.iloc[0]['Nombres y Apellidos']
            empresa = df.iloc[0]['Empresa usuaria']
            estado = df.iloc[0]['Estado postulación']
            print(nombre, empresa,estado)
            respuesta_consulta_registro()
    else:
        consulta_hoja_vida()

# HV
def consulta_hoja_vida():
    print("hoja de vida")
    URL = hoja_vida + filtro_documento_hoja_vida + n_documento
    df = pd.read_excel(URL)
    df = pd.DataFrame(df)
    print(len(df))
    if df.empty == False:
        if len(df) == 1:
            nombre = df.iloc[0]['Primer apellido'] + " " + df.iloc[0]['Segundo apellido'] + " " + df.iloc[0]['Primer nombre'] + " " + df.iloc[0]['Segundo nombre']
            documento = df.iloc[0]['Numero documento']
            print(nombre, documento)
            respuesta_consulta_registro()
    else:
        no_registrado()

# Usuario no registrado en el sistema
def no_registrado():
    print("No registrado")
    
def respuesta_consulta_registro():
    print("Enviando respuesta")

# Ejecución de consulta de numero de documento de la persona en el sistema
consulta_crear_empleado()