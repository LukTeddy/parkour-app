from django import forms
from .models import Spot, Comment, CommentMedia

class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = ['name', 'description', 'latitude', 'longitude']

        def save(self, commit=True):
            spot = super.save(commit=False)
            if commit:
                spot.user = self.request.user
                spot.save()
            return spot

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'is_challenge']
    is_challenge = forms.BooleanField(required=False, initial=False, label="Is this a challenge?")

class CommentMediaForm(forms.ModelForm):
    class Meta:
        model = CommentMedia
        fields = ['media_file', 'media_type']
    media_file = forms.FileField(required=False)
    media_type = forms.ChoiceField(choices=[('image', "Image"), ('video', 'Video')])
