from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
settings.configure()


send_mail("Test Email", "This is a simple text email body.",
  "ochomoswill <hello@ochomoswill.com>", ["ochomoswill@gmail.com"])

# or
# mail = EmailMultiAlternatives(
#     # subject="Your Subject",
#     # body="This is a simple text email body.",
#     from_email="ochomoswill <hello@ochomoswill.com>",
#     to=["ochomoswill@gmail.com"],
#     headers={"Reply-To": "ochomoswill@gmail.com"}
# )
# Add template
# mail.template_id = '30b8a992-b0e7-4579-ba2b-d35a457c8f6c'

# Replace substitutions in sendgrid template
# mail.substitutions = {'%Sender%': 'Derek Prince'}

# Attach file
# with open('somefilename.pdf', 'rb') as file:
#     mail.attachments = [
#         ('somefilename.pdf', file.read(), 'application/pdf')
#     ]
#
# mail.attach_alternative(
#     "<p>This is a simple HTML email body</p>", "text/html"
# )

# mail.send()
