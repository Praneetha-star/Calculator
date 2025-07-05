from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    expression = ''
    result = None

    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            result = eval(expression)  # Simple evaluation (use ast.literal_eval in real apps for safety)
        except Exception:
            result = 'Error'

    return render(request, 'index.html', {
        'expression': expression,
        'result': result
    })

   

# Create your views here.
def game(request):
    result=None
    player1 = ''
    player2 = ''
    
    if request.method=='POST':
        player1 = request.POST.get('player1', '').lower()
        player2=request.POST.get('player2', '').lower()
        
        valid_choices = ['rock','paper','scissor']
        
        if  player1 in valid_choices and player2 in valid_choices:
            if player1 == player2:
                result = 'It\'s a tie!'
        elif(player1=='Rock'and player2=='Scissors') or \
            (player1=='Scissor' and player2=='paper') or \
                (player1=='paper' and player2=='Rock'):
            result="player1 wins!"
        else:
            result="player2 wins!"
            
    else:
        result = 'invalid input! please enter rock,paper,or scissors.'
        
    return render(request,'index2.html', {
        'result': result,
        'player1':player1,
        'player2':player2,
        
    })

from django.shortcuts import render,redirect
from django.http import HttpResponse
def home(request):
    result=None
    if request.method == 'POST':
        a=int(request.POST.get('num1'))
        b=int(request.POST.get('num2'))
        o=request.POST.get('op')
        if o == 'add':
            result=a+b
        #return render(request,'home.html',{'result':result})
        return redirect('hello',result)
    return render(request,'home.html')
def hello(request,result):
    return render(request, 'result.html',{'result':result})

