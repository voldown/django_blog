from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed

from .models import Post


class LatestPostFeed(Feed):
 	feed_type = Rss201rev2Feed
 	title = 'Django Blog System'
 	link = '/rss/'
 	description = 'Just Another Django-based Blog Application'

 	def items(self):
 		return Post.objects.filter(status=Post.STATUS_NORMAL)[:5]

 	def item_title(self, item):
 		return item.title

 	def item_description(self, item):
 		return item.desc

 	def item_link(self, item):
 		return reverse('post-detail', args=[item.pk])
