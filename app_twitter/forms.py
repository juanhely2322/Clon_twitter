from django import forms
from . import models
class creationPost(forms.ModelForm):
    class Meta:
        model= models.post
        fields=["content"]
        widgets={"content": forms.Textarea(attrs={'class':'form-control w-100',
                                                  'id':'contentBox',
                                                  'rows':'3',
                                                  'placeholder':'¿Que estas pensando hoy?'}),}