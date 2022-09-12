from django.views.generic import ListView
from


def index(ListView):
    form = MyForm()
    rendered_form = form.render("form_snippet.html")
    context = {'form': rendered_form}
    return render(request, 'index.html', context)