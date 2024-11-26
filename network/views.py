from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User, Post


def index(request):
    posts = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {
        "page_obj": page_obj
    })


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            post = Post(user=request.user, content=content)
            post.save()
        return redirect("index")
    return redirect("index")


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user).order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    is_following = profile_user.followers.filter(id=request.user.id).exists() if request.user.is_authenticated else False

    return render(request, "network/profile.html", {
        "profile_user": profile_user,
        "page_obj": page_obj,
        "is_following": is_following,
    })


@login_required
def toggle_follow(request, username):
    profile_user = get_object_or_404(User, username=username)

    if request.user != profile_user:
        if profile_user.followers.filter(id=request.user.id).exists():
            profile_user.followers.remove(request.user)
        else:
            profile_user.followers.add(request.user)

    return HttpResponseRedirect(reverse("profile", args=[username]))


@login_required
def following(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(user__in=following_users).order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "network/following.html", {
        "page_obj": page_obj
    })


@csrf_exempt
@login_required
def edit_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if post.user != request.user:
        return JsonResponse({"error": "You are not allowed to edit this post."}, status=403)

    if request.method == "PUT":
        data = json.loads(request.body)
        content = data.get("content", "")
        if content:
            post.content = content
            post.save()
            return JsonResponse({"message": "Post updated successfully."}, status=200)

    return JsonResponse({"error": "Invalid request."}, status=400)


@login_required
def like_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "POST":
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return JsonResponse({
            "liked": liked,
            "like_count": post.likes.count()
        }, status=200)

    return JsonResponse({"error": "Invalid request."}, status=400)