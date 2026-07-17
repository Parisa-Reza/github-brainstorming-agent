from django import forms


class ChatForm(forms.Form):

    question = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder":
                "Ask about the repository..."
            }
        )
    )