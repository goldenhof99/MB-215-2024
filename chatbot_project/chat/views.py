from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.http import JsonResponse
from django.shortcuts import render
import datetime

chatbot = ChatBot('ChatBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

def home(request):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'chatbot/home.html', {'current_time': current_time})

def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_response = chatbot.get_response(user_message)
        return JsonResponse({'user_message': user_message, 'bot_response': str(bot_response)})
    return render(request, 'chatbot/chat.html')



