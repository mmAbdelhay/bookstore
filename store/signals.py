# from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
# from django.dispatch import receiver
#
# from .models import Store,User,Isbn
# from django.core.mail import send_mail
#
#
# @receiver(post_save,sender=Store)
# def after_book_creation(sender, instance, created, *args, **kwargs):
#     if created:
#         isbn_instance = Isbn.objects.create(title=instance.title)
#
#
#         isbn_instance.save()
#         instance.isbn = isbn_instance
#
#         send_mail('New Book{}',format(instance.title),'')
#     else:
#         print("")