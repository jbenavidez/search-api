from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from api.services import UtilityService
from api.services import SearchService
import logging
import json


logger = logging.getLogger(__name__)


@api_view(['GET'])
@csrf_exempt
def search_api(request):
    """This API is used search"""
    try:
        received_data = request.GET
        if received_data.get('q', None) is None:
            err = 'empty search params'
            return JsonResponse(
                    UtilityService.generate_response(400, 'fail', err),
                    status=400)
        response = UtilityService.generate_response(200, 'success')
        response['data'] = SearchService.\
            search(json.loads(json.dumps(received_data)))
        return JsonResponse(response, status=200)

    except Exception as e:
        logger.exception(e)
        err = f"Error while trying to search: {str(e)}"
        return JsonResponse(
                UtilityService.generate_response(500, 'error',  err),
                status=500)
