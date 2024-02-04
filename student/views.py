import math

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from blockchain.models import Block
from blockchain.views import blockchain, blockchain_log, blockchain_log_list
from common import fail, success
from student.serializers import MentalMessagesSerializer
from student.models import MentalMessages


# Create your views here.
# 上链操作以及信息保存

class AddMentalMessages(APIView):
    def post(self, request):
        data = request.data
        mental_model = MentalMessages.objects.filter(name=data["name"]).first()
        if mental_model is not None:
            return fail('学生信息已存在')
        # if "cover" in data and data["cover"]:
        #     serializers.change_tmg_to_use(data["cover"])
        mental_serializer = MentalMessagesSerializer(data=data)
        if mental_serializer.is_valid():
            mental_serializer.save()
            student = MentalMessages.objects.filter(name=data["name"]).first()
            print(student.id)

            blockchain.chain = blockchain_log_list  # 读取数据库中的块
            #  新建交易数据
            index = blockchain.new_transaction(student.name, student.sex, student.class_name, student.phone,
                                               student.grade_time)
            print(f'数据将会被添加到块  {index}')
            #  打包区块
            last_block = blockchain.last_block  # 获取链上最后一个区块的信息
            #  工作量证明计算
            last_proof = last_block['proof']
            proof = blockchain.proof_of_work(last_proof)
            #  生成一个新块
            block = blockchain.new_block(proof, student_id=student.id, data=data)
            #  存入数据库
            blockchain_log_new = Block()  # 初始化model类，并存入新块的数据
            blockchain_log_new.index = block['index']
            blockchain_log_new.time_stamp = block['time_stamp']
            blockchain_log_new.trade = block['trade']
            blockchain_log_new.proof = block['proof']
            blockchain_log_new.student_id = block['student_id']
            blockchain_log_new.data = block['data']
            blockchain_log_new.self_hash = block['self_hash']
            blockchain_log_new.pre_hash = block['pre_hash']
            blockchain_log_new.save()
            print(block)
            response = {
                'respond': '数据上链成功',
                'chain': blockchain.chain,
                'length': len(blockchain.chain)
            }
            return JsonResponse(response)
        return fail(mental_serializer.errors)


# 删除信息
class DeleteMentalMessages(APIView):
    def post(self, request):
        try:
            pk = request.data["id"]
            mental = MentalMessages.objects.get(id=pk)
            mental.delete()
            return success('数据删除成功')
        except MentalMessages.DoesNotExist:
            return fail('健康信息不存在')


# 更新健康信息
class UpdateMentalMessages(APIView):
    def post(self, request):
        try:
            pk = request.data["id"]
            mental = MentalMessages.objects.get(id=pk)
            data = request.data
            mental.rolename = data.get('rolename', mental.rolename)
            mental.cover = data.get('cover', mental.cover)
            mental.remark = data.get('remark', mental.remark)
            mental.save()
            return success('角色更新成功')
        except MentalMessages.DoesNotExist:
            return fail('角色不存在')


# 根据id查找健康信息
class GetMentalMessages(APIView):
    def post(self, request):
        try:
            pk = request.data["id"]
            mental = MentalMessages.objects.get(id=pk)
            mental_serializer = MentalMessagesSerializer(mental)
            return success(mental_serializer.data)
        except MentalMessages.DoesNotExist:
            return fail('角色不存在')


# 查找所有学生健康信息
class GetAllMentalMessages(APIView):
    def post(self, request):
        mental = MentalMessages.objects.all()
        mental_serializer = MentalMessagesSerializer(mental, many=True)
        # 区块链验证
        blockchain.chain = blockchain_log_list  # 读取数据库中的块
        if blockchain.vaild_chain(blockchain.chain):
            return success(mental_serializer.data)
        else:
            return fail('区块链验证错误')

# 分页查询学生健康信息
class GetMentalPageList(APIView):
    def post(self, request):
        page = int(request.data.get('page', 1))  # get the current page number, default is 1
        size = int(request.data.get('size', 10))  # get the number of items per page, default is 10
        key = request.data.get('key', '')  # get the search keyword

        mental = MentalMessages.objects.filter(name__contains=key)  # filter users based on the search keyword
        total_count = mental.count()  # total number of users

        # Calculate the number of pages
        total_pages = math.ceil(total_count / size)

        # Calculate the starting and ending indices of users to retrieve based on the current page
        start_index = (page - 1) * size
        end_index = start_index + size

        # Retrieve the users for the current page
        users_page = mental[start_index:end_index]

        # Serialize the users
        serializer = MentalMessagesSerializer(users_page, many=True)

        # Prepare the response data
        data = {
            'total_count': total_count,
            'total_pages': total_pages,
            'current_page': page,
            'per_page': size,
            'mental': serializer.data
        }
        blockchain.chain = blockchain_log_list  # 读取数据库中的块
        if blockchain.vaild_chain(blockchain.chain):
            return success(data=data)
        else:
            return fail('区块链验证错误')

