from django.urls import path

from . import contentviews

urlpatterns = [
    path('xchk_javascript_content_demo', contentviews.DemoJavascriptView.as_view(), name=f'{contentviews.DemoJavascriptView.uid}_view'),
]
