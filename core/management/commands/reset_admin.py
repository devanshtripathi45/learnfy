from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
	help = "Create or update admin user 'devansh' (password: deva@1231)"

	def handle(self, *args, **options):
		User = get_user_model()
		username = 'devansh'
		password = 'deva@1231'  # set by user request
		user, created = User.objects.get_or_create(username=username, defaults={
			'is_staff': True,
			'is_superuser': True,
		})
		user.is_staff = True
		user.is_superuser = True
		user.set_password(password)
		user.save()
		if created:
			self.stdout.write(self.style.SUCCESS(f"Created admin user '{username}'."))
		else:
			self.stdout.write(self.style.SUCCESS(f"Updated password and permissions for '{username}'."))
