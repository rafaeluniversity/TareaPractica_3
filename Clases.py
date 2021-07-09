
class Bd_sintomas:

    def __init__(self):
        self.sintomas={}
    
    def añadirSintoma(self,nombre,posibles_enfermedades):
        self.sintomas[nombre]=posibles_enfermedades

    def datos(self):
        print("+-------------------------+----------------------------------------+")
        print("|Sintomas                 |Posibles enfermedades                   |")
        print("+-------------------------+----------------------------------------+")
        for i in self.sintomas:
            sintoma = i
            posibles_enfermedades =""
            for j in self.sintomas[i]:
                posibles_enfermedades=posibles_enfermedades+j+"  "
            cadena = "|{:<25}|{:<40}|".format(sintoma, posibles_enfermedades)
            print(cadena)
            print("+-------------------------+----------------------------------------+")


class Bd_enfermedades:

    def __init__(self):
        self.enfermedades={}
    
    def anadirEnfermedad(self, nombre, sintomas_necesarios):
        self.enfermedades[nombre]=sintomas_necesarios
        
    def datos(self):
        print("+-------------------------+----------------------------------------+")
        print("|Enfermedades             |Sintomas necesarios                     |")
        print("+-------------------------+----------------------------------------+")
        for i in self.enfermedades:
            sintoma = i
            posibles_enfermedades =""
            for j in self.enfermedades[i]:
                posibles_enfermedades=posibles_enfermedades+j+"  "
            cadena = "|{:<25}|{:<40}|".format(sintoma, posibles_enfermedades)
            print(cadena)
            print("+-------------------------+----------------------------------------+")



class Sintomatologia:

    def __init__(self,sintomas,enfermedades):
        self.sintomas_paciente = set()
        self.sintomas=sintomas
        self.enfermedades=enfermedades

    def sintomaAgregar(self, sintoma):
        self.sintomas_paciente.add(sintoma)

    def reiniciar(self):
        self.sintomas_paciente.clear()

    def diagnostico(self):
        enfermedad = []
        posibles_enfermedades=set()
        #primero debo agregar al conjunto posibles_enfermedades las enfermedades 
        #que podria tener el paciente segun los sintomas que presenta
        for i in self.sintomas_paciente:
            if i in self.sintomas:
                for j in self.sintomas[i]:
                    posibles_enfermedades.add(j)
        #verifico con cada posible enfermedad si su conjunto de sintomas 
        #es un subconjunto de sintomas_paciente, de ser asi se confirmaria
        #esa posible enfermedad y la agrego al vector enfermedad
        for i in posibles_enfermedades:
            if self.enfermedades[i].issubset(self.sintomas_paciente):
                enfermedad.append(i)
        
        return enfermedad

    def sintomaAusente(self,enfermedad_ingresada):
        enfermedad=set()
        enfermedad.add(enfermedad_ingresada)
        sintomas_ausente=set()
        posibles_enfermedades=set()
        #primero debo agregar al conjunto posibles_enfermedades las enfermedades 
        #que podria tener el paciente segun los sintomas que presenta
        for i in self.sintomas_paciente:
            if i in self.sintomas:
                for j in self.sintomas[i]:
                    posibles_enfermedades.add(j)
        # si la enfermedad esta entre la posibles enfermedades entonces retorno un 
        #vector con la diferencia de los conjuntos es decir los sintomas faltantes, 
        #caso contrario retorno None
        if enfermedad.issubset(posibles_enfermedades):
            sintomas_ausente=self.enfermedades[enfermedad_ingresada] - self.sintomas_paciente
            return list(sintomas_ausente)
        else:
            return None
    
    def reader(self,sintomas,enfermedades):
        sintomas.datos()
        print("\n\n")
        enfermedades.datos()
            

#insertamos los sintomas que se muestran en la tarea
all_sintomas=Bd_sintomas()
all_sintomas.añadirSintoma("fiebre",{"malaria","covid19"})
all_sintomas.añadirSintoma("escalofrio",{"malaria","covid19"})
all_sintomas.añadirSintoma("temblor_involuntario",{"malaria"})
all_sintomas.añadirSintoma("tos_seca",{"covid19"})
all_sintomas.añadirSintoma("dificultad_para_respirar",{"apnea","sobredosis_de_cafeina","asma"})
all_sintomas.añadirSintoma("somnolencia",{"apnea","trastorno_de_ansiedad"})
#insertamos las enfermedades que se muestran en la tarea
all_enfermedades=Bd_enfermedades()
all_enfermedades.anadirEnfermedad("covid19",{"tos_seca"})
all_enfermedades.anadirEnfermedad("malaria",{"fiebre","escalofrio"})
all_enfermedades.anadirEnfermedad("apnea",set())
all_enfermedades.anadirEnfermedad("sobredosis_de_cafeina",set())
all_enfermedades.anadirEnfermedad("asma",{"dificultad_para_respirar"})
all_enfermedades.anadirEnfermedad("trastorno_de_ansiedad",set())
# creo una instancia de la clase sintomatologia y le envio como parametros los diccionarios 
# de sintomas y enfermedades
sintomatologia=Sintomatologia(all_sintomas.sintomas,all_enfermedades.enfermedades)

#pruebas del programa
print("------- Prueba del programa con los pasos de la tabla 3 de la tarea --------")
sintomatologia.sintomaAgregar("fiebre")
print(sintomatologia.diagnostico())
print(sintomatologia.sintomaAusente("dengue"))
print(sintomatologia.sintomaAusente("apnea"))
print(sintomatologia.sintomaAusente("covid19"))
print(sintomatologia.sintomaAusente("malaria"))
sintomatologia.sintomaAgregar("escalofrio")
print(sintomatologia.diagnostico())
print(sintomatologia.sintomaAusente("apnea"))
print(sintomatologia.sintomaAusente("covid19"))
print(sintomatologia.sintomaAusente("malaria"))
sintomatologia.sintomaAgregar("dificultad_para_respirar")
print(sintomatologia.diagnostico())
print("------- Fin de la prueba --------\n")

print("------- Ejecucion del metodo Reader --------")
sintomatologia.reader(all_sintomas,all_enfermedades)



