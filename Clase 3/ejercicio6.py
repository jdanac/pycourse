lista_estudiantes = [
    {
    "nombre": "Andrés",
    "apellido": "Gómez",
    "edad": 22,
    "cursos": [
        {
        "nombre": "Introducción a la Programación",
        "creditos": 4,
        "nota": 88
        },
        {
        "nombre": "Matemáticas I",
        "creditos": 3,
        "nota": 92
        }]
    },
    {
    "nombre": "Ileym",
    "apellido": "Ramírez",
    "edad": 19,
    "cursos": [
        {
        "nombre": "Introducción a la Programación",
        "creditos": 4,
        "nota": 95
        },
        {
        "nombre": "Inglés I",
        "creditos": 2,
        "nota": 90
        }]
    },
    {
    "nombre": "Steven",
    "apellido": "Pérez",
    "edad": 21,
    "cursos": [
        {
        "nombre": "Matemáticas I",
        "creditos": 3,
        "nota": 78
        },
        {
        "nombre": "Inglés I",
        "creditos": 2,
        "nota": 85
        }]
}]

print("Promedio por clase:")
cursos_promedio = {}

for estudiante in lista_estudiantes:
    for curso in estudiante["cursos"]:
        nombre_curso = curso["nombre"]
        nota = curso["nota"]
        
        if nombre_curso not in cursos_promedio:
            cursos_promedio[nombre_curso] = {"total_notas": 0, "cantidad": 0}
        
        cursos_promedio[nombre_curso]["total_notas"] += nota
        cursos_promedio[nombre_curso]["cantidad"] += 1

for curso, datos in cursos_promedio.items():
    promedio = datos["total_notas"] / datos["cantidad"]
    print(curso + ": " + str(promedio))
