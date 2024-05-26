from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib import messages as mg
from .form import ClientForm, ItemForm
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contacts(request):
    return render(request, 'contact.html')


def tracking_details(request):
    if request.method == 'POST':
        track_id = request.POST.get('track')
        # print(track_id)

        receiver = Delivery.objects.get(tracking_id=track_id)
        details = receiver.item_set.all()
        total = 0

        for x in details:
            total += float(x.shipping_cost)
        context = {'receiver': receiver, 'details': details, 'total': total}

        return render(request, 'dashboard/invoice.html', context)
    return render(request, 'dashboard/invoice.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            mg.error(request, 'Invalid Username or Password')
    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard(request):
    clients = Delivery.objects.all()
    return render(request, 'dashboard/index.html', {'clients': clients})


@login_required(login_url='login')
def edit(request, pk):
    client = Delivery.objects.get(id=pk)
    items = client.item_set.all()
    form = ClientForm(instance=client)
    edit = True

    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)

        if form.is_valid:
            form.save()
            return redirect('dashboard')
    return render(request, 'dashboard/add-edit-client.html', {'form': form, 'client': client, 'items': items, 'edit': edit})


@login_required(login_url='login')
def addClient(request):
    form = ClientForm()

    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('dashboard')

    return render(request, 'dashboard/add-edit-client.html', {'form': form, })


@login_required(login_url='login')
def addItem(request, pk):
    client = Delivery.objects.get(id=pk)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid:
            save = form.save(commit=False)
            save.receiver = client
            save.save()

            return redirect('edit', pk=client.id)
    return render(request, 'dashboard/add-edit-item.html', {'client': client, 'form': form})


@login_required(login_url='login')
def editItem(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)

    edit = True

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)

        if form.is_valid:
            save = form.save()

            return redirect('edit', pk=item.receiver.id)
    return render(request, 'dashboard/add-edit-item.html', {'form': form})


def delete(request, pk):
    obj = Delivery.objects.get(id=pk)
    obj.delete()
    return redirect('dashboard')


def deleteItem(request, pk):
    obj = Item.objects.get(id=pk)
    obj.delete()
    return redirect('edit', pk=obj.receiver.id)



def sendEmail(request, pk):
    client = Delivery.objects.get(id=pk)
    with get_connection(
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_ssl=settings.EMAIL_USE_SSL
    ) as connection:

        subject = "WAYBILL INFORMATION"
        message = f"""
            Welcome to 
        TRUSTED LOGISTICS EXPRESS
    Email: info@normaltrusted.agency 


        Delivery Details:


Name: {client.receivers_name}
Address: {client.receivers_address}
Phone Number: {client.receivers_phone}
Destination Country: {client.destination_country}
Tracking ID: {client.tracking_id}




        Thanks for using our Service


"""
        email_from = "info@normaltrusted.agency"
        receiver = [client.receivers_email]
        EmailMessage(subject, message, email_from,
                     receiver, connection=connection).send()

    return redirect('dashboard')
