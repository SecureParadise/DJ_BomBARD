from django.shortcuts import render
from .forms import TweetForm
from .models import TweetModel
from django.shortcuts import get_object_or_404,redirect
from .forms import UserRegistrationForm
# import decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request,'index.html')

# Views For handling Form
@login_required
def tweetlist(request):
    tweets = TweetModel.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweete':tweets})
@login_required
def tweet_create(request):
    # handle whatever data is comming
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save() 
            return redirect('tweetlist')

    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})


# Edit tweet
@login_required
def edit_tweet(request,tweet_id):
    tweet = get_object_or_404(TweetModel,primary_key=tweet_id,user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    
    return render(request,'tweet_form.html',{'form':form})

# Tweet Delete
@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(TweetModel,primary_key=tweet_id,user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweetlist')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


# Register USer
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweetlist')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
