import streamlit as st
import matplotlib.pyplot as plt
import tempfile
import os
import sys

# ── Ruta raíz del proyecto en el path ────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (
    calcular_tiempo_total,
    calcular_promedio_uso,
    calcular_uso_por_app,
)

# ── Configuración general de la página ───────────────────────────────────────
st.set_page_config(
    page_title="BehaviorTracker Dashboard",
    page_icon="📱",
    layout="wide",
)

st.title("📱 BehaviorTracker — Dashboard Interactivo")
st.markdown(
    "Cargá el archivo CSV de tu laboratorio para analizar el uso de "
    "aplicaciones por participante."
)
st.divider()

# ════════════════════════════════════════════════════════════════════════════
# PASO 1 — CARGA DINÁMICA DE DATOS
# ════════════════════════════════════════════════════════════════════════════
st.header("1 · Carga de datos")

archivo_subido = st.file_uploader(
    label="Arrastrá o seleccioná el archivo CSV",
    type=["csv"],
    help="El archivo debe tener las columnas: id_participante, fecha, app, cantidad_uso, tiempo_uso",
)

if archivo_subido is None:
    st.info("⬆️ Esperando archivo CSV para comenzar el análisis.")
    st.stop()

# ── Guardar el upload en un archivo temporal para que cargar_datos() lo lea ──
with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
    tmp.write(archivo_subido.getbuffer())
    ruta_tmp = tmp.name

# ════════════════════════════════════════════════════════════════════════════
# PASO 2 — PUENTE DE VALIDACIÓN DEFENSIVA
# ════════════════════════════════════════════════════════════════════════════
st.header("2 · Validación del archivo")

try:
    datos = cargar_datos(ruta_tmp)
except FileNotFoundError as e:
    st.error(f"❌ Archivo no encontrado: {e}")
    os.unlink(ruta_tmp)
    st.stop()
finally:
    # limpiamos el temporal en cualquier caso
    if os.path.exists(ruta_tmp):
        os.unlink(ruta_tmp)

try:
    datos_validos = validar_registro(datos)
except ValueError as e:
    st.error(f"🚨 El archivo no superó la validación:\n\n**{e}**")
    st.stop()

st.success("✅ Archivo válido. Podés continuar con el análisis.")

# ════════════════════════════════════════════════════════════════════════════
# PASO 3 — SELECCIÓN DE PARTICIPANTE
# ════════════════════════════════════════════════════════════════════════════
st.header("3 · Selección de participante")

ids_disponibles = sorted(datos_validos["id_participante"].unique().tolist())

id_buscado = st.selectbox(
    "Seleccioná el ID del participante:",
    options=ids_disponibles,
)

try:
    participante = filtrar_por_participante(datos_validos, id_buscado)
except ValueError as e:
    st.error(f"❌ {e}")
    st.stop()

# ════════════════════════════════════════════════════════════════════════════
# PASO 4 — KPIs (INDICADORES CLAVE)
# ════════════════════════════════════════════════════════════════════════════
st.header("4 · Indicadores clave (KPIs)")

try:
    tiempo_total = calcular_tiempo_total(participante)   # suma de tiempo_uso
    promedio     = calcular_promedio_uso(participante)   # media de cantidad_uso
    uso_apps     = calcular_uso_por_app(participante)    # Serie agrupada por app
except ValueError as e:
    st.error(f"❌ Error al calcular métricas: {e}")
    st.stop()

col1, col2, col3 = st.columns(3)

col1.metric(
    label="⏱ Tiempo total de uso",
    value=f"{tiempo_total:.1f} min",
)
col2.metric(
    label="📊 Promedio de cantidad de uso",
    value=f"{promedio:.2f}",
)
col3.metric(
    label="📱 Apps distintas usadas",
    value=int(uso_apps.shape[0]),
)

st.divider()

# ════════════════════════════════════════════════════════════════════════════
# PASO 5 — VISUALIZACIONES INTERACTIVAS
# ════════════════════════════════════════════════════════════════════════════
st.header("5 · Visualizaciones")

col_izq, col_der = st.columns(2)

# ── Gráfico 1: barras — uso por app ──────────────────────────────────────────
with col_izq:
    st.subheader(f"Uso por aplicación — Participante {id_buscado}")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    uso_apps.plot(kind="bar", ax=ax1, color="#4C9BE8", edgecolor="white")
    ax1.set_xlabel("Aplicación")
    ax1.set_ylabel("Cantidad de uso")
    ax1.set_title(f"Uso por app — ID {id_buscado}")
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

# ── Gráfico 2: líneas — evolución del tiempo de uso ──────────────────────────
with col_der:
    st.subheader(f"Evolución del tiempo de uso — Participante {id_buscado}")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    participante["tiempo_uso"].reset_index(drop=True).plot(
        kind="line", ax=ax2, color="#E8834C", marker="o"
    )
    ax2.set_xlabel("Registro")
    ax2.set_ylabel("Tiempo de uso (min)")
    ax2.set_title(f"Evolución del tiempo — ID {id_buscado}")
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

# ── Datos crudos (expandible) ─────────────────────────────────────────────────
st.divider()
with st.expander("🔍 Ver datos crudos del participante seleccionado"):
    st.dataframe(participante.reset_index(drop=True), use_container_width=True)

st.caption("BehaviorTracker Dashboard · Desarrollado con Streamlit")
