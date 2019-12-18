from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse('Primera vista con Django')

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
