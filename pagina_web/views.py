from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def enviar_correo(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('email')
        mensaje = request.POST.get('message')

        # Contenido del correo
        subject = 'Nuevo mensaje de AUTOPET UTT 🐾'
        message = f"""
        Nombre: {nombre}
        Correo: {correo}
        Mensaje: {mensaje}
        """
        
        # Destinatario del mensaje (cambia esto con el correo de tu equipo)
        destinatario = ['futech2026@gmail.com']

        try:
            # Enviar correo
            send_mail(subject, message, settings.EMAIL_HOST_USER, destinatario)
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente! Nos pondremos en contacto contigo pronto. 🎉')
            return redirect('home')  # Redirige a la página principal o donde prefieras
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            messages.error(request, 'Hubo un error al enviar tu mensaje. 😢')
            return redirect('home')

def home(request):
    return render(request, 'home.html')