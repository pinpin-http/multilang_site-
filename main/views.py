from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Article
from .forms import UserRegisterForm, UserLoginForm, ArticleForm
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import gettext as _ , activate
from django.conf import settings
import logging
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import translation
from django.shortcuts import redirect

def set_language(request):
    if request.method == 'POST':
        lang_code = request.POST.get('language')
        if lang_code and translation.check_for_language(lang_code):
            response = HttpResponseRedirect(request.POST.get('next', '/'))
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
            request.session[settings.LANGUAGE_COOKIE_NAME] = lang_code  
            return response
    return redirect('/')

def logout_view(request):
    logout(request)
    messages.success(request, _("You have been logged out."))
    return redirect('article_list')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

@csrf_protect
def auth_view(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            # Handle login form
            login_form = UserLoginForm(request, data=request.POST)
            register_form = UserRegisterForm()
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('article_list')
            else:
                messages.error(request, _('Login failed. Please check your username and password.'))
        else:
            # Handle registration form
            login_form = UserLoginForm()
            register_form = UserRegisterForm(request.POST, request.FILES)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('article_list')
            else:
                messages.error(request, _('Registration failed. Please check the form and try again.'))
    else:
        login_form = UserLoginForm()
        register_form = UserRegisterForm()

    return render(request, 'auth.html', {'login_form': login_form, 'register_form': register_form})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.author
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})
