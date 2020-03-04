# author : Hao, Sam


from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.http import Http404
from app.models import Gamecode
from app.models import Questions

# current node number, global variable
num = 1


def index(request):
    # sets the node num to 1 when landing on index page
    global num
    num = 1
    return render(request, 'app/index.html')


def redirect(request):

    global num
    # Below is to check if whether the button is for groupcode or answer to question
    # process the group code passed from the landing page
    if request.method == 'POST' and 'submit-groupcode' in request.POST:
        groupcode = str(request.POST.get('groupCode'))    # Get inputted groupcode from the user
        print(Gamecode.objects.all())

        info = Questions.objects.filter(node_num=int(num))    # Get question from the database using num counter

        # if the group code exists, load the treasure hunt page with the correct questions
        if Gamecode.objects.filter(groupcode=groupcode).exists():
            request.session['groupcode'] = groupcode         # Add group code into user's session
            return render(request, 'app/studentview.html',{"groupcode":groupcode, "data":info, "id":id})

        # otherwise show an error message
        else:
            print("Wrong")
            messages.error(request, 'The game code does not exist')
            return render(request, 'app/index.html')

    # if an answer to question is submitted, check if it is correct
    if request.method == 'POST' and 'submit-question' in request.POST:
        groupcode = request.session['groupcode']            # Get groupcode from user's sessio
        data = str(request.POST.get('answer'))              # Get text from the input answer box

        # if answer is correct for the current node, move onto the next question if it exists, 
        # otherwise show they have finished the quiz
        # Check if user get's the answer correct
        if Questions.objects.filter(answers__icontains=data.strip(), node_num=int(num)).exists():
            num += 1       # Add 1 to the counter so the questions moves on to the next one
            # Check whether if the user is on the last question
            if Questions.objects.filter(node_num=int(num)).exists():
                info = Questions.objects.filter(node_num=num)
                messages.success(request, 'Correct!')  # Generate message saying correct
                return render(request, 'app/studentview.html',{"groupcode":groupcode,"data":info,"id":id})
            else:                 # Case when the user is on the last question
                num -=1      # Question stays the same when user has reach the end
                info = Questions.objects.filter(node_num=num)
                # Generate message when user finish the quiz
                messages.success(request, 'You have finished the quiz, well done!')
                return render(request, 'app/studentview.html', {"groupcode": groupcode, "data": info, "id": id})
        else:         # Case when user gets the answer wrong

            info = Questions.objects.filter(node_num=num)
            messages.error(request, 'That is the wrong answer, please try again')
            # Return incorrect message
            return render(request, 'app/studentview.html', {"groupcode": groupcode, "data": info, "id": id})
    print(request.method)


def hint(request):
    hint_get = Questions.objects.values_list('hints',flat=True).filter(node_num=num)
    print(hint_get)
    return HttpResponse(hint_get)


def update_request(request):
    question_num = request.POST.get('current_question')
    group_num = request.session['groupcode']
    print(question_num)
    print(group_num)
    latest_question = Gamecode.objects.get(groupcode=group_num)
    latest_num = latest_question.
    print(latest_question)
    if question_num != latest_question:
        print("Not the same question")
    else:
        print("Same question")
    return HttpResponse("Hello")


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def MVP_treasure_hunt(request):
    return render(request, 'app/MVP_treasure_hunt.html')


def studentview(request):
    return render(request,'app/studentview.html')
