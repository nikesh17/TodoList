from django import forms
from todofeature.models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = "__all__"
        #exclude = ("image", )
        # widgets = {
        #     'name' : (forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'})),
        #     'description' : (forms.Textarea(attrs={'class':'form-control', 'row':3, 'placeholder':'Write something....'})),
        #     'image' : (forms.FileInput(attrs={'class':'form-control-2', 'id' : 'image_field'})),
        #     'task_date' : (forms.SelectDateWidget),
        #     'priority' : (forms.Select(attrs={'class':'form-control'})),
        #     'category' : (forms.Select(attrs={'class':'form-group'})),
        #     'labels' : (forms.CheckboxSelectMultiple(attrs={'class':'form-group'})),

        # }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"]="form-control"
        
        
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name.isdigit():
            raise forms.ValidationError("Name cannot be number")
        return name