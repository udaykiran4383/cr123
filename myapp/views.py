# views.py

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import os    
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .models import UserProfile,College


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


class GetDistrictsView(View):
    def get(self, request, state_name):
        file_path = os.path.join(settings.BASE_DIR, 'static/states_districts.json')
        with open(file_path) as f:
            data = json.load(f)

        state_data = next((state for state in data['states'] if state['state'] == state_name), None)
        if state_data:
            districts = [district['name'] for district in state_data['districts']]
            return JsonResponse(districts, safe=False)
        else:
            return JsonResponse([], safe=False)

class GetCollegesView(View):
    def get(self, request, state_name, district_name):
        file_path = os.path.join(settings.BASE_DIR, 'static/states_districts.json')
        with open(file_path) as f:
            data = json.load(f)

        state_data = next((state for state in data['states'] if state['state'] == state_name), None)
        if state_data:
            district_data = next((district for district in state_data['districts'] if district['name'] == district_name), None)
            if district_data:
                return JsonResponse(district_data['colleges'], safe=False)
        return JsonResponse([], safe=False)

@method_decorator(csrf_exempt, name='dispatch')    
class SubmitFormView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        state = data.get('state')
        district = data.get('district')
        college_name = data.get('college')
        new_college = data.get('new_college')
        year_of_study = data.get('year_of_study')

        print(f"Received data: {data}")

        if new_college:
            college, created = College.objects.get_or_create(name=new_college)
            if created:
                print(f"New college created: {new_college}")
                self.update_json_file(state, district, new_college)
            else:
                print(f"New college not created, already exists: {new_college}")
        else:
            college = get_object_or_404(College, name=college_name)

        user = UserProfile.objects.create(
            name=name,
            phone=phone,
            state=state,
            district=district,
            college=college,
            year_of_study=year_of_study
        )

        return JsonResponse({"message": "Form submitted successfully."})

    def update_json_file(self, state, district, new_college):
        file_path = os.path.join(settings.BASE_DIR, 'static/states_districts.json')
        print(f"Updating JSON file at: {file_path}")
        
        with open(file_path, 'r+') as f:
            data = json.load(f)
            state_data = next((s for s in data['states'] if s['state'] == state), None)
            if state_data:
                print(f"Found state: {state}")
                district_data = next((d for d in state_data['districts'] if d['name'] == district), None)
                if district_data:
                    print(f"Found district: {district}")
                    if new_college not in district_data['colleges']:
                        district_data['colleges'].append(new_college)
                        print(f"Added new college to district: {new_college}")
                    else:
                        print(f"College already exists in district: {new_college}")
            else:
                print(f"State not found: {state}")
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print("JSON file updated.")