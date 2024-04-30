from django.db import models
from django.urls import reverse


# Create your models here.

class MailList(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    
    email = models.EmailField()
    status = models.TextField()
    
    status = "success"
    invalid_mail = "" 
    
    # …

    # Metadata
    class Meta:
        ordering = ['email']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('newsuser-detail-view', args=[str(self.id)])
    
    def get_status_value(self):
        if self.status == "success" : 
            return f"sitemiz açıldığında {self.email} adresine mail atacağız."
        elif self.status == "error" : 
            return f"{self.email} geçerli bir email değil."

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.email
    