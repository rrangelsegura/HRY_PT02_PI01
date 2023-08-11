
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


# Carga de dataset para la funcion
nro_peliculas_x_idioma = pd.read_csv("Datos/nro_peliculas_x_idioma.csv")
drcion_anio_x_peli = pd.read_csv("Datos/drcion_anio_x_peli.csv")
nro_pels_avgrev_totrev_x_franq = pd.read_csv("Datos/nro_pels_avgrev_totrev_x_franq.csv")
movies_x_country = pd.read_csv("Datos/movies_x_country.csv")
pelis_rev_x_productora = pd.read_csv("Datos/pelis_rev_x_productora.csv")

    
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    '''Ingresas el idioma, retornando la cantidad de peliculas producidas en el mismo'''
    # Filtrar el DataFrame por idioma y obtener la cantidad correspondiente
    cantidad = nro_peliculas_x_idioma.loc[nro_peliculas_x_idioma['original_language'].str.lower() == idioma.lower(), 'cantidad'].values
    if len(cantidad) == 0:
        return {'idioma': idioma, 'cantidad': 0}
    else:
        return {'idioma': idioma, 'cantidad': str(cantidad[0])}


@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    '''Ingresas la pelicula, retornando la duracion y el año'''
    r_pelicula = drcion_anio_x_peli.loc[drcion_anio_x_peli['title'] == 'Toy Story', 'runtime':'releae_year']
    return {'pelicula':pelicula, 'duracion':str(r_pelicula.runtime[0]), 'anio':str(r_pelicula.release_year[0])}


@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    r_franquicia = nro_pels_avgrev_totrev_x_franq[nro_pels_avgrev_totrev_x_franq['belongs_to_collection']==franquicia]
    return {'franquicia':franquicia, 'cantidad':str(r_franquicia.nro_peliculas[0]), 'ganancia_total':str(r_franquicia.total_revenue[0]), 'ganancia_promedio':str(r_franquicia.average_revenue[0])}


@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    r_pais = movies_x_country[movies_x_country['pais'] == pais]
    if r_pais.empty:
        return {'pais': pais, 'cantidad': 'No data'}
    else:
        cantidad = str(r_pais.cantidad.iloc[0])
        return {'pais': pais, 'cantidad': cantidad}



@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    '''Ingresas la productora, entregandote el revunue total y la cantidad de peliculas que realizo '''
    r_productora = pelis_rev_x_productora[pelis_rev_x_productora['productora'] == productora]
    return {'productora':productora, 'revenue_total': str(r_productora.revenue[0]),'cantidad':str(r_productora.nro_peliculas[0])}

#
#@app.get('/get_director/{nombre_director}')
#def get_director(nombre_director:str):
#    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
#    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista'''
#    return {'director':nombre_director, 'retorno_total_director':respuesta, 
#    'peliculas':respuesta, 'anio':respuesta, 'retorno_pelicula':respuesta, 
#    'budget_pelicula':respuesta, 'revenue_pelicula':respuesta}
#
## ML
#@app.get('/recomendacion/{titulo}')
#def recomendacion(titulo:str):
#    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
#    return {'lista recomendada': respuesta}