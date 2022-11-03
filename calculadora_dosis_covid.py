# Autor: Juan Ribeiro 2022

import csv
import struct


class CalculadoraDosisCovid(object):
    def __init__(self):
        # Diccionarios que contendrán los datos de las dosis
        self.vacunados_por_provincia = {}
        self.vacunados_por_condicion = {}
        self.vacunados_por_genero = {}
        self.vacunados_en_general = {}

        # Teniendo en cuenta que a fines de 2022 se han reportado hasta séptima dosis
        # provincia, dosis_1, dosis_2, dosis_adicional, dosis_refuerzo, total_dosis
        self._formato_dosis_provincia = self.__obtener_cadena_formato(20)

        # condicion, dosis_1, dosis_2, dosis_adicional, dosis_refuerzo, total_dosis
        self._formato_dosis_condicion = self.__obtener_cadena_formato(36)

        # genero, dosis_1, dosis_2, dosis_adicional, dosis_refuerzo, total_dosis
        self._formato_dosis_genero = self.__obtener_cadena_formato(4)

        # totales, dosis_1, dosis_2, dosis_adicional, dosis_refuerzo, total_dosis
        self._formato_dosis_totales = self.__obtener_cadena_formato(8)

    @staticmethod
    def __obtener_cadena_formato(len_categoria):
        return "%ds%ds%ds%ds%ds%ds%ds" % (len_categoria, 9, 9, 9, 9, 9, 9)

    def clasificar_dosis(self, archivo):
        """
        :param archivo: ruta del archivo

        Se carga un archivo .csv con datos de las dosis de vacuna contra el COVID aplicadas en Argentina, clasificando
        los mismos en diferentes categorias, guardandolos en diccionarios.
        """

        # Este atributo sólo servirá para poder monitorear la cantidad de líneas del archivo que se van leyendo
        # durante el transcurso de la ejecución.
        self.total = 0

        with open(archivo, "r", encoding="utf-8") as archivo_csv:
            lector = csv.DictReader(archivo_csv)

            for linea in lector:
                dosis = linea["nombre_dosis_generica"]
                provincia = linea["jurisdiccion_aplicacion"]
                condicion = linea["condicion_aplicacion"]
                genero = linea["sexo"]

                # Llamamos a un metodo que se encarga de ir agregando la dosis a su respectiva categoria
                self.__sumar_dosis_a_diccionario__(self.vacunados_por_provincia, dosis, provincia)
                self.__sumar_dosis_a_diccionario__(self.vacunados_por_condicion, dosis, condicion)
                self.__sumar_dosis_a_diccionario__(self.vacunados_por_genero, dosis, genero)
                self.__sumar_dosis_a_diccionario__(self.vacunados_en_general, dosis, "General")

                # Sientase libre de borrar estas dos líneas si no le interesa monitorear la ejecución
                self.total += 1
                print(self.total)

        # Calculamos los totales de cada categoria de una sola vez
        self.__calcular_dosis_totales_por_categoria__(self.vacunados_por_provincia)
        self.__calcular_dosis_totales_por_categoria__(self.vacunados_por_condicion)
        self.__calcular_dosis_totales_por_categoria__(self.vacunados_por_genero)
        self.__calcular_dosis_totales_por_categoria__(self.vacunados_en_general)

    @staticmethod
    def __sumar_dosis_a_diccionario__(diccionario, dosis, categoria):
        """
        :param diccionario: uno de los diccionarios atributos de la clase
        :param dosis: "1ra", "2da", "Adicional" o "Refuerzo"
        :param categoria: una provincia, condicion, genero o totales, según corresponda

        Agrega una dosis a la categoria que corresponda, en su diccionario correspondiente.
        """

        if categoria not in diccionario:
            diccionario[categoria] = {}

        if dosis not in diccionario[categoria]:
            diccionario[categoria][dosis] = 0

        diccionario[categoria][dosis] += 1

    @staticmethod
    def __calcular_dosis_totales_por_categoria__(diccionario):
        """
        :param diccionario: uno de los diccionarios atributos de la clase

        Simplemente asigna el valor a 'totales' a partir de las sumas de las dosis aplicadas en cada categoria.
        """
        for categoria, dosis in diccionario.items():
            cantidad_total_dosis_x_categoria = 0
            for cantidad in diccionario[categoria].values():
                cantidad_total_dosis_x_categoria += int(cantidad)
            diccionario[categoria]["Totales"] = cantidad_total_dosis_x_categoria

    @staticmethod
    def guardar_datos_por_categoria(archivo, diccionario, formato):
        """
        :param archivo: nombre del archivo que contiene o contendrá los registros
        :param diccionario: uno de los diccionarios atributos de la clase
        :param formato: uno de los formatos establecidos, atributos de la clase

        Metodo utilizado para guardar los datos almacenados en los diccionarios atributos de la clase
        en archivos de registro de longitud fija.
        """
        with open(archivo, "ab") as datos:
            for clave, valor in diccionario.items():
                datos.write(struct.pack
                            (formato,
                             clave.encode(),
                             str(valor["1ra"]).encode(),
                             str(valor["2da"]).encode(),
                             str(valor["Unica"]),
                             str(valor["Adicional"]),
                             str(valor["Refuerzo"]),
                             str(valor["Totales"]).encode()
                             )
                            )

    def guardar_datos(self):
        """
        Se guardan los datos de las cuatro categorias en registros de longitud fija, con los formatos establecidos
        """
        # Guardar datos de dosis aplicadas por provincia
        self.guardar_datos_por_categoria("datos_dosis_provincia", self.vacunados_por_provincia,
                                         self._formato_dosis_provincia)

        # Guardar datos de dosis aplicadas por condicion
        self.guardar_datos_por_categoria("datos_dosis_condicion", self.vacunados_por_condicion,
                                         self._formato_dosis_condicion)

        # Guardar datos de dosis aplicadas por genero
        self.guardar_datos_por_categoria("datos_dosis_genero", self.vacunados_por_genero, self._formato_dosis_genero)

        # Guardar datos de dosis aplicadas totales
        self.guardar_datos_por_categoria("datos_dosis_generales", self.vacunados_en_general,
                                         self._formato_dosis_totales)
