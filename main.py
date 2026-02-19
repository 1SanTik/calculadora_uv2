from flask import Flask, request, random

app = Flask (__name__)

@app.route("/")
def home():
    return '''

<h1> Aplicación Calculadora </h1>

<p> Opciones disponibles </p>

<ul>

    <li><a href="suma?a=&b=12"> Suma </a>  </li>
    <li><a href="resta?a=8&b=12"> Resta  </a> </li>
    <li><a href="multiplicacion?a=8&b=12"> Multiplicación </a></li>
    <li><a href="division?a=8&b=12"> División </a></li>

</ul>

'''

#esta es una ruta adicional en la aplicación para la función suma
@app.route("/suma")
def ruta_suma():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a+b
    return f'''
    "La suma de los números {a} y {b} es: {resultado} "
    <p><a href="/">Volver a inicio</a></p>
'''
#esta es una ruta adicional en la aplicación para la función resta
@app.route("/resta")
def ruta_resta():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a-b
    return f'''
    "La resta de los números {a} y {b} es: {resultado} "
    <p><a href="/">Volver a inicio</a></p>
'''
#esta es una ruta adicional en la aplicación para la función multiplicación
@app.route("/multiplicacion")
def ruta_multiplicacion():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado = a * b
    return f'''
        <p>La multiplicación de los números {a} y {b} es: {resultado}</p>
        <p><a href="/">Volver a inicio</a></p>
    '''
#esta es una ruta adicional en la aplicación para la función división
@app.route("/division")
def ruta_division():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if b == 0:
        return '''
            <p>Error: No se puede dividir entre cero.</p>
            <p><a href="/">Volver a inicio</a></p>
        '''
    resultado = a / b
    return f'''
        <p>La división de los números {a} y {b} es: {resultado}</p>
        <p><a href="/">Volver a inicio</a></p>
    '''
#esto nos permite actualizar rápidamente los cambios
if __name__=="__main__":
    app.run(debug=True)