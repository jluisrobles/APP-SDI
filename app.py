import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import os

# Función para detectar tecnología
def detect_technology(domain):
    urls_to_try = [f"http://{domain}", f"https://{domain}"]
    for url in urls_to_try:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            html_content = soup.prettify().lower()
            if 'prestashop' in html_content:
                return "PrestaShop", url
            if 'wp-content' in html_content or 'wp-includes' in html_content:
                return "WordPress", url
            if 'woocommerce' in html_content:
                return "WooCommerce", url
            if 'mage' in html_content or 'varien' in html_content or 'magento' in html_content:
                return "Magento", url
            if 'cdn.shopify' in html_content or 'shopify' in html_content:
                return "Shopify", url
            if 'joomla' in html_content or 'jfactory' in html_content:
                return "Joomla", url
            if 'wix.com' in html_content or 'wixstatic' in html_content:
                return "Wix", url
            if 'squarespace' in html_content:
                return "Squarespace", url
            if 'salesforce' in html_content:
                return "Salesforce", url
            if 'logicommerce' in html_content:
                return "Logicommerce", url
            if 'odoo' in html_content:
                return "Odoo", url
        except requests.RequestException:
            continue
    return "Otra", None

# Función para procesar cada fila del DataFrame
def process_row(row):
    empresa = row['Empresa']
    dominio = row['Dominio']
    tech, final_url = detect_technology(dominio)
    return {
        'Empresa': empresa,
        'Dominio': dominio,
        'Tecnología Usada': tech,
        'URL Verificada': final_url if final_url else 'No disponible'
    }

# Interfaz de usuario con Streamlit
st.title('Detección de Tecnologías Web')

# Explicación del formato del archivo
st.markdown("""
### Formato del Archivo Excel
El archivo debe contener las siguientes columnas:
- **Empresa**: Nombre de la empresa.
- **Dominio**: Dominio web de la empresa.
""")

# Subir archivo Excel
uploaded_file = st.file_uploader("Sube tu archivo Excel con los dominios", type=["xlsx"])

# Elegir carpeta para guardar resultados
output_folder = st.text_input("Carpeta donde guardar los resultados", value="C:\\Users\\roble\\Downloads")

if uploaded_file and output_folder:
    df = pd.read_excel(uploaded_file)
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_row, [row for index, row in df.iterrows()]))
    df_results = pd.DataFrame(results)
    st.write(df_results)
    
    # Guardar resultados en la carpeta especificada
    output_path = os.path.join(output_folder, 'resultado_Empresas-Dominio.xlsx')
    df_results.to_excel(output_path, index=False)
    st.success(f'Verificación completada y archivo guardado en {output_path}.')

# Pie de página
st.markdown("""
---
by J Robles
""")