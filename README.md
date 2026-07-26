class Pedido:
    def calcular_pedido(self, *args):
        # 1. Caso: Un primer plato y una bebida (4 parámetros)
        if len(args) == 4:
            primer_plato, costo_primer_plato, bebida, costo_bebida = args
            total = costo_primer_plato + costo_bebida
            print(f"\n---> Resumen: El costo de {primer_plato} y {bebida} es = ${total:,.2f}")

        # 2. Caso: Primer plato, segundo plato y bebida (6 parámetros)
        elif len(args) == 6:
            primer_plato, costo_primer_plato, segundo_plato, costo_segundo_plato, bebida, costo_bebida = args
            total = costo_primer_plato + costo_segundo_plato + costo_bebida
            print(f"\n---> Resumen: El costo de {primer_plato} + {segundo_plato} + {bebida} es = ${total:,.2f}")

        # 3. Caso: Primer plato, segundo plato, postre y bebida (8 parámetros)
        elif len(args) == 8:
            (primer_plato, costo_primer_plato,
             segundo_plato, costo_segundo_plato,
             postre, costo_postre,
             bebida, costo_bebida) = args

            total = costo_primer_plato + costo_segundo_plato + costo_postre + costo_bebida
            print(f"\n---> Resumen: El costo de {primer_plato} + {segundo_plato} + {bebida} + {postre} es = ${total:,.2f}")

        else:
            print("\nError: Cantidad de parámetros no válida.")

def iniciar_consola():
    while True:
        print("\n" + "#"*49)
        print("      SISTEMA DE PEDIDOS RESTAURANTE      ")
        print("#"*49)
        print("1. Pedir: Primer Plato + Bebida")
        print("2. Pedir: Primer Plato + Segundo Plato + Bebida")
        print("3. Pedir: Primer Plato + Segundo Plato + Bebida + Postre")
        print("4. Salir del programa")
        print("#"*49)

        opcion = input("Seleccione el tipo de pedido (1-4): ")

        if opcion == '4':
            print("Saliendo del sistema de pedidos. ¡Hasta luego!")
            break

        if opcion not in ['1', '2', '3']:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue

        try:
            p_plato = input("Nombre del primer plato: ")
            c_p_plato = float(input(f"Costo de '{p_plato}': $"))

            bebida = input("Nombre de la bebida: ")
            c_bebida = float(input(f"Costo de '{bebida}': $"))

            pedido = Pedido()

            if opcion == '1':
                # Llamada sobrecargada 1
                pedido.calcular_pedido(p_plato, c_p_plato, bebida, c_bebida)

            elif opcion == '2':
                s_plato = input("Nombre del segundo plato: ")
                c_s_plato = float(input(f"Costo de '{s_plato}': $"))

                # Llamada sobrecargada 2
                pedido.calcular_pedido(p_plato, c_p_plato, s_plato, c_s_plato, bebida, c_bebida)

            elif opcion == '3':
                s_plato = input("Nombre del segundo plato: ")
                c_s_plato = float(input(f"Costo de '{s_plato}': $"))

                postre = input("Nombre del postre: ")
                c_postre = float(input(f"Costo de '{postre}': $"))

                # Llamada sobrecargada 3
                pedido.calcular_pedido(p_plato, c_p_plato, s_plato, c_s_plato, postre, c_postre, bebida, c_bebida)

        except ValueError:
            print("\n¡Error! Por favor, ingrese valores numéricos válidos para los costos.")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    iniciar_consola()
