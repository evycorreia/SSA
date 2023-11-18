import csv

#crear una funcion con permisos solo de lectura 'r'
def read_csv(path):

#para evitar el error UnicodeDecodeError try...
    try:

        with open (path, 'r', encoding='ISO-8859-1') as csvfile:
           
            reader = csv.reader(csvfile, delimiter=',')
            # primera fila de forma manual
            header = next(reader)
            #para retornar lista con todos sus diccionarios
            data = []
            #print(header)
            for row in reader:
                #convertir de header y el row en un solo array de tuplas
                iterable = zip(header, row)
                #generar el diccionario a partir del iterable
                episode_dic = {key: value for key, value in iterable}
                #clave-valor
                data.append(episode_dic)
            return data
            """leer fila a fila separando con ******
             print('***' * 5)
                print(row)"""

    except UnicodeDecodeError:
        print('No se puso abrir el archivo con la codificación ISO-8859-1')       

#para ejecutar como script desde la terminal:
if __name__ == '__main__':
    data = read_csv('reporte_ventas.csv')
    print (data)