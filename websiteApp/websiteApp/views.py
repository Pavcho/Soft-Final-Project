from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main_templates/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
            if len(user.username) > 7:
                context['username'] = user.username[:7] + '...'
        return context
