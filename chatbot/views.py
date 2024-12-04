from http.client import responses

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Chat

#@login_required()
from django.http import JsonResponse

def chatbot(request):
    if request.method == "POST":
        user_message = request.POST.get('message', '').strip().lower()

        # Liste des services
        services = [
            "Demander une facture des charges",
            "Obtenir le bilan des dépenses",
            "Obtenir la liste des firmes financées"
        ]

        if user_message == "bonjour":
            # Création de la réponse avec services numérotés
            response = (
                "Bonjour, comment puis-je vous aider aujourd'hui ?\n"
                "Voici les services que je peux vous proposer :\n"
                "1. " + services[0] + "\n"
                "2. " + services[1] + "\n"
                "3. " + services[2] + "\n\n"
                "Veuillez entrer le numéro du service que vous souhaitez :"
            )
        else:
            response = "Je ne comprends pas, pouvez-vous reformuler ?"

        # Retourner la réponse avec la liste des services
        return JsonResponse({"response": response})

    # Si la requête est un GET, on rend la page de chat
    return render(request, 'chatbot/chat.html')

    return render(request, 'chatbot/chat.html')
def chat_view(request):
    chats = Chat.objects.filter(user=request.user)
    return render(request, 'chatbot/chat.html', {'chats': chats})
def handle_message(request):
    user_message = request.GET.get('message', '').lower()
    services = [
        "Demander une facture des charges",
        "Obtenir le bilan des dépenses",
        "Obtenir la liste des firmes financées"
    ]
    if 'bonjour' in user_message:
        response = "\n".join(services)
    else:
        response = "Je ne comprends pas votre message."

    return JsonResponse({'response': response})


#def login(request):
 #   if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
 #       user = auth.authenticate(request, username=username, password=password)
#        if user is not None:
#            auth.login(request, user)
#            return redirect('chatbot')
 #       else:
 #           error_message = 'Invalid username or password'
 #           return render(request, 'login.html', {'error_message': error_message})
#    else:
 #       return render(request, 'login.html')

#def register(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        email = request.POST['email']
#        password1 = request.POST['password1']
 #       password2 = request.POST['password2']

#        if password1 == password2:
#            try:
#               user = User.objects.create_user(username, email, password1)
#                user.save()
#                auth.login(request, user)
#                return redirect('chatbot')
#            except:
#                error_message = 'Error creating account'
#                return render(request, 'register.html', {'error_message': error_message})
#        else:
#            error_message = 'Password dont match'
#            return render(request, 'register.html', {'error_message': error_message})
 #   return render(request, 'register.html')

#def logout(request):
#    auth.logout(request)
#    return redirect('login')
