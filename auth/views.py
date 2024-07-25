# views.py

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def google_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        # token = request.data.get('token')

    # Verify token with Google
    try:
        # Send token to Google for verification
        url = 'https://oauth2.googleapis.com/tokeninfo?id_token=' + token
        response = requests.get(url)

        if response.status_code == 200:
            # Token is valid, extract user information
            user_info = response.json()
            email = user_info.get('email')
            # Check if user with this email exists in your database
            User = get_user_model()
            user, created = User.objects.get_or_create(email=email)

            # Optionally, you can return user data or success message
            return JsonResponse({'message': 'Google login successful', 'user': user.email, 'newCreated': created})
        else:
            # Token verification failed
            return JsonResponse({'error': 'Invalid token'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
