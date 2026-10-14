from django.db import models
import os

class SharedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.file.name)

    def filesize_mb(self):
        try:
            return round(self.file.size / (1024 * 1024), 2)
        except:
            return 0
