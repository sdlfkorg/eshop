from django.shortcuts import render
from .models import Sausage, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
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
	paginate_by = 25

	def categories(self):
		return Category.objects.all()
	def get_queryset(self):
		query_set = super(SausageListView, self).get_queryset()

		category = self.kwargs.get('category')

		if category:
			query_set = query_set.filter(category__name=category)

		return query_set	



class SausageDetailView(DetailView):
	model = Sausage
	




#sausages_list_view = SausageListView.as_view()



