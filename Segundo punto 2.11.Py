class ArticuloCientifico:
    def __init__(self, titulo, autor, palabras_claves=None, publicacion=None, ano=None, resumen=None):
        # 1. Lógica del "Primer Constructor" (Parámetros obligatorios)
        self.titulo = titulo
        self.autor = autor
        # 2. Lógica del "Segundo Constructor" (Si se envían estos parámetros)
        # Si no se envían, se asignan valores por defecto vacíos o nulos
        self.palabras_claves = palabras_claves if palabras_claves is not None else []
        self.publicacion = publicacion if publicacion is not None else "No especificada"
        self.ano = ano if ano is not None else "Desconocido"
        # 3. Lógica del "Tercer Constructor" (Si se envía el resumen)
        self.resumen = resumen if resumen is not None else "Sin resumen"

    def imprimir(self):

        print("\n" + "#" * 40)
        print("DATOS DEL ARTÍCULO CIENTÍFICO")
        print("#" * 40)
        print(f"Título del artículo = {self.titulo}")
        print(f"Autor del artículo  = {self.autor}")
        print("Palabras clave      =")
        if self.palabras_claves:
            for palabra in self.palabras_claves:
                print(f"  - {palabra}")
        else:
            print("  (No especificadas)")
        print(f"Publicación         = {self.publicacion}")
        print(f"Año                 = {self.ano}")
        print(f"Resumen             = {self.resumen}")
        print("-" * 40 + "\n")


def iniciar_consola():
    while True:
        print("_________________________________________")
        print("   SISTEMA DE ARTÍCULOS CIENTÍFICOS   ")
        print("_________________________________________")
        print("1. Registrar artículo (Solo Título y Autor)")
        print("2. Registrar artículo (+ Palabras Clave, Publicación y Año)")
        print("3. Registrar artículo (Completo con Resumen)")
        print("4. Salir del programa")
        print("_________________________________________")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '4':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
            
        if opcion not in ['1', '2', '3']:
            print("Opción no válida. Por favor, intente de nuevo.\n")
            continue
            
        # Pedimos los datos básicos que SIEMPRE se necesitan
        titulo = input("Ingrese el título del artículo: ")
        autor = input("Ingrese el autor del artículo: ")
        
        if opcion == '1':
            # Instanciación equivalente al Primer Constructor
            articulo = ArticuloCientifico(titulo, autor)
            articulo.imprimir()
            
        elif opcion == '2':
            print("Ingrese 3 palabras clave:")
            palabras = []
            for i in range(3):
                palabras.append(input(f"  Palabra {i+1}: "))
                
            publicacion = input("Ingrese la publicación: ")
            
            try:
                ano = int(input("Ingrese el año (ej. 2023): "))
            except ValueError:
                ano = 0
                print("  [!] Año inválido, se asignó 0.")
                
            # Instanciación equivalente al Segundo Constructor
            articulo = ArticuloCientifico(titulo, autor, palabras, publicacion, ano)
            articulo.imprimir()
            
        elif opcion == '3':
            print("Ingrese 3 palabras clave:")
            palabras = []
            for i in range(3):
                palabras.append(input(f"  Palabra {i+1}: "))
                
            publicacion = input("Ingrese la publicación: ")
            
            try:
                ano = int(input("Ingrese el año (ej. 2023): "))
            except ValueError:
                ano = 0
                print("  [!] Año inválido, se asignó 0.")
                
            resumen = input("Ingrese el resumen: ")
            
            # Instanciación equivalente al Tercer Constructor
            articulo = ArticuloCientifico(titulo, autor, palabras, publicacion, ano, resumen)
            articulo.imprimir()


# Punto de entrada de la aplicación
if __name__ == "__main__":
    iniciar_consola()
