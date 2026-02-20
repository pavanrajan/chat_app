from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import Message


@login_required
def user_list(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, "user_list.html", {"users": users})


@login_required
def chat_view(request, user_id):
    other_user = get_object_or_404(CustomUser, id=user_id)

    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("timestamp")

    # mark messages as read
    messages.filter(receiver=request.user).update(is_read=True)

    return render(request, "chat.html", {
        "other_user": other_user,
        "messages": messages
    })
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import Message


@login_required
def user_list(request):
    # Get all users except current user
    users = CustomUser.objects.exclude(id=request.user.id)

    user_data = []

    for user in users:
        # Count unread messages from this user
        unread_count = Message.objects.filter(
            sender=user,
            receiver=request.user,
            is_read=False
        ).count()

        user_data.append({
            "user": user,
            "unread": unread_count
        })

    return render(request, "user_list.html", {
        "user_data": user_data
    })
