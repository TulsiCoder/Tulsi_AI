from django.shortcuts import render
from django.http import HttpResponse

from chat.agent import get_response
# Create your views here.
def home(request):
    response = None
    user_message = None

    if request.method =="POST":
        user_message = request.POST.get("message")

        if user_message:
            response = get_response(user_message)

    return render(request, "home.html", {"response": response, "user_message": user_message})
