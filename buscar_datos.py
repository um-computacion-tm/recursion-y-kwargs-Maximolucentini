import unittest


def buscar_datos(*args, **kwargs):
    args_set = set(args)

    for key, value in kwargs.items():
        values_set = set(value.values())
        
        if args_set == values_set:
            return key
    
    return None


database = {
    "persona1": {
        "primer_nombre": "Norma",
        "segundo_nombre": "Roxana",
        "primer_apellido": "Sanchez",
        "segundo_apellido": "Colombero"
    },
    "persona2": {
        "primer_nombre": "Pedro",
        "primer_apellido": "Arrigoni"
    },
    "persona3": {
        "primer_nombre": "Catalina",
        "primer_apellido": "Montanaro",
        "segundo_apellido": "Caroglio"
    },
    "persona4": {
        "primer_nombre": "Lionel",
        "segundo_nombre": "Andres",
        "primer_apellido": "Messi",
        "segundo_apellido": "Cuccittini"
    },
    "persona5": {
        "primer_nombre": "Juan",
        "segundo_nombre": "Roman",
        "primer_apellido": "Riquelme"
    }  
}      


class TestBuscarDatos(unittest.TestCase):
    def test_buscar_datos_persona1(self):
        result = buscar_datos("Norma", "Roxana", "Sanchez", "Colombero", **database)
        self.assertEqual(result, "persona1")

    def test_buscar_datos_persona2(self):
        result = buscar_datos("Pedro", "Arrigoni", **database)
        self.assertEqual(result, "persona2")
        
    def test_buscar_datos_persona3(self):
       result = buscar_datos("Catalina", "Montanaro", "Caroglio", **database)
       self.assertEqual(result, "persona3") 
       
    def test_buscar_datos_persona4(self):
       result = buscar_datos("Lionel", "Andres", "Messi", "Cuccittini", **database)
       self.assertEqual(result, "persona4") 
       
    def test_buscar_datos_persona5(self):
       result = buscar_datos("Juan", "Roman", "Riquelme", **database)
       self.assertEqual(result, "persona5")
         
    def test_buscar_datos_no_encontrado(self):
        result = buscar_datos("Carlos", "Alberto", **database)
        self.assertIsNone(result, None)
            

    
unittest.main()
       
