from django.shortcuts import render, render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

# Create your views here.
class ContactWizard(SessionWizardView):
    template_name = "contact_form.html"
    
    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        
        return render_to_response('done.html', {'form_data': form_data})