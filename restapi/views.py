from .models import Pereval, PerevalImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pereval
from .serializers import PerevalSerializer


class SubmitData(APIView):
    def post(self, request, format=None):
        # Получаем данные из тела запроса
        data = request.data

        # Вызываем метод add_pereval из класса PerevalDataHandler
        result = PerevalDataHandler.add_pereval(data)

        # Проверяем результат операции
        if result['status'] == 200:
            # Если добавление прошло успешно, возвращаем HTTP 200 OK и информацию о добавленной записи
            return Response({"status": 200, "message": "Отправлено успешно", "id": result['id']},
                            status=status.HTTP_200_OK)
        else:
            # Если произошла ошибка, возвращаем соответствующий HTTP статус и сообщение об ошибке
            return Response({"status": 500, "message": result['message'], "id": None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PerevalDataHandler:
    @classmethod
    def add_pereval(cls, data):
        try:
            # Создание нового перевала
            pereval = Pereval.objects.create(
                beauty_title=data.get('beauty_title', ''),
                title=data['title'],
                other_titles=data.get('other_titles', ''),
                connect=data.get('connect', ''),
                add_time=data['add_time'],
                user_email=data['user']['email'],
                user_phone=data['user']['phone'],
                user_fam=data['user']['fam'],
                user_name=data['user']['name'],
                user_otc=data['user']['otc'],
                coords_latitude=data['coords']['latitude'],
                coords_longitude=data['coords']['longitude'],
                coords_height=data['coords']['height'],
                level_winter=data['level'].get('winter', ''),
                level_summer=data['level'].get('summer', ''),
                level_autumn=data['level'].get('autumn', ''),
                level_spring=data['level'].get('spring', ''),
                status='new'  # Устанавливаем статус "new" по умолчанию
            )

            # Добавление изображений перевала, если они есть
            images_data = data.get('images', [])
            for image_data in images_data:
                PerevalImage.objects.create(pereval=pereval, title=image_data['title'], image=image_data['data'])

            return {"status": 200, "message": "Отправлено успешно", "id": pereval.id}
        except Exception as e:
            return {"status": 500, "message": str(e), "id": None}



class PerevalDetailView(APIView):
    def get_object(self, pk):
        try:
            return Pereval.objects.get(pk=pk)
        except Pereval.DoesNotExist:
            return None

    def get(self, request, id):
        pereval = self.get_object(id)
        if pereval:
            serializer = PerevalSerializer(pereval)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        pereval = self.get_object(id)
        if not pereval:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if pereval.status != 'new':
            return Response({'state': 0, 'message': 'Cannot edit record with status other than "new".'})

        serializer = PerevalSerializer(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'state': 1})
        else:
            return Response({'state': 0, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PerevalByUserEmailView(APIView):
    def get(self, request):
        email = request.query_params.get('user__email', None)
        if email is not None:
            perevals = Pereval.objects.filter(user_email=email)
            serializer = PerevalSerializer(perevals, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)