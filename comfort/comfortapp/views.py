#!/usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import index
from background_task import background
from django.contrib.auth.models import User
import pika
import time
import datetime
from django.utils import timezone

from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import task


def insert():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	method_frame, header_frame, body = channel.basic_get('hello')
	corpo = body
	if method_frame:
	    print method_frame, header_frame, body
	    channel.basic_ack(method_frame.delivery_tag)
	else:
	    print 'No message returned'

	load = task(task_name="hello ww", task_desc=corpo,data_created=timezone.now())
	load.save()
	return "salvo"


class TaskViewSet(viewsets.ModelViewSet):
	queryset = task.objects.all().order_by('-data_created')
	serializer_class = TaskSerializer

def single():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	method_frame, header_frame, body = channel.basic_get('hello')
	corpo = body
	if method_frame:
	    print method_frame, header_frame, body
	    channel.basic_ack(method_frame.delivery_tag)
	else:
	    print 'No message returned'
	return corpo

corpo = ''




def load_one_message():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	corpo =""
	# Get ten messages and break out
	for method_frame, properties, body in channel.consume('hello'):

	    # Display the message parts
	    print method_frame
	    print properties
	    print body
	    corpo = body
	    # Acknowledge the message
	    channel.basic_ack(method_frame.delivery_tag)

	    # Escape out of the loop after 10 messages
	    if method_frame.delivery_tag == 1:
	        break

	# Cancel the consumer and return any pending messages
	requeued_messages = channel.cancel()
	print 'Requeued %i messages' % requeued_messages

	# Close the channel and the connection
	channel.close()
	connection.close()
	return corpo


@background(schedule=5)
def loading_temp(valor):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.26.50.120'))
	channel = connection.channel()
	#channel.queue_declare(queue='hello', durable=True)
	#print(' [*] Waiting for messages. To exit press CTRL+C')

	
	def callback(ch, method, properties, body):
	    print(" [x] Received %r" % body)
	    ch.basic_ack(delivery_tag = method.delivery_tag)
	    

	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(callback,queue='hello')
	channel.start_consuming()
	return valor

def send_message(queue, message):
	connection = pika.BlockingConnection(pika.ConnectionParameters('172.26.50.120'))
	channel = connection.channel()
	channel.basic_publish(exchange='', routing_key=queue,body=message)
	connection.close()


# Create your views here.

def home(request):
	preference = "8"

	template = 'index.html'
	#loading = single()
	if request.method == 'POST':
		form = index(request.POST)
		if form.is_valid():
			preference = form.cleaned_data['preference']
			request.session['preference'] = preference
	#If the variable session exist 
	#print 'single', loading
	return render(request,template)


def strategies(request):
	salvo=insert()
	preference = request.session['preference'] # The frist thin to do is set the prefernce temperature when we open this form 
	queue = "hello" # name of the queue that will receive the temperature
	send_message(queue, preference)
	template ="strategies.html"
	print salvo
	return render(request, template,{'preference':request.session['preference']})








