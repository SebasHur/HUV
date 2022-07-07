def map_to_eps(s, df):
    df2 = df.copy()
    s = s.replace('Ñ', '�')
    s = f"responsable EPS_{s}"
    if s in df.columns:
        df2[s] = 1
    return df2

def map_to_cie(s, df):
    df2 = df.copy()
    s = s.replace('Ñ', '�')
    s = f"cie10 egrdin_{s}"
    if s in df.columns:
        df2[s] = 1
    return df2

def map_to_pos(s, df):
    df2 = df.copy()
    s = f"tipo POS_{s}"
    if s in df.columns:
        df2[s] = 1
    return df2

def map_gender(s, df):
    df2 = df.copy()
    s = f"genero - sexo_{'M' if s == 'MALE' else 'F'}"
    if s in df.columns:
        df2[s] = 1
    return df2