# Detección de Tecnologías Web

Este proyecto es una herramienta que permite detectar las tecnologías utilizadas en los sitios web de empresas a partir de sus dominios. Está construido con **Streamlit** para la interfaz gráfica, usa **requests** y **BeautifulSoup** para analizar las páginas web, y guarda los resultados en un archivo Excel.

## Características

- **Detección automática** de tecnologías web como: WordPress, Shopify, Magento, Joomla, Wix, entre otras.
- **Interfaz gráfica** con Streamlit para subir archivos Excel y visualizar resultados.
- Guarda los resultados en un archivo Excel descargable.
- Detección rápida mediante el uso de **ThreadPoolExecutor** para manejar múltiples solicitudes al mismo tiempo.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes paquetes:

```bash
pip install streamlit requests beautifulsoup4 pandas openpyxl
