from django.shortcuts import render,redirect

from django.views import View
from .models import Topic

class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        return redirect("bbs:index")

index   = IndexView.as_view()


"""
from django.shortcuts import render,redirect
from django.views import View

from django.http import JsonResponse
#from asgiref.sync import database_sync_to_async # ← 存在しない。
#from django.db.async_unsafe import sync_to_async

from .models import Topic


# データベースから非同期にデータを取得する関数
# @database_sync_to_async
@sync_to_async
def get_data_from_db():
    return list(Topic.objects.all().values())


# 非同期ビュー
async def async_view(request):
    # 非同期にデータを取得
    data = await get_data_from_db()
    return JsonResponse(data, safe=False)

class IndexView(View):

    async def get(self, request, *args, **kwargs):

        data = await get_data_from_db()
        print(data)
        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    async def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        return redirect("bbs:index")

index   = IndexView.as_view()

"""

