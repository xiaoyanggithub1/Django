import os
import uuid
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

from common import success
from upload_common.models import PictureModel, HomeIcon, Order
from upload_common.serializers import HomeIconuSerializer, OrderSerializer


class UploadView(APIView):
    def post(self, request):
        file = request.FILES['file']
        type = file.name.split('.')[-1]
        file_size = 100000 * 5  # 5M
        if file.content_type != 'image/jpeg':
            return Response({'message': '只允许上传图片'}, status=400)
        if type != 'jpg':
            return Response({'message': '只允许上传jpg图片'}, status=400)
        if file.size > file_size:
            return Response({'message': '图片文件过大不允许上传！'}, status=400)
        filePath = f'public/img/{datetime.now().strftime("%Y/%m/%d")}'
        if not os.path.isdir(filePath):
            os.makedirs(filePath)
        fileName = f'/{uuid.uuid4().hex}.{type}'
        try:
            with open(f'{filePath}{fileName}', 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            # data = {'path': f'{filePath}{fileName}', 'name': file.name, 'size': file.size}
            path = f'{filePath}{fileName}'
            name = file.name
            size = file.size
            pictureModel = PictureModel(path=path, name=name, size=size)
            pictureModel.save()
            return Response({'path': f'{filePath}{fileName}'}, status=200)
        except Exception as e:
            return Response({'message': '图片上传失败！'}, status=500)


# 图片删除
class DeleteImageView(APIView):
    def post(self, request):
        name = request.data.get('name')
        try:
            picture = PictureModel.objects.get(name=name)
            file_path = picture.path
            if os.path.exists(file_path):
                os.remove(file_path)
                picture.delete()
                return Response({'message': '图片删除成功！'}, status=200)
            else:
                return Response({'message': '图片不存在！'}, status=400)
        except  PictureModel.DoesNotExist:
            return Response({'message': '图片不存在！'}, status=400)
        except  Exception as e:
            return Response({'message': '图片删除失败！'}, status=500)


class GetHomeIcon(APIView):
    def post(self, request):
        home_icon = HomeIcon.objects.all()
        role_serializer = HomeIconuSerializer(home_icon, many=True)
        return success(role_serializer.data)


class OrderData(APIView):
    def post(self, request):
        order = Order.objects.all()
        order_serializer = OrderSerializer(order, many=True)
        return success(order_serializer.data)
