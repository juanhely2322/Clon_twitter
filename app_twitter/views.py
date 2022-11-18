from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
# Create your views here.
def home(request):
    post=models.post.objects.all()
    if request.method == "GET":
            return render(request, "twitter/newsfeed.html", {
            "form": forms.creationPost, "post":post,
        })
    else:
        try:
            form = forms.creationPost(request.POST)
            new_post= form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect("home")
        
        except ValueError:
                 return render(request, "twitter/newsfeed.html", {
                "error":"please provide valide data","post":post,"form":forms.creationPost,
 
                     })
                 
def delete_post(request,post_id):
    post=get_object_or_404(models.post, pk=post_id, user=request.user)
    post.delete()
    return redirect("home")