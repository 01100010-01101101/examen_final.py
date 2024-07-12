import random
import csv
import math

trabajadores = [
    {"nombre": "Juan Pérez", "cargo": "Consultor TI"},
    {"nombre": "María García", "cargo": "Analista"},
    {"nombre": "Carlos López", "cargo": "Programador"},
    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernández", "cargo": "Analista"},
    {"nombre": "Miguel Sánchez", "cargo": "Programador"},
    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernández", "cargo": "Analista"}
]

sueldos = [random.randint(300000, 2500000) for _ in range(10)]

def condicion_menor_800000(sueldo):
    return sueldo < 800000

def condicion_entre_800000_y_2000000(sueldo):
    return 800000 <= sueldo <= 2000000

def condicion_mayor_2000000(sueldo):
    return sueldo > 2000000

while True:
    opcion = int(input("\nMenu:\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas\n4. Generar reporte de sueldos\n5. Salir del programa\nSeleccione una opción: "))
    match opcion:
        case 1:
            sueldos = [random.randint(300000, 2500000) for _ in range(10)]
            print("Sueldos asignados aleatoriamente.")
        case 2:
            rangos = [
                ("menores a $800.000", condicion_menor_800000), 
                ("entre $800.000 y $2.000.000", condicion_entre_800000_y_2000000), 
                ("superiores a $2.000.000", condicion_mayor_2000000)
            ]
            for descripcion, condicion in rangos:
                seleccionados = [sueldo for sueldo in sueldos if condicion(sueldo)]
                print(f"Sueldos {descripcion} TOTAL:", len(seleccionados))
                for trabajador, sueldo in zip(trabajadores, sueldos):
                    if condicion(sueldo):
                        print(f"Nombre: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo: ${sueldo}")
            print("\nTOTAL SUELDOS:", sum(sueldos))
        case 3:
            max_sueldo, min_sueldo = max(sueldos), min(sueldos)
            avg_sueldo = sum(sueldos) / len(sueldos)
            geom_sueldo = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
            print(f"Sueldo más alto: ${max_sueldo}\nSueldo más bajo: ${min_sueldo}\nPromedio: ${avg_sueldo:.2f}\nMedia geométrica: ${geom_sueldo:.2f}")
        case 4:
            with open('reporte_sueldos.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nombre", "Cargo", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
                for trabajador, sueldo in zip(trabajadores, sueldos):
                    descuento_salud, descuento_afp = sueldo * 0.07, sueldo * 0.12
                    sueldo_liquido = sueldo * 0.81
                    writer.writerow([trabajador["nombre"], trabajador["cargo"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
                    print(f"Nombre: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo Base: ${sueldo} Descuento Salud: ${descuento_salud:.2f} Descuento AFP: ${descuento_afp:.2f} Sueldo Líquido: ${sueldo_liquido:.2f}")
        case 5:
            print("Finalizando programa…\nDesarrollado por Marco Alvial\nRUT: 19134106-6")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")