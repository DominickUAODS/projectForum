from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, JsonResponse
from django.conf import settings
from django.core.exceptions import ValidationError
from .models import *
from .forms import *

def base(request):
    return render(request, "base.html")

#add custom user to create a category
# custom_user = CustomUser.objects.create(
#     username="pavelkosov",
#     password=make_password("securepassword123"),  
#     first_name="Pavel",
#     last_name="Kosov",
#     date_of_bitrh="1990-05-12", 
#     user_image="user_image/pavel-kosov.jpg"  
# )

# print(f"CustomUser {custom_user.username} created successfully!")


# custom_user = CustomUser.objects.create(
#     username="elenasometh",
#     password=make_password("000"),  
#     first_name="Elena",
#     last_name="Lena",
#     date_of_bitrh="1990-05-12", 
#     user_image="user_image/jake-nackos.jpg "  
# )

# print(f"CustomUser {custom_user.username} created successfully!")

#get categories

def index(request):
    categories = Category.objects.all()  
    return render(request, 'index.html', {'categories': categories})


#add posts to category 1

# category = Category.objects.get(id=1)
# user = CustomUser.objects.get(id=1)
# Post.objects.create(
#     category=category,
#     author=user,
#     content="The impact of AI on the future of technology. It's shaping industries globally.",
#     likes=0
# )

# Post.objects.create(
#     category=category,
#     author=user,
#     content="Exploring the world of quantum computing and its potential for revolutionizing technology.",
#     likes=0
# )

# Post.objects.create(
#     category=category,
#     author=user,
#     content="The rise of smart devices and how they are transforming our daily lives.",
#     likes=0
# )

# Post.objects.create(
#     category=category,
#     author=user,
#     content="How 5G technology will change the way we communicate and work remotely.",
#     likes=0
# )

# Post.objects.create(
#     category=category,
#     author=user,
#     content="Blockchain technology is paving the way for a more secure and transparent internet.",
#     likes=0
# )

#add posts to category 2


# category_programming = Category.objects.get(id=2)
# Post.objects.create(
#     category=category_programming,
#     author=user,
#     content="Python is one of the most versatile programming languages out there. It's used for everything from web development to data science. Its simple syntax and powerful libraries make it a great choice for both beginners and experienced developers. Python is constantly evolving, and it's here to stay.",
#     likes=0
# )

# Post.objects.create(
#     category=category_programming,
#     author=user,
#     content="JavaScript is essential for modern web development. It allows you to create interactive and dynamic websites. With frameworks like React and Angular, JavaScript has become even more powerful, enabling developers to build complex applications. Learning JavaScript opens up countless opportunities in front-end and back-end development.",
#     likes=0
# )

# Post.objects.create(
#     category=category_programming,
#     author=user,
#     content="C++ is a high-performance language that's used in everything from gaming to systems programming. It offers direct memory management, which gives developers more control but also requires a deeper understanding of how memory works. C++ remains one of the most important languages for performance-critical applications.",
#     likes=0
# )

# Post.objects.create(
#     category=category_programming,
#     author=user,
#     content="The world of mobile app development is dominated by two major platforms: iOS and Android. Swift and Kotlin have emerged as the go-to languages for building apps on these platforms. These languages offer modern features, and their integration with their respective ecosystems makes them essential for mobile developers.",
#     likes=0
# )

# Post.objects.create(
#     category=category_programming,
#     author=user,
#     content="Git is a must-know tool for any developer. It allows developers to track changes in code, collaborate with others, and maintain a history of project versions. Platforms like GitHub and GitLab have further expanded Git's usefulness by providing cloud-based repositories, enabling seamless collaboration across teams.",
#     likes=0
# )

#add posts to category 3


# category_gadgets = Category.objects.get(id=3)
# Post.objects.create(
#     category=category_gadgets,
#     author=user,
#     content="The latest smartphones are not just communication tools anymore; they are powerful mini-computers. With features like high-resolution cameras, advanced processors, and AI-powered apps, smartphones have become indispensable in our daily lives. Companies like Apple and Samsung continue to push the boundaries with each new release.",
#     likes=0
# )

# Post.objects.create(
#     category=category_gadgets,
#     author=user,
#     content="Smartwatches have quickly evolved from simple timepieces to full-fledged health and fitness tracking devices. With built-in sensors, GPS, and heart rate monitors, they help users stay on top of their health while staying connected. Brands like Apple and Fitbit offer sleek designs with robust features.",
#     likes=0
# )

# Post.objects.create(
#     category=category_gadgets,
#     author=user,
#     content="Wireless earbuds have become a must-have accessory for many. With their compact design and high-quality sound, they make listening to music, taking calls, and attending virtual meetings on the go more convenient. Popular options include Apple's AirPods and Samsung's Galaxy Buds, both of which offer seamless connectivity with their respective ecosystems.",
#     likes=0
# )

