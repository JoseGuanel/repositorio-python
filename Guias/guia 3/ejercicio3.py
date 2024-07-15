print()

pago_diurno = 12000
pago_nocturno = 16000


empleados = {
    'empleado1': {
        'Lunes': 'nocturno',
        'Martes': 'nocturno',
        'Miércoles': 'nocturno',
        'Jueves': 'diurno',
        'Viernes': 'diurno'
    },
    'empleado2': {
        'Martes': 'nocturno',
        'Miércoles': 'nocturno',
        'Jueves': 'nocturno',
        'Domingo': 'diurno'
    },
    'empleado3': {
        'Miércoles': 'diurno',
        'Jueves': 'diurno',
        'Viernes': 'diurno',
        'Sábado': 'nocturno',
        'Domingo': 'nocturno'
    }
}


for empleado, horarios in empleados.items():
    pago_semanal = 0
    for dia, turno in horarios.items():
        if turno == 'diurno':
            if dia == 'domingo':
                pago_dia = 10 * (pago_diurno + 2000)
            else:
                pago_dia = 10 * pago_diurno
        elif turno == 'nocturno':
            if dia == 'domingo':
                pago_dia = 10 * (pago_nocturno + 3000)
            else:
                pago_dia = 10 * pago_nocturno
        
        print(f"Empleado: {empleado}, Día: {dia}, Pago: {pago_dia} CLP")
        pago_semanal += pago_dia
    
    print(f"Total semanal para {empleado}: {pago_semanal} CLP")
    print()