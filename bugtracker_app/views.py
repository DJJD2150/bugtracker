from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bugtracker_app.models import CustomUserModel, Ticket
from bugtracker_app.forms import AddLoginForm, TicketForm, UserForm

# Create your views here.
def index_view(request):
    tickets = Ticket.objects.all()
    return render(request, "homepage.html", {'tickets': tickets})

def login_view(request):
    if request.method == "POST":
        form = AddLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = authenticate(
                request,
                username=data.get("username"),
                password=data.get("password")
            )
            if username:
                login(request, username)
            return HttpResponseRedirect(
                request.GET.get('next', reverse("homepage"))
            )

    form = AddLoginForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

@login_required
def create_ticket_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Ticket.objects.create(
                title=data.get('title'),
                user_filed_ticket=request.user,
                description=data.get('description'),
                user_assigned_ticket=None,
                user_completed_ticket=None
            )
        if new_ticket:
            return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()
    return render(request, "generic_form.html", {"form": form})

@login_required
def ticket_view(request):
    pass

@login_required
def ticket_edit_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticket_view", args=[ticket.id]))

    data = {
        "title": ticket.title,
        "description": ticket.description,
    }
    form = TicketForm(initial=data)
    return render(request, "generic_form.html", {"form": form})

@login_required
def create_user_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Ticket.objects.create(
                title=data.get('title'),
                user_filed_ticket=request.user,
                description=data.get('description'),
                user_assigned_ticket=None,
                user_completed_ticket=None
            )
    if new_ticket:
        return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()
    return render(request, "generic_form.html", {"form": form})

@login_required
def user_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = UserForm()
    return render(request, "generic_form.html", {"form": form})

"""localhost:8000/username/3/edit"""
@login_required
def user_edit_view(request, user_id):
    username = CustomUserModel.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=username)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = UserForm(instance=username)
    return render(request, "generic_form.html", {"form": form})