# Post.objects.create(
#     category=category_gadgets,
#     author=user,
#     content="The rise of smart home devices is transforming how we interact with our living spaces. From voice assistants like Amazon's Alexa and Google Assistant to smart thermostats and security cameras, these devices offer convenience and efficiency. As technology improves, the integration of various gadgets makes homes smarter and more energy-efficient.",
#     likes=0
# )

# Post.objects.create(
#     category=category_gadgets,
#     author=user,
#     content="Electric vehicles (EVs) are becoming more popular as an alternative to traditional cars. With advancements in battery technology and charging infrastructure, EVs offer a cleaner, more sustainable mode of transportation. Companies like Tesla are leading the charge, while traditional automakers are following suit with their own electric models.",
#     likes=0
# )

#add posts to category 4


# category_games = Category.objects.get(id=4)
# Post.objects.create(
#     category=category_games,
#     author=user,
#     content="The gaming industry has seen tremendous growth in recent years, with titles like 'Fortnite' and 'Call of Duty' dominating the charts. These games have not only changed the way we play but also the way we connect with others, thanks to their online multiplayer features. Gaming has become a social experience.",
#     likes=0
# )

# Post.objects.create(
#     category=category_games,
#     author=user,
#     content="Virtual reality (VR) gaming is taking the experience to the next level. With VR headsets like Oculus Quest and PlayStation VR, players can immerse themselves in entirely new worlds. As technology advances, VR is expected to become even more realistic and engaging, creating opportunities for new types of gaming experiences.",
#     likes=0
# )

# Post.objects.create(
#     category=category_games,
#     author=user,
#     content="Mobile gaming has become increasingly popular, with games like 'PUBG Mobile' and 'Genshin Impact' attracting millions of players worldwide. The convenience of gaming on smartphones allows players to enjoy high-quality games on the go, breaking down the traditional barriers of console or PC gaming.",
#     likes=0
# )

# Post.objects.create(
#     category=category_games,
#     author=user,
#     content="Indie games have seen a resurgence in recent years, with titles like 'Hades' and 'Hollow Knight' receiving critical acclaim. These games often bring unique art styles and creative gameplay mechanics, giving players something different from the mainstream titles. Indie developers are proving that you don’t need a big budget to create a great game.",
#     likes=0
# )

# Post.objects.create(
#     category=category_games,
#     author=user,
#     content="The rise of eSports has turned competitive gaming into a global phenomenon. Professional players and teams compete in games like 'League of Legends' and 'Dota 2' for massive prizes, drawing millions of viewers. As eSports continues to grow, it’s becoming more accepted as a legitimate form of entertainment.",
#     likes=0
# )

#add posts to category 5

# category_science = Category.objects.get(id=5)
# Post.objects.create(
#     category=category_science,
#     author=user,
#     content="The field of renewable energy is rapidly advancing, with solar and wind power taking center stage in efforts to combat climate change. Scientists are developing new technologies to make these energy sources more efficient and affordable, paving the way for a greener future. The shift to renewables is not just an environmental need, but also an economic opportunity.",
#     likes=0
# )

# Post.objects.create(
#     category=category_science,
#     author=user,
#     content="Artificial Intelligence (AI) is transforming industries worldwide, from healthcare to transportation. Researchers are working on improving AI systems to enhance decision-making, reduce human error, and predict outcomes with greater accuracy. As AI technology continues to evolve, its potential to change society is limitless.",
#     likes=0
# )

# Post.objects.create(
#     category=category_science,
#     author=user,
#     content="The study of genetics has made significant breakthroughs in recent years. Scientists are now able to identify genetic disorders and even work on gene editing techniques such as CRISPR to cure certain diseases. These advances hold the promise of revolutionizing medicine and improving human health.",
#     likes=0
# )

# Post.objects.create(
#     category=category_science,
#     author=user,
#     content="Space exploration has reached new heights with missions to Mars and the Moon. NASA and private companies like SpaceX are developing technologies to make space travel more feasible and sustainable. The ultimate goal is to establish human colonies on other planets, opening up new frontiers for humanity.",
#     likes=0
# )

# Post.objects.create(
#     category=category_science,
#     author=user,
#     content="Quantum computing is an emerging field that could potentially revolutionize computing as we know it. By harnessing the power of quantum mechanics, researchers aim to develop computers that can solve problems far beyond the capabilities of today's classical machines. This could lead to breakthroughs in fields such as cryptography and drug discovery.",
#     likes=0
# )


#add posts to category 6


# category_cybersecurity = Category.objects.get(id=6)
# Post.objects.create(
#     category=category_cybersecurity,
#     author=user,
#     content="With the rise of digital transformation, cybersecurity has become a critical aspect of protecting sensitive data. Hackers are constantly developing new methods to breach systems, making it essential for organizations to stay one step ahead. Implementing strong encryption and regular system audits are key to safeguarding digital assets.",
#     likes=0
# )

