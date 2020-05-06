from django.shortcuts import render
from .models import Post
import requests

def home(request):
    ext_api = 'https://jsonplaceholder.typicode.com/posts'
    data = request.POST
    # payload = API_KEY
    res = requests.post(ext_api, data) # You can add more parameter e.g api key as a payload dictionary
    # user = Post(res)
    res_dict = res.json()
    print("==========================================")
    print('Submitted to API successfully')
    
    if request.method == 'POST':
        # user_id = request.POST['post_id']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        post = Post(username=username, first_name=first_name, last_name=last_name)

        post.save()
        print('==============================================')
        print(post)

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'api_app/home.html', context)
