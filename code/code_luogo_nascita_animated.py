import geopandas as gpd
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/Passports_grouped.csv")
grouped_geo = gpd.GeoDataFrame(df, geometry=df.geometry, crs="epsg:4326")
grouped_geo = grouped_geo.sort_values(by="data_nascita_y")
grouped_geo = grouped_geo.rename(columns={"data_nascita_y": "data_nascita"})
center = grouped_geo.unary_union.centroid
token= "Your Mapbox token" 
                                 
fig = px.scatter_mapbox(grouped_geo,
                    lat="y",
                    lon="x",
                    hover_name="luogo_nascita", 
                    color="luogo_nascita",    
                    color_discrete_sequence=px.colors.qualitative.Pastel,
                    opacity=.6,
                    size="size",
                    hover_data={'Numero di emigranti':True,
                                'data_nascita_y':False, 
                                'y':False,
                                'x':False, 
                                'luogo_nascita':False, "size": False} ,                       
                    animation_frame="data_nascita_y")
                    
fig.update_layout(title="Luogo e data di nascita degli emigranti trentini",mapbox_style="light", mapbox_accesstoken=token,
                  mapbox_zoom=7, mapbox_center = {"lat": center.y, "lon": center.x})

fig.update_layout(margin={"r":40,"t":40,"l":0,"b":0})                               
                          
fig.write_html("Viz/luogo_nascita_animated.html")
