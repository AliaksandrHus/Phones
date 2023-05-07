from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import LoginForm, RegistrationForm
from .models import Person
from .random_user import get_random
import re


def index(request):

    if request.method == 'POST':

        for x in range(10):
            tmp = get_random()
            person = Person(name=tmp[0], phone=tmp[1])
            person.save()

        numbers = Person.objects.all()
        all_p = numbers.count()
        data = {'title': 'Главная:', 'all_p': all_p}
        return render(request, 'main/index.html', data)


    else:

        numbers = Person.objects.all()
        all_p = numbers.count()
        data = {'title': 'Главная:', 'all_p': all_p}
        return render(request, 'main/index.html', data)


def error(request):
    data = {'title': 'Ошибка'}
    return render(request, 'main/error.html', data)


def registration_page(request):

    error = 'Введите данные:'

    step1 = r"(?:[a-z0-9!#$%&'*+=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+=?^_`{|}~-]+)*)@(?:[a-z0-9]+(?:-[a-z0-9]+)*)\.[a-z]{2,5}"
    step2 = r"@.{1,63}\."

    def check_email(arg): return True if re.fullmatch(step1, arg) and re.search(step2, arg) else False

    if request.method == 'POST':

        registration_form = RegistrationForm(request.POST)

        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if registration_form.is_valid() and password == password_confirmation and check_email(email):

            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            user = User.objects.create_user(username, email, password)
            user.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('user_home')

        else:
            registration_form = RegistrationForm
            error = 'Данные не корректны, повторите ввод!'
            data = {'title': 'Личный кабинет', 'registration_form': registration_form, 'error': error}

            return render(request, 'main/registration_page.html', data)

    else:
        registration_form = RegistrationForm
        data = {'title': 'Личный кабинет', 'registration_form': registration_form, 'error': error}

        return render(request, 'main/registration_page.html', data)


def login_page(request):

    error = 'Введите данные:'

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_home')

        else:
            error = 'Данные не корректны, повторите ввод!'

            login_form = LoginForm
            data = {'title': 'Личный кабинет', 'login_form': login_form, 'error': error}

            return render(request, 'main/login_page.html', data)

    else:
        login_form = LoginForm
        data = {'title': 'Вход в кабинет', 'login_form': login_form, 'error': error}
        return render(request, 'main/login_page.html', data)


def logout_page(request):

    logout(request)
    return redirect('user_home')



@login_required(login_url='login_page')
def user_home(request):

    data = {'title': 'Кабинет пользователя'}
    return render(request, 'main/user_home.html', data)


@login_required(login_url='error')
def phones_all(request):

    numbers = Person.objects.all()
    data = {'title': 'Все номера:', 'numbers': numbers}
    return render(request, 'main/phones_all.html', data)


def phones_7(request):

    numbers = Person.objects.filter(phone__endswith='7')
    data = {'title': 'Номера ...7', 'numbers': numbers}
    return render(request, 'main/phones_all.html', data)


def phones_985(request):

    numbers = Person.objects.filter(phone__endswith='985')
    data = {'title': 'Номера ...985', 'numbers': numbers}
    return render(request, 'main/phones_all.html', data)


def search(request):

    if request.method == 'POST':

        num = request.POST.get('num')

        if num:
            print(num)

            numbers = Person.objects.filter(phone__contains=num)
            data = {'title': f'Номера с {num}', 'numbers': numbers}
            return render(request, 'main/search.html', data)

        else:
            data = {'title': 'Поиск номера'}
            return render(request, 'main/search.html', data)

    else:

        data = {'title': 'Поиск номера'}
        return render(request, 'main/search.html', data)