from django.shortcuts import redirect


class CustomLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super(CustomLoginRequiredMixin, self).dispatch(request, *args, **kwargs)
