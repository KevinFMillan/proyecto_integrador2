import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
velConexionLocalidades = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Acc_vel_loc_sinrangos']) #velocidades especificas
velConexionProvincias = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Velocidad_sin_Rangos']) #velocidades especificas
mbpsBajadaPorvincias = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Velocidad % por prov'])
mbpsBajadaTrimestral = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Totales VMD'])
tipoConexion = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Accesos_tecnologia_localidad'])
tipoConexionTrimestral = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Totales Accesos Por Tecnología'])
tipoConexionProvincias = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Accesos Por Tecnología'])
dialBaf = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Dial-BAf'])
dialBafTrimestral = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Totales Dial-BAf'])
accesoPoblacionalPersonas = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Penetración-poblacion'])
accesoPoblacionalHogares = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Penetracion-hogares'])
accesoPoblacionalTrimestal = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Penetracion-totales'])
velInternetTrimestral = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Totales Accesos por velocidad']) #esta velocidad se mido por intervalos 
velInternetProvincias = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Accesos por velocidad']) #esta velocidad se mide por intervalos
ingresos = pd.read_excel(io='./data/Internet.xlsx',sheet_name=['Ingresos'])
print(ingresos)
