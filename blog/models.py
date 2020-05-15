from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from PIL import Image
# import io
# from django.core.files.storage import default_storage as storage


class Blog(models.Model):
    dp_image = models.ImageField(default='default_dp.jpg', upload_to='pictures')
    icon_image = models.ImageField(default='default_icon.jpg', upload_to='icons')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.dp_image.path)
    #
    #     if img.height > 500 and img.width > 500:
    #         output_size = (500, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.dp_image.path)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img_read = storage.open(self.image.name, 'r')
    #     img = Image.open(img_read)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         in_mem_file = io.BytesIO()
    #         img.save(in_mem_file, format='JPEG')
    #         img_write = storage.open(self.image.name, 'w+')
    #         img_write.write(in_mem_file.getvalue())
    #         img_write.close()
    #
    #     img_read.close()

    class Meta:
        ordering = ['-id']
