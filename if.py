import pandas as pd
data = pd.read_csv('BaseCaseiFood.csv')

data.info()
data[['id_loja','hora_data_pedido','atraso_pedido_seg']].loc[data['atraso_pedido_seg']==0]

data.describe()

data.loc[data['tempo_real_ate_restaurante_seg']<0]

