# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.conf import settings
import boto3, os
from models import Document
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from storage_backends import MediaStorage

# Create your views here.
def index(request):    
    """ Home page view """
    # form = UploadFileForm()
    if request.method=="POST":
        # form = UploadFileForm(request.POST, request.FILES)
        print "post view"        
        print request.POST
        print request.POST.get("age")
        object_name = request.FILES['upload_pic']
        img_file_name = request.FILES['upload_pic'].name
        print img_file_name, object_name
        print type(img_file_name), type(object_name)
        print "home"
        print "before MediaStorage"
        ms = MediaStorage()
        ms.save(str(img_file_name), object_name)
        print "afer MediaStorage"
        print ms

        # s3_client = boto3.client('s3', region_name='ap-south-1', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        #      aws_secret_access_key= settings.AWS_SECRET_ACCESS_KEY)

        # # s3_client = boto3.client('s3')
        # response = s3_client.list_buckets()
        # print "==", response

        # for bucket in response['Buckets']:
        #     print(f'  {bucket["Name"]}')
        # Suni@1994, sunithaswain9@gmail.com

        s3 = boto3.resource('s3', region_name='ap-south-1', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
             aws_secret_access_key= settings.AWS_SECRET_ACCESS_KEY)
        bucket = s3.Bucket('imageuploadingbloom')
        print "***"*30
        print bucket
        print bucket.get_available_subresources()
        print bucket.multipart_uploads.all()
        objects =  bucket.objects.all()
        print objects

        for obj in objects:
            print object.download_file()

        # # uploading an image file into AWS s3 bucket
        # upload = s3_client.upload_file(img_file_name, 'sunitha-sample-bucket', object_name)
        # print upload



        # return render(request, 'index.html', {})
        return HttpResponseRedirect('/application/step2/')
        return HttpResponse("next page we vl check later")

    else:
    
        return render(request, 'index.html', {})

def step2(request):
    """ Passport page view """
    print "passport"
    return render(request, 'step2.html', {})
def step3(request):
    """ Passport page view """
    print "all done"
    return render(request, 'step3.html', {})
    