from django.http import JsonResponse

from .utils import run_etl_with_limit_util


def run_etl_with_limit(request):
    # Retrieve the limit value from the request parameters
    limit = request.GET.get('limit', 100)

    # Check if limit is provided
    try:
        # Call the run_etl_with_limit_util function with the provided limit value
        limit = int(limit)
        result = run_etl_with_limit_util(limit)
        # Process the result or return it as needed
        return JsonResponse({'success': result}, status=200)
    except Exception as e:
        # Handle exceptions if any
        # raise e // Uncomment this and comment the below line to debug an exception.
        return JsonResponse({'error': str(e)}, status=500)
