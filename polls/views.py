# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response #form
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from polls.models import Poll
from polls.models import Count
from polls.forms import CountForm
import gdata.youtube
import gdata.youtube.service
from django.template import RequestContext


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

def form(request):
	if request.method == "POST": #requestがPOSTかGETか判別
		form = CountForm(request.POST) #request.POSTは辞書のようなデータなのでそのままEntryFormに渡せる
		print request.POST
		print request.POST['num']
		if form.is_valid(): # エラーがないか判別
			Count.objects.filter(id=1).update(num= request.POST['num'])
			form = CountForm() #保存したのでフォームを空に、is_valid()でFalseの場合はerrosや入れられた値を持ったまま
	else:
		form = CountForm() #GETなので空のフォームを作る
		if not Count.objects.all():
			c = Count()
			c.num = 1
			c.save()
		else:
			cnum = Count.objects.all()[0].num
			cnum += 1
			Count.objects.filter(id=1).update(num=cnum)

	# cnums = [x.num for x in Count.objects.all()]
	cnum = Count.objects.all()[0].num
	# formとobject_listをテンプレートに渡す
	return  render_to_response("form.html",RequestContext(request,{"form":form,"cnum":cnum}))
