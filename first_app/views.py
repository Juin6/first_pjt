from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


def root(request):
    return render(request, 'root.html')

def hello(request):
    username = 'June'

    context = {
        'username': username,
    }

    return render(request, 'hello.html', context)

def lunch(request):
    menus = ['김밥', '라면', '돈까스']

    pick = random.choice(menus)

    context = {
        'pick': pick
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    #lotto = ''
    #for i in range(6):
    #    lotto = lotto + ' ' + random.choice(range(1,46))
    
    def random_number():
        return str(sorted(random.sample(range(1,46), 6)))
    
    lotto = random_number

    context = {
        'lotto': lotto
    }

    return render(request, 'lotto.html', context)