import random
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def random_values(request):
    data = {'list':[
                    {'main': 
                     {'value1': random.randint(0, 1),
                      'value2': random.randint(0, 1),
                      'value3': random.randint(0, 1)}
                    }
                         ]}
    return JsonResponse(data)
donat = 0

@csrf_exempt
def webhook_handler(request):
    global donat

    if request.method == 'POST':
        # Обработка входящего запроса от Twitch
        # Разбор информации о донатах и выполнение необходимых действий

        # Изменяем значение donat на 1
        # global donat_value
        donat = 1
        return HttpResponse(status=200)
    elif request.method == 'GET':
            # При запросе методом GET возвращаем текущее значение donat и сбрасываем его на 0
        response_data = {'list':[
                    {'main': 
                     {'donat': donat,}
                    }
                         ]}

        # Сбрасываем значение donat на 0
        donat = 0

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(status=405)
