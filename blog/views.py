from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from myproject.decorators import otp_rec_required
import ldap

# Create your views here.


# @login_required(login_url='account/login')
# @otp_rec_required
def home(request):
    # con = ldap.initialize('ldap://localhost')
    # ldap_base = 'dc=example,dc=com'
    # con.simple_bind_s('cn=admin,dc=example,dc=com','ElMiguel11@@')
    # print('In home')
    # query = "(objectClass=*)"
    # result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
    # print(result)
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # can pass in value without context if small enough
    return render(request, 'blog/about.html', {'title' : 'About'})
