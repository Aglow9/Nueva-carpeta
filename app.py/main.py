from flask import Flask, send_from_directory
import random

app = Flask(__name__)



facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos0",
             "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
             "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
             "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
             "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
             "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
             "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
             "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]
@app.route("/")
def index():
    return f'<h1>Datos Interesantes</h1><p>prueba>p<<p>{random.choice(facts_list)}</p><a href="/random_fact">¡Ver un dato aleatorio!</a>'

@app.route("/random_fact")
def datos():
    return f'<h1>Datos Interesantes</h1><p>{random.choice(facts_list)}</p> <a href="/cat">¡gatitos!!!!!</a>'

@app.route("/cat") #generador de gatitos
def gatos():
    cat = random.randint(1,10) #seleccionamos una foto
    if cat == 1:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato siames!!!!</h1>
                        <img src="https://th.bing.com/th/id/OIP.TjCAcDUIv_awRheRlfulMAAAAA?rs=1&pid=ImgDetMain" alt="Imagen de gato siames">
                </body>
            </html>
        '''
    elif cat == 2:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>Maine coon!!!!!</h1>
                        <img src="https://th.bing.com/th/id/OIP.p4qIAmsMC1TBIo5S-sEAHwHaHd?rs=1&pid=ImgDetMain" alt="imagen de maine coon">
                </body>
            </html>
        '''

    elif cat == 3:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato azul ruso!!!!!</h1>
                        <img src="https://th.bing.com/th/id/OIP.Gu1l8BA94P-thHqqqey67AHaEt?rs=1&pid=ImgDetMain" alt="imagen de gato azul ruso">
                </body>
            </html>
        '''
    elif cat == 4:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato britanico de pelo corto!!!!!</h1>
                        <img src="https://th.bing.com/th/id/R.af25b43a840f9535a91f31d7c51e6841?rik=BAxIM6AnouosYg&pid=ImgRaw&r=0" alt="imagen de gato britanico de pelo corto">
                </body>
            </html>
        '''

    elif cat == 5:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato ragamuffin!!!!!</h1>
                        <img src="https://petstutorial.com/wp-content/uploads/2021/05/ragamuffin-cat-breed-Appearance.jpg" alt="imagen de gato ragamuffin">
                </body>
            </html>
        '''
    
    elif cat == 6:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato khao manee GIGANTEEE!!!!!</h1>
                        <img src="https://www.thesprucepets.com/thmb/4Ccj_2np2nBy5UvZcm0IlHVLk4o=/2121x0/filters:no_upscale():strip_icc()/GettyImages-1067857094-dd4cc0c7b2ef48b1a7afe44e85b1082b.jpg" alt="imagen de gato khao manee">
                </body>
            </html>
        '''
    elif cat == 7:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato himalayo!!!!!</h1>
                        <img src="https://th.bing.com/th/id/R.dee59a7b01d0ecc1bb80907b3f6d6041?rik=5Yej%2b0BBXcoVZQ&pid=ImgRaw&r=0" alt="imagen de gato himalayo">
                </body>
            </html>
        '''
    elif cat == 8:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato chantilly-tiffany!!!!!</h1>
                        <img src="https://th.bing.com/th/id/OIP.0AQabOjfZLh3lZGj-Fcu4wHaE8?rs=1&pid=ImgDetMain" alt="imagen de gato chantilly-tiffany">
                </body>
            </html>
        '''
    elif cat == 9:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato munchkin!!!!!</h1>
                        <img src="https://i0.wp.com/vetplace.pe/wp-content/uploads/2021/12/Gato-Munchkin-cuidados.jpg" alt="imagen de gato munchkin">
                </body>
            </html>
        '''
    elif cat == 10:
        return '''
            <html>
                <body>
                    <h1>generador de gatitos</h1>
                    <h1>gato selkirk rex!!!!!</h1>
                        <img src="https://th.bing.com/th/id/R.e03b60ce6a27dc4dfb442744aaeee0f6?rik=Mwry1bYC%2fZ8vdw&pid=ImgRaw&r=0" alt="imagen de gato selkirk rex">
                </body>
            </html>
        '''


app.run(debug=True)
