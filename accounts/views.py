from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


# ---------------------------------
# REGISTER VIEW
# ---------------------------------
def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Validate empty fields
        if not email or not username or not password:
            return render(request, "register.html", {
                "error": "All fields are required."
            })

        # Check duplicate email
        if CustomUser.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "Email already registered."
            })

        # Check duplicate username
        if CustomUser.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already taken."
            })

        # Create user
        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password
        )

        # Login immediately after register
        login(request, user)

        # Mark user online
        user.is_online = True
        user.save()

        return redirect("user_list")

    return render(request, "register.html")


# ---------------------------------
# LOGIN VIEW  (Email Authentication)
# ---------------------------------
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # IMPORTANT:
        # Django expects "username" parameter internally
        # We pass email as username because we created EmailBackend
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            # Mark user online
            user.is_online = True
            user.save()

            return redirect("user_list")

        return render(request, "login.html", {
            "error": "Invalid email or password."
        })

    return render(request, "login.html")


# ---------------------------------
# LOGOUT VIEW
# ---------------------------------
def logout_view(request):
    if request.user.is_authenticated:
        request.user.is_online = False
        request.user.save()

    logout(request)
    return redirect("login")
