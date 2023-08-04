from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver


class User(AbstractBaseUser):
    pass


class Profile(models.Model):
    text = models.CharField(max_length=32, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")


class Product(models.Model):
    name = models.CharField(max_length=32)
    creator = models.ForeignKey(
        Profile, related_name="products", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    reply_to_coment = models.ForeignKey(
        "Comment",
        on_delete=models.CASCADE,
        related_name="replies",
        null=True,
        blank=True,
    )
    comment = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(
        Profile, related_name="rating_replies", on_delete=models.CASCADE
    )


class Rating(models.Model):
    class Meta:
        unique_together = ("author", "product")

    rating = models.SmallIntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, blank=True)

    product = models.ForeignKey(
        Product, related_name="ratings", null=False, on_delete=models.CASCADE
    )
    comment = models.TextField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(
        Profile, related_name="published_ratings", on_delete=models.CASCADE
    )


# Create thumbnail when new stream is created
@receiver(models.signals.post_save, sender=User)
def create_thumbnail(sender, instance: User, created: bool, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
