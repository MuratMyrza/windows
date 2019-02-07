from django.shortcuts import render
from django.db.models import Q
from testuser.models import TestUser

def users(request):
    #testusers = TestUser.objects.filter(
      # username__icontains='AvaTarka',
     #  username__icontains='Maria',
    #   is_active=True
   # ).exclude('id')


    testusers =TestUser.objects.filter(
       Q(username__icontains='maria') | Q(username__icontains='AvaTarka'),
        is_active=True
    ).order_by('id')

    return render(request, 'maria/home.html', {
        'users': testusers
    })
