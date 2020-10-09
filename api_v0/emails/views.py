import os, json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import EmailModel
from .serializers import EmailSerializer

@csrf_exempt
def email_list(request):
    if request.method == 'GET':
        data = EmailModel.objects.all()
        serializer = EmailSerializer(data, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.POST

        full_name = data['full_name']
        email = data['email']
        phone = data['phone']
        message = data['message']

        if full_name and email and phone and message:
            send_email(full_name, email, phone, message)
        else:
            return HttpResponse('Make sure all fields are entered and valid.', status_code=400)

        return JsonResponse(data='', safe=False)


def send_email(full_name, email, phone, message):
    subject = 'Message from the site'
    btype = 'html'
    body = render_to_string(
        'email_sender_form.html', {
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'message': message
        }
    )

    with open(os.path.join(settings.BASE_DIR, "config", "email.json")) as email_conf_file:
        email_conf = json.load(email_conf_file)

    from_mail = email_conf['DEFAULTS']['DEFAULT_FROM_EMAIL']
    to_mail = [email_conf['DEFAULTS']['DEFAULT_TO_EMAIL']]

    with mail.get_connection() as connection:
        email = mail.EmailMessage(
            subject=subject,
            body=body,
            from_email=from_mail,
            to=to_mail,
            connection=connection,
            headers={
                'Priority': 'normal',
                'Precedence': 'buld'
            }
        )
        email.content_subtype = btype
        email.send(fail_silently=False)