# Post.objects.create(
#     category=category_cybersecurity,
#     author=user,
#     content="Phishing attacks remain one of the most common cybersecurity threats today. Attackers often use deceptive emails and websites to trick users into revealing personal information or downloading malicious software. Awareness training and robust email filtering systems are crucial in preventing these attacks.",
#     likes=0
# )

# Post.objects.create(
#     category=category_cybersecurity,
#     author=user,
#     content="Ransomware attacks have become increasingly sophisticated, with cybercriminals encrypting important files and demanding payments in exchange for decryption keys. To defend against these attacks, regular data backups, secure networks, and strong user authentication protocols must be in place to mitigate the risks.",
#     likes=0
# )

# Post.objects.create(
#     category=category_cybersecurity,
#     author=user,
#     content="The growing use of Internet of Things (IoT) devices presents new challenges for cybersecurity. Many IoT devices have weak security features, making them vulnerable to exploitation. It is important to implement network segmentation and enforce strict security measures on all connected devices.",
#     likes=0
# )

# Post.objects.create(
#     category=category_cybersecurity,
#     author=user,
#     content="Zero-day vulnerabilities are a major concern in the cybersecurity world. These are flaws in software or hardware that are unknown to the vendor, and once discovered by cybercriminals, they can be exploited before a fix is developed. Timely patching and monitoring are vital to protect systems from zero-day attacks.",
#     likes=0
# )

################### CATEGORY, POSTS ###################

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    for post in posts:
        post.author_picture = post.author.user_image.url if post.author.user_image else None

    return render(request, 'category_posts.html', {'category': category, 'posts': posts})

def full_post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    post.author_picture = post.author.user_image.url if post.author.user_image else None
    return render(request, 'full_post.html', {'post': post})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.title = form.cleaned_data['title']
            category.description = form.cleaned_data['description']
            category.created_by = request.user
            category.save()
            return redirect('Start page')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def add_post(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category = category
            post.save()
            return redirect('category_posts', category_id=category.id)
    else:
        form = PostForm(initial={'category': category})
    return render(request, 'add_post.html', {'form': form, 'category': category})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("Вы не можете удалить этот пост.")

    if request.method == "POST":
        post.delete()
        return redirect('category_posts', category_id=post.category.id)

    return render(request, 'delete_post.html', {'post': post})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)  
    
    if request.method == 'POST':  
        content = request.POST.get('content')  
        if content:  
            comment = Comment(post=post, author=request.user, content=content)
            comment.save()
            return redirect('full_post', post_id=post.id)
    return HttpResponse("Ошибка при добавлении комментария", status=400)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('full_post', post_id=post_id)
    return render(request, 'delete_comment.html', {'comment': comment})

################### LOGIN, REGISTER(SingUp), LOGOUT, USER PROFILE ###################

def login_user(request:HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('Start page')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_user(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('Start page', permanent=True)
        else:
            return render(request, "signup.html", context={"form": form})
    else:
        return render(request, "signup.html", context={"form": SignUpForm()})
    
def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        logout(request)
        return redirect('/', permanent=True)

@login_required()
def user_profile_details(request:HttpRequest, user_id): 
    user = CustomUser.objects.get(id=user_id)
    form = UserProfileForm(instance=user)
    return render(request, "user_profile_details.html", context={"form": form})

@login_required()
def user_profile_edit(request:HttpRequest, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
                logout(request)
                user.save()
                return redirect('login')
            user.save()    
            image = form.cleaned_data.get('user_image')
            if image:
                user.user_image = image  
                user.save()
            
            return redirect('user_profile_details', user_id=user.id)
        else:
            return render(request, "user_profile_edit.html", context={"form": form})
    else:
        form = UserProfileForm(instance=user)
        return render(request, "user_profile_edit.html", context={"form": form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = PostLike.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        like.delete()
        post.likes -= 1
        post.save()
        liked = False
    else:
        post.likes += 1
        post.save()
        liked = True
    post.save()

    return JsonResponse({'liked': liked, 'likes_count': post.likes})

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)
    
    if not created:
        like.delete()
        comment.likes -= 1
        comment.save()
        liked = False
    else:
        comment.likes += 1
        comment.save()
        liked = True
    comment.save()
    return JsonResponse({'liked': liked, 'likes_count': comment.likes})


###
# post = Post.objects.get(id=2)

# user1 = CustomUser.objects.get(id=1)
# user2 = CustomUser.objects.get(id=2)


# Comment.objects.create(post=post, author=user1, content="Cool post, I love it!")
# Comment.objects.create(post=post, author=user2, content="I agree with your thoughts.")
# Comment.objects.create(post=post, author=user1, content="This is really interesting!")
# Comment.objects.create(post=post, author=user2, content="Well said, couldn't agree more.")
# Comment.objects.create(post=post, author=user1, content="Amazing content, keep it up!")

# print("Comments created successfully!")