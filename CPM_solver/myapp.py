
from criticalpath import Node
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyappLayout(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.varubicacion = ''
        self.vardia = ''
        self.varmes = ''
        self.varanio = ''
        self.varids = ''
        
    def obtener_ubicacion(self):
        self.varubicacion = self.ids.ubicacion.text
        
    def obtener_dia(self):
        self.vardia = self.ids.dia.text
        
    def obtener_mes(self):
        self.varmes = self.ids.mes.text
        
    def obtener_anio(self):
        self.varanio = self.ids.anio.text
        
    def mostrar_texto(self,texto = ''):
        self.ids.output.text += f'\n{texto}'

    def info(self):
        self.mostrar_texto('''
============= PROYECTO PORYGON ==============
        
Hecho por: Abdiel Hernandez
        
Mira el programa, codigo e instrucciones en:
https://github.com/abdzher/ProyectoPorygon

                           ''')
        
    def comienzo(self):
        comprobacion = []
        self.mostrar_texto('\n')
        try:
            ubicacion = self.varubicacion
            df = pd.read_csv(ubicacion)
        except ValueError:
            self.mostrar_texto(f'{ubicacion} no es una ubicacion valida.')
        except FileNotFoundError:
            self.mostrar_texto(f'{ubicacion} no es una ubicacion valida.')
        else:
            self.mostrar_texto(f'Ubicacion correcta.')
            comprobacion.append(True)
        
        try:
            anio = int(self.varanio)
        except UnboundLocalError:
            self.mostrar_texto(f'{self.varanio} no es un año valido.')
        except ValueError:
            self.mostrar_texto(f'{self.varanio} no es un año valido.')
        else:
            self.mostrar_texto(f'Año correcto.')
            comprobacion.append(True)
        
        try:
            mes = int(self.varmes)
        except ValueError:
            self.mostrar_texto(f'{self.varmes} no es un mes valido.')
        else:
            if mes not in range(1,13):
                self.mostrar_texto(f'{mes} no es un mes valido.')
            else:
                self.mostrar_texto(f'Mes correcto.')
                comprobacion.append(True)
        
        try:
            dia = int(self.vardia)
        except ValueError:
            self.mostrar_texto(f'{self.vardia} no es un dia valido.')
        else:
            if dia not in range(1,32):
                self.mostrar_texto(f'{dia} no es un dia valido.')
            else:
                self.mostrar_texto(f'Dia correcto.')
                comprobacion.append(True)
        
        if comprobacion == [True,True,True,True]:
            self.iniciar(ubicacion, dia, mes, anio)
        
    


    def iniciar(self, ubicacion = '', dia_inicio = 13, mes_inicio = 10, anio_inicio = 2023):
        p = Node('MiProyecto')
        
        dataframe = pd.read_csv(ubicacion)
        largo = dataframe.shape[0]
        
        tareas = []
        letras = []
        duraciones = []
        
        for i in range(0 , largo):
            letra = dataframe.iloc[i,0]
            duracion = {'duracion': int(dataframe.iloc[i,2])}
            tareas.append(tuple((letra,duracion)))
            letras.append(letra)
            duraciones.append(float(dataframe.iloc[i,2]))
        
        dependencias = []
        
        for i in range(0,largo):
            x = str(dataframe.iloc[i,1])
            x = x.split(' ')

            if x == ['nan']:
                continue
            else:
                for k in x:
                    dependencias.append((k,letras[i]))
        
        for i in tareas:
            p.add(Node(i[0],duration=i[1]['duracion']))
        
        for i in dependencias:
            p.link(i[0],i[1])
        
        p.update_all()
        
        ruta_critica = (str(i) for i in p.get_critical_path())
        duracion_total = p.duration
        
        fecha_inicio = datetime.date(anio_inicio, mes_inicio, dia_inicio)
        
        calendario = pd.DataFrame([dict(Tarea = key, 
                                    Inicio = fecha_inicio, 
                                    Fin = fecha_inicio + datetime.timedelta(val['duracion']), 
                                    Status = 'Actividad Normal')
                                for key, val in dict(tareas).items()])

        for key, val in dict(tareas).items():
            dep = [d for d in dependencias if d[1] == key]
            prev_tareas = [t[0] for t in dep]
            if prev_tareas:
                prev_fin = calendario[calendario.Tarea.isin(prev_tareas)]['Fin'].max()
                calendario.loc[calendario.Tarea == key, 'Inicio'] = prev_fin
                calendario.loc[calendario.Tarea == key, 'Fin'] = prev_fin + datetime.timedelta(val['duracion'])
                
        calendario.loc[calendario.Tarea.isin(ruta_critica), 'Status'] = 'Ruta Crítica'
        
        dias_inicio = []
        dias_fin = []
        diferencia = []
        for i in range(0,largo):
            di = (calendario.iloc[i,1] - fecha_inicio).days
            df = (calendario.iloc[i,2] - fecha_inicio).days
            dif = df - di
            dias_inicio.append(di)
            dias_fin.append(df)
            diferencia.append(dif)
        calendario['dias_inicio'] = dias_inicio
        calendario['dias_fin'] = dias_fin
        calendario['diferencia'] = diferencia
        
        
        calendario['color'] = calendario.apply(color, axis=1)
        fig, ax = plt.subplots(1, figsize=(16,6))
        ax.barh(calendario.Tarea, calendario.diferencia, left=calendario.dias_inicio, color=calendario.color)

        c_dict = {'Ruta crítica':'#E64646', 'Actividad normal':'#4F81BE'}
        leyenda = [Patch(facecolor=c_dict[i], label=i)  for i in c_dict]
        plt.legend(handles=leyenda)

        clipboard = calendario.copy()
        clipboard = clipboard.iloc[:,:-1]
        clipboard['Duracion'] = duraciones
        for i in range(0,largo):
            clipboard.iloc[i,1] = f'{calendario.iloc[i,1].strftime("%d/%m/%Y")}'
            clipboard.iloc[i,2] = f'{calendario.iloc[i,2].strftime("%d/%m/%Y")}'
        clipboard.to_clipboard(excel=True)
        self.mostrar_texto('¡Tabla copiada al portapapeles!')
        
        
        plt.show()






def color(row):
    c_dict = {'Ruta Crítica':'#E64646', 'Actividad Normal':'#4F81BE'}
    return c_dict[row['Status']]   






class Myapp(App):
    def build(self):
        return MyappLayout()






if __name__ == '__main__':
    Myapp().run()