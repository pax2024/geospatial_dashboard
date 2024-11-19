import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = "Demonstration for the public tender of the city of Lüneburg"


logo = "FS-Logo_600dpi.png"


st.image(logo,width=300)

st.title("Testmap")


filepath = "https://geodienste.leipzig.de/l3/OpenData//wfs?VERSION=1.3.0&REQUEST=getFeature&typeName=OpenData%3Averkehrsraumeinschraenkungen&outputFormat=application/json"
# filepath = "https://geodienste.leipzig.de/l10/opendata/PR_Anlagen_Belegung_aktuell/MapServer/WFSServer?SERVICE=WFS&request=GetFeature&typeName=PR_Anlagen_Belegung_aktuell%3aPR_Anlagen_Belegung_aktuell&outputFormat=GEOJSON"

m = leafmap.Map(center=[51.33, 12.37], zoom=12)
# m.add_wms_layer(url="https://geodienste.leipzig.de/l3/OpenData/verkehrsraumeinschraenkungen_point/wfs?REQUEST=GetCapabilities&SERVICE=WFS", layers="Verkehrsraumeinschränkungen Punkte (WFS), Stadt Leipzig", name="Leipzig Verkehrsraumeinschränkungen ...", overlay=True,shown=True)
m.add_geojson(filepath, layer_name="Verkehrsraumeinschränkungen Leipzig")

m.to_streamlit(height=700)