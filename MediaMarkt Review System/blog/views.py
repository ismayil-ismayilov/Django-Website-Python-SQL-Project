import sqlite3
from pyexpat import model
from typing import List
from unicodedata import name
from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import connection


from .models import Review, City, Store
from .forms import PersonForm


def home(request):
    return render(request, 'blog/home.html',{'title': 'Homepage'})

#def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def review(request):
    return render(request,'blog/review.html', {'title': 'Review'})


class PersonListView(LoginRequiredMixin, ListView):
    model = Review
    context_object_name = 'people'
    ordering = ['-date']




class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')
    

    def form_valid(self,form):
        form.instance.name = self.request.user
        return super(PersonCreateView,self).form_valid(form)

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class PersonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

    def form_valid(self,form):
        form.instance.name = self.request.user
        return super(PersonUpdateView,self).form_valid(form)

    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.name:
            return True
        return False


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'blog/city_dropdown_list_options.html', {'cities': cities})


def load_stores(request):
    city_id = request.GET.get('city')
    stores = Store.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'blog/storedropdown.html', {'stores': stores})



def average(request):
        connection = sqlite3.connect('Mediamarkt.db')
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """select name, avg(rating_id) from blog_review 
                                join city 
                                on blog_review.city_id = city.id
                                group by name, blog_review.city_id """

        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        connection.commit()
        connection.close

        ##Store
        connection = sqlite3.connect('Mediamarkt.db')
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_q = """SELECT name, avg(rating_id) from blog_review 
                        join store 
                        on blog_review.store_id = store.id
                        group by name, blog_review.store_id"""

        cursor.execute(sqlite_q)
        records2 = cursor.fetchall()
        connection.commit()
        connection.close

        ##Department
        connection = sqlite3.connect('Mediamarkt.db')
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_q = """select name, avg(rating_id) from blog_review 
                        join departments
                        on blog_review.department_id = departments.id
                        group by name, blog_review.department_id"""

        cursor.execute(sqlite_q)
        records3 = cursor.fetchall()
        connection.commit()
        connection.close


        return render(request,'blog/average_list.html',{'data2': records2, 'data': records, 'data3': records3}) 
