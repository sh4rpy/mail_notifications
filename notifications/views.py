from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import NotificationForm
from .models import Notification
from .tasks import send_notification_task


class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/index.html'
    context_object_name = 'notifications'


class CreateNotificationView(CreateView):
    form_class = NotificationForm
    template_name = 'notifications/create_or_update_notification.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        notification = form.save(commit=False)
        notification.author = self.request.user
        notification.save()
        form.save_m2m()
        emails = [participant.email for participant in notification.participants.all()]
        send_notification_task.apply_async(
            (notification.subject, notification.message, emails),
            eta=notification.send_at
        )
        return super().form_valid(form)


class UpdateNotificationView(UpdateView):
    form_class = NotificationForm
    template_name = 'notifications/create_or_update_notification.html'
    success_url = reverse_lazy('list')
    queryset = Notification.objects.all()


class DeleteNotificationView(DeleteView):
    model = Notification
    success_url = reverse_lazy('list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
