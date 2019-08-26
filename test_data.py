# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'decrypt_tokyo.settings')
django.setup()

from idol_token.models import Idol, Idol_Item
from cloudinary import CloudinaryImage
import cloudinary, cloudinary.uploader, cloudinary.forms, cloudinary.api
from django.http import HttpResponse, JsonResponse

if __name__ == '__main__':

    kk = '1243567654ffdsadfsdf'

    idol = Idol.objects.filter(address=kk).first()

    io = {
        'id': idol.id,
        'name': idol.name,
        'image': idol.image,
        'address': idol.address
    }
    kio = JsonResponse(io)
    print(kio)



    # image='いくた.jpeg'
    #
    # ret = cloudinary.uploader.upload(image, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')
    # url = ret['secure_url']
    #
    #
    # idol = Idol.objects.create(
    #     name='生田絵梨花',
    #     image=url,
    #     address='1243567654ffdsadfsdf'
    # )
    # idol.save()
    # print(idol)
    #
    # image2 = 'dEcfeNTso1tI5LIG3YOvtk5kFJzXkAL175KsGPKtRCQ.jpg'
    # ret2 = cloudinary.uploader.upload(image2, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')
    # url2 = ret2['secure_url']
    #
    # idol2 = Idol.objects.create(
    #     name='丹生明里',
    #     image=url2,
    #     address='htryrt4t34rjfiejriwejfdiewjfd'
    #
    # )
    # idol2.save()
    #
    # print(Idol.objects.all())
    #
    # print(idol2)
