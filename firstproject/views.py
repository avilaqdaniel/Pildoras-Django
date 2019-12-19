from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    #nombre= "Ariel"
    #apellido= "Avila Jesús"
    ahora=datetime.datetime.now()
    p1=Persona("Ariel","Avila Jesús")
    temas=["Plantillas", "Modelos", "Formularios", "Vistas","Despliegue"]
    
    #doc_ext = open("D:/Daniel/OnlineCourses/Python/Django/firstproject/firstproject/templates/mytemplate.html")
        #create template variable
    #tmpl = Template(doc_ext.read())
    #doc_ext.close()
    doc_ext = loader.get_template('mytemplate.html')

    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"fecha_ahora":ahora, "temas":temas})
    doc = doc_ext.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"fecha_ahora":ahora, "temas":temas})
    return HttpResponse(doc)

def despedido(request):
    return HttpResponse('Segunda vista')

def traeDate(request):
    fecha_actual=datetime.datetime.now()
    documento = """
    <html>
        <body>
            <h2>
            Fecha y hora actuales %s
            </h2>
        </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculateEdad(request, edad, anno):
    #actualYear = 18
    period = anno - 2019
    futureYear = edad + period
    documento = """
    <html>
        <body>
            <h2>
            En el año %s tendrás %s
            </h2>
        </body>
    </html>""" %(anno, futureYear)
    return HttpResponse(documento)
