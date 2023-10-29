from django.forms import ModelForm
from halamanreview.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]