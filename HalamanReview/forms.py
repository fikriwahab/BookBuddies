from django.forms import ModelForm
from HalamanReview.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]