from django.shortcuts import render
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.utils import ErrorList
from .models import Sausage, Category
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.

def sausage_list(request, category=None):

    sausage_list = Sausage.objects.all()
    # sausage_list_queryset = Sausage.objects.all()
    
    # if category: 
    #     sausage_list_queryset = sausage_list_queryset.filter(category__name=category)
    
    paginator = Paginator(sausage_list, 10)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
   
    content = {
    "sausage_list": page_obj,
    "categories": Category.objects.all(),
    "page_obj": page_obj,
    }
    
    return render(request, "home.html", content)

class SausageListView(ListView):
    model = Sausage
    paginate_by = 4
    template_name = 'sausage/index.html'

    def categories(self):
        return Category.objects.all()
    def get_queryset(self):
        query_set = super(SausageListView, self).get_queryset()

        category = self.kwargs.get('category')

        if category:
            query_set = query_set.filter(category__name=category)

        return query_set    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        query_set = super(SausageListView, self).get_context_data()
        # Add extra content in QuerySet 
        query_set['page_title'] = "香氣四溢 沁人肝腸"
        query_set['page_intro'] = "亞洲最大的香腸販售平台終於上線啦！"
        # query_set['footer_str'] = "Tzu-Chieh Liao. All rights reserved, 2017."

        return query_set



class SausageDetailView(DetailView):
    model = Sausage


class SausageCreateView(LoginRequiredMixin, CreateView):
    model = Sausage 
    login_url = reverse_lazy('login')

    success_url = reverse_lazy('sausage_list')
    fields = [
        'name', 'description', 'image', 
        'original_price', 'current_price', 
        'tag', 'category', 'place_of_origin']

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(SausageCreateView, self).form_valid(form)
        else:
            # return self.form_invalid(form)
            form._errors[forms.forms.NON_FIELD_ERRORS] = \
                ErrorList(['User must be logged in to continue.'])            
            return self.form_invalid(form)


class SausageUpdateView(LoginRequiredMixin, UpdateView):
    model = Sausage
    template_name_suffix = '_update_form'
    fields = [
        'name', 'description', 'image', 
        'original_price', 'current_price', 
        'tag', 'category', 'place_of_origin']
    success_url = reverse_lazy('sausage_list')

    def get_object(self, *args, **kwargs):
        current_user = self.request.user
        instance = super(SausageUpdateView, self)\
            .get_object(*args, **kwargs)
        user_id = instance.user_id
        user = User.objects.get(id=user_id)
        if current_user.is_superuser or \
            current_user.is_staff or current_user == user:
            return instance
        raise PermissionDenied


    # def form_valid(self, form):
    #     print(form.instance.user)
    #     print(self.request.user)
    #     if self.request.user.is_authenticated and \
    #         self.request.user == form.instance.user:
    #         return super(SausageUpdateView, self).form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    

def about(request):
    title = '緣起：'
    description = '''
    我們是一群對著台灣肉品有著堅持的7年級生。

    就讀農業科系的我們，大學時代在肉舖打工，跟著師父香腸伯學習製作各種肉品。

    香腸伯曾告訴我們：把香腸當事業要有心理準備，前3年的壓力會喘不過氣。

    在結束研替後一年，我們還是堅持要做香腸。

    透過在大學時所學『生農為體，機電為用』，

    我們對優質肉品的堅持，不只是口號，而是透過引入在台灣最高學店所學的技能、以及用心研發證明。

    雖然很多人說我們傻，但為了讓台灣人享用最優質的香腸，我們仍然在這裡堅持著。

   '''
    content = {
        'title': title,
        'description': description}

    return render(request, 'about.html', content)




#sausages_list_view = SausageListView.as_view()



