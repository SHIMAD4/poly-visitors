from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from users.forms import UserCreationForm


# Create your views here.
def profile(request):
    return render(request, "users/profile.html")


class Register(View):
    template_name = "users/register.html"

    def get(self, request):
        context = {"form": UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("../")
        context = {"form": form}
        return render(request, self.template_name, context)
