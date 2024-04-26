from django.http import JsonResponse


def contact_form(request):
    # Your form processing logic here
    # Assuming the form was sent successfully
    message = "Your custom success message here."
    return JsonResponse({"message": message})
