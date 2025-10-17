from django.db import models


class About(models.Model):
	"""Site owner's about section editable from admin."""
	name = models.CharField(max_length=100, default='LearnWithShivam')
	photo = models.ImageField(upload_to='about/', blank=True, null=True)
	about_text = models.TextField(blank=True)

	class Meta:
		verbose_name = 'About'
		verbose_name_plural = 'About'

	def __str__(self):
		return self.name


class ContactMessage(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.name} <{self.email}> - {self.created_at:%Y-%m-%d}"
