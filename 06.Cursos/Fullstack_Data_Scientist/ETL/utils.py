import pandas as pd

# Limpiar el código de la partida arancelaria 
def code_clean(x):
    code = str(x)
    
    if len(code) == 11:
        return code[:5]
    else:
        return code[:6]        
    
# Limpiar el código de la sección
def code_comm(x):
    code = str(x)
    
    if len(code) == 5:
        return code[:1]
    else:
        return code[:2]        
    
# Crear dataframes relacionales para columnas en concreto 
def create_dimension(df, id_name):
    list_keys = []
    value = 1

    for i in df:
        list_keys.append(value)
        value = value + 1

    return pd.DataFrame({
        id_name: list_keys,
        'values': df
    }) 