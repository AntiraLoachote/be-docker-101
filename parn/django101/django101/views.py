from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template = 'home_view.html'

    def get(self, request):
        return render(
            request=request,
            template_name=self.template
        )
