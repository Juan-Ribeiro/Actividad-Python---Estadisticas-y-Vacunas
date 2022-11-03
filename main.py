from calculadora_dosis_covid import CalculadoraDosisCovid

if __name__ == '__main__':
    nombre_archivo = "datos_nomivac_covid19.csv"
    calculadora = CalculadoraDosisCovid()
    calculadora.clasificar_dosis(nombre_archivo)
    guardar_datos("asd.pb", calculadora.vacunados_por_provincia, formato_provincia)

    print("Vacunados por provincia: ", calculadora.vacunados_por_provincia)
    print("Vacunados por condicion: ", calculadora.vacunados_por_condicion)
    print("Vacunados por genero: ", calculadora.vacunados_por_genero)
    print("Vacunados en general: ", calculadora.vacunados_en_general)
