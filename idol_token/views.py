from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from .models import Idol, Idol_Item
import json

# Create your views here.
def top(request):
    data = list(Idol.objects.all()[:4].values('id', 'name', 'image', 'address', 'construct_id'))
    return JsonResponse({'data': data})

# Show the 'Idol' page
def idol(request, idol_id):
    data = list(Idol.objects.filter(id = idol_id).values('id', 'name', 'image', 'address', 'construct_id'))
    return JsonResponse({'data': data})

# Show all Idol data
def all_idol(request):
    data = list(Idol.objects.all().values('id', 'name', 'image', 'address', 'construct_id'))
    return JsonResponse({'data': data})

def get_idol(request):
    if request.method == 'GET':
        address = request.GET.get('address')
        idol = Idol.objects.filter(address=address).first()
        io = {
            'id': idol.id,
            'name': idol.name,
            'image': idol.image,
            'address': idol.address
        }

        return JsonResponse(io)

def get_index(request):
    recomends = Idol.objects.all().order_by('name').values('id', 'name', 'image', 'address')
    recomends_list = list(recomends)
    ranking = Idol.objects.all().order_by('-name').values('id', 'name', 'image', 'address')
    ranking_data = list(ranking)


    data = {
        'recomends': recomends_list,
        'ranking': ranking_data
    }
    return JsonResponse(data)

# Resist Idol
def register_idol(request):
    if request.method == "GET":
        params = request.GET
        name = params.get('name')
        image = request.FILES.get('image')
        if image:
            ret = cloudinary.uploader.upload(image, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')
            url = ret['secure_url']
        else:
            url='https://res.cloudinary.com/hlimgugdc/image/upload/v1560044044/samplename.png'
        address = params.get('address')

        print('ioioio')

        try:
            idol = Idol(
                name = name,
                address = address,
                image=url
            )
            idol.save()
        except Exception as e:
            print(e)
            content = {'message': 'access denied'}
            return JsonResponse(content)
        else:
            data = {
                'id': idol.id,
            }

            return JsonResponse(data)

def register_item(request):
    if request.method == 'GET':
        params = request.GET
        title = params.get('title')
        image = request.FILES.get('image')
        address = params.get('address')
        if address:
            print('取得')
        else:
            address = ''
        if image:
            ret = cloudinary.uploader.upload(image, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')
            url = ret['secure_url']
        else:
            url = 'https://res.cloudinary.com/hlimgugdc/image/upload/v1560035850/samplename.png'

        try:
            item = Idol_Item(
                title=title,
                image=url,
                token=address,
            )
            item.save()
        except Exception as e:
            print(e)
            content = {'message': 'access denied'}
            return JsonResponse(content)
        else:
            data = {
                'id': item.id
            }
            return JsonResponse(data)



def purchase_item(request):
    if request.method == 'POST':
        params = request.POST
        token = params.get('tokenID')
        item = params.get('itemID')

        item = Idol_Item.objects.get(id=item)
        item.token = token
        token.save()

        data = {
            'id': item.id,
        }


        return JsonResponse(data)

def item_detail(request, pk=None):
    if request.method == 'GET':

        try:
            pk = int(pk)
            item = Idol_Item.objects.get(id=pk)
            address = item.token

            idol = Idol.objects.filter(address=address).first()

        except Except as e:
            print(e)
            content = {'message': 'access denied'}
            return JsonResponse(content)
        else:
            data = {
                'title': item.title,
                'idol_name': idol.name
            }

            return JsonResponse(data)
