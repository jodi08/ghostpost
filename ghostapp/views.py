from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from ghostapp.models import BoastRoast
from ghostapp.forms import NewPost


# Create your views here.
def index_view(request):
    post_data = BoastRoast.objects.all().order_by('-timestamp')
    return render(request, "index.html", {"post_data": post_data})

def create_post_view(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastRoast.objects.create(
                boast_roast = data.get('boast'),
                body = data.get('create_post'),
                )
        return HttpResponseRedirect(reverse('homepage'))

    form = NewPost()
    return render(request, 'createpost.html', {"form": form})


def roast_view(request):
    postsort = BoastRoast.objects.filter(boast_roast=False).order_by('-timestamp')
    return render(request, "roast.html", {'postsort': postsort})
    

def boast_view(request):
    postsort = BoastRoast.objects.filter(boast_roast=True).order_by('-timestamp')
    return render(request, "boast.html", {'postsort': postsort})

def sort_votes_view(request):
    brsort = BoastRoast.objects.all()
    sorted_post = sorted(brsort, key=lambda x:(-x.totalvotes))
    return render(request, 'sortbyvotes.html', {'brsort':sorted_post})

def upvote_view(request, post_id):
    post = BoastRoast.objects.get(id=post_id)
    post.upvote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def downvote_view(request, post_id):
    post = BoastRoast.objects.get(id=post_id)
    post.downvote -= 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))
