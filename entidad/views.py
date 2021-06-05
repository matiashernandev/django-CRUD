from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona, Localidad
from .forms import PersonaForm

#import sqlite3

def index(request, template_name="entidad/index.html"):
    return render(request, template_name)


def acerca_de(request):
    return HttpResponse("Curso de Python y Django")

def cliente(request, template_name="entidad/cliente.html"):
    clientes = Persona.objects.all()
    datos = {"clientes": clientes}
    return render(request, template_name, datos)

def localidad(request, template_name="entidad/localidad.html"):
    localidades = Localidad.objects.all()
    datos = {"localidades": localidades}
    return render(request, template_name, datos)

def nuevo_cliente(request, template_name="entidad/nuevo_cliente.html"):
    if request.method == "POST":
        form_cliente = PersonaForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save(commit=True)
            return redirect("cliente")    

    else:
        form_cliente = PersonaForm()
    datos = {"form": form_cliente}
    return render(request, template_name, datos)


def editar_cliente(request, pk, template_name="entidad/nuevo_cliente.html"):
    cliente = get_object_or_404(Persona, pk=pk)
    form = PersonaForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect("cliente")
        else:
            print(form.errors)
            return render(request, template_name, {"form": form })
    else:
        return render(request, template_name, {"form": form})


def borrar_cliente(request, pk, template_name="entidad/cliente_confirm_delete.html"):
    cliente = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return HttpResponse("El cliente fundió")
    else:
        return render(request, template_name)



# def cursos ( request ):
#     conn = sqlite3.connect( "cursos.db" )
#     cursor = conn.cursor()
#     cursor.execute( "SELECT nombre, inscriptos FROM cursos" )
#     html = """
#             <html>
#             <title>Lista de cursos</title>
#             <table style="border: 1px solid">
#             <thead>
#             <tr>
#             <th>Curso</th>
#             <th>Inscriptos</th>
#             </tr>
#             </thead>
#             """
#     for (nombre, inscriptos) in cursor.fetchall():
#         html += " <tr><td> " + nombre + " </td><td> " +  str(inscriptos) + " </td></tr>"
#     html += "</table></html>"
#     conn.close()
#     return HttpResponse(html)