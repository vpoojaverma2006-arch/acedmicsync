

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User  # Ya aapka custom model ho toh wo import karein

def register(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_active = request.POST.get('is_active') == 'true'

        # Example: Direct creation logic (Model ke hisab se modify kar sakte hain)
        # user = User.objects.create_user(
        #     username=user_id,
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     password=password,
        #     is_active=is_active
        # )
        
        # Save hone ke baad redirect ya response:
        messages.success(request, 'Registration Successful!')
        return redirect('register')

    return render(request, 'register.html')
