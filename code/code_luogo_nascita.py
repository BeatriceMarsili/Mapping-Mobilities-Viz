import geopandas as gpd
import pandas as pd
import plotly.express as px
from shapely import wkt

df = pd.read_csv("data/Passports.csv")
geo_df = gpd.GeoDataFrame(df, geometry=df.geometry, crs="epsg:4326")
token = "your Mapbox Token"
center = geo_df.unary_union.centroid

fig = px.scatter_mapbox(geo_df,
                    lat="y",
                    lon="x",
                    hover_name="luogo_long", 
                    color="luogo_long",    
                    color_discrete_sequence=px.colors.qualitative.Pastel, 
                    size="Numero di emigranti",
                    opacity=.6,
                    hover_data={'Numero di emigranti':True,
                                'data_nascita':False, 
                                'y':False,
                                'x':False, 
                                'luogo_nascita':False, "luogo_long":False
                                })


fig.update_layout(title="Luogo di nascita degli emigranti trentini",mapbox_style="light", mapbox_accesstoken=token,
                  mapbox_zoom=7, mapbox_center = {"lat": center.y, "lon": center.x})

fig.update_layout(margin={"r":80,"t":40,"l":0,"b":0})

fig.write_html("luogo_nascita.html")

