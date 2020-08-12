from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.core.exceptions import PermissionDenied

# from django.core.mail import send_mail
# send_mail('Subject here', 'Here is the message.', 'eminli.turan@gmail.com', ['eminli.turan@gmail.com'], fail_silently=False)


# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# EMAIL CONFIRMATION


# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.template.loader import render_to_string

# def success(request, uid):

#     email = EmailMessage(
#         'subject', 
#         'body', 
#         settings.EMAIL_HOST_USER, 
#         ['storylino@gmail.com'],
#     )

#     email.fail_silently=False
#     email.send()

#     user = User.objects.get(id=uid)
#     context = {
#         'users': user, 
#     }

#     return render(request, 'success.html', context)


