from django.shortcuts import render, HttpResponse, redirect
from .models import Book

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    # return HttpResponse("<html> <h1> Welcome Here !!</h1> </html>")
    if request.method == "POST":
        print(request.POST)
        bid = request.POST.get("book_id")
        name = request.POST.get("book_name")
        price = request.POST.get("book_price")
        qty  = request.POST.get("book_quantity")
        author = request.POST.get("book_author")
        is_pub = request.POST.get("book_is_pub")
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False
        if not bid:
            Book.objects.create(name = name, qty = qty, price = price, author = author, is_published = is_pub)
        else:
            book_obj = Book.objects.get(id = bid)
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.author = author
            book_obj.is_published = is_pub
            book_obj.save()
        return redirect("home_page")
    
    elif request.method == "GET":
        return render(request, "home.html")
    


    #View to show all books
@login_required
def show_all_books(request):
    return render(request, 'show_books.html', {"all_books" :Book.objects.all()})


#view for update book
@login_required
def update_book(request, pk):
    return render(request, "home.html", context = {"single_book" : Book.objects.get(id = pk)})


@login_required
def delete_book(request, pk):
    Book.objects.get(id = pk).delete()
    return redirect("all_books")



#class based views

from django.views import View
class NewView(View):
    def get(self,request):
        return HttpResponse("In get method of CBV")
    

from django.views.generic.edit import CreateView

class BookCreate(CreateView):
    model = Book
    fields = "__all__"
    success_url = "/cbv-create-book/"

from django.views.generic.list import ListView

class BookRetrieve(ListView):
    model = Book
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = Book.objects.filter(is_published = 1)


from django.views.generic.detail import DetailView

class BookDetail(DetailView):
    model = Book


from django.views.generic.edit import UpdateView
class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"
    success_url = "/cbv-book-list/"


from django.views.generic.edit import DeleteView
class BookDelete(DeleteView):
    model = Book
    success_url = "/cbv-book-list/"


#CSV file 
from django.http import HttpResponse
import csv

def create_csv(request):
    response = HttpResponse(content_type = "text/csv")
    response['Content-Disposition'] = 'attachment; filename = "book_data.csv"'
    
    writer =  csv.writer(response)
    writer.writerow(["id", 'name', "qty", 'price', 'author', 'is_published'])

    books = Book.objects.all().values_list('id', 'name', 'qty', 'price', 'author', 'is_published')
    for book in books:
        writer.writerow(book)
    return response


def upload_csv(request):
    file = request.FILES["csv_file"]
    # print(file)
    decoaded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoaded_file)
    # print(reader)
    lst  =[]

    for elem in reader:
        is_pub =elem.get('is_published')
        if is_pub == "TRUE":
            is_pub = True
        else:
            is_pub = False
        lst.append(Book(name =elem.get('name'), qty = elem.get('qty'), price = elem.get('price'), author = elem.get('author'), is_published = is_pub))

    Book.objects.bulk_create(lst)
    return HttpResponse("Success")