from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from common.util.auth_util import login_required

from suggest.models import Suggestion


# Create your views here.
@require_http_methods(['GET'])
@login_required
def suggest_list(request):
    suggestions = Suggestion.objects.order_by('-updated_at'). \
        filter(user_id=request.user.id). \
        select_related('place'). \
        prefetch_related('hashtag').all()

    result = []
    for suggestion in suggestions:
        result.append({
            'id': suggestion.id,
            'place': {
                'name': suggestion.place.name,
                'lat': suggestion.place.latitude,
                'lng': suggestion.place.longitude,
                'score': suggestion.place.avg_score
            },
            'updated_at': suggestion.updated_at,
            'status': suggestion.status,
            'hashTags': [tag.hashtag_name for tag in suggestion.hashtag.all()]
        })
    return JsonResponse({'suggestList': result}, safe=False)


@require_http_methods(['GET'])
@login_required
def suggest(request, suggest_id):
    return JsonResponse({'suggest': suggest_id}, safe=False)
