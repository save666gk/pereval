
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pereval, PerevalImage


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
