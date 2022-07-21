from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import mail_admins

from .forms import ContactFormForm


def about(request):
    is_sent = False
    form = ContactFormForm(request.POST or None)
    if form.is_valid():
        data = form
        form = form.save(commit=False)
        form.message = form.message[:1000]
        form.save()
        is_sent = True
        subject = f"Ticket number {form.id}"
        body = {
            'subject': subject,
            'name': data.cleaned_data['name'],
            'email': data.cleaned_data['email'],
            'message': data.cleaned_data['message'],
        }
        message = "\n\n".join(body.values())
        email_template = render_to_string(
            'contact/email/contact_form_mail.html', body)
        mail_admins(subject, message, html_message=email_template)

    context = {
        'form': form,
        'is_sent': is_sent,
    }
    return render(request, 'contact/about.html', context)
