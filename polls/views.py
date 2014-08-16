from django.shortcuts import render
# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from polls.models import Poll
from polls.models import Count
import gdata.youtube
import gdata.youtube.service


def main(request):
	if not Count.objects.all():
		c = Count()
		c.num = 1
		c.save()
		return HttpResponse("hello world")
	else:
		cnum = Count.objects.all()[0].num
		cnum += 1
		Count.objects.filter(id=1).update(num=cnum)
		return HttpResponse(cnum)

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_poll_list' : latest_poll_list}
	return render(request, 'polls/index.html', context)

def tube(request):
	client = gdata.youtube.service.YouTubeService()
	query = gdata.youtube.service.YouTubeVideoQuery()

	query.vq = 'ミスチル'
	query.max_results = 25
	query.start_index = 1
	query.racy = 'exclude'
	query.orderby = 'relevance'

	entry = client.YouTubeQuery(query).entry
	feed = [x.media.player.url for x in entry]

	context = {'feed' : feed}
	return render(request, 'polls/tube.html', context)
