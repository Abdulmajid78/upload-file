import telegram
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import View
from django.views.generic.edit import FormMixin
from telegram import Bot

from config import settings
from .forms import ContactsForm


class HomeView(CreateView):
    form_class = ContactsForm
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactsForm()
        return context

    def get_success_url(self):
        return reverse('home')


class ContactCreateView(View, FormMixin):
    form_class = ContactsForm
    template_name = 'index.html'
    success_url = reverse_lazy('home')

    async def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            group_name = form.cleaned_data['group_name']
            radio = form.cleaned_data["radio"]


            bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
            chat_id = settings.TELEGRAM_CHAT_ID
            message = f"Yangi habar: \n    Ismi: {full_name}dan \n    Guruh nomi: {group_name}\n    Test turi: {radio} \n ***end***"

            try:
                await bot.send_message(chat_id=chat_id, text=message)
            except telegram.error.TelegramError:
                return render(request, "index.html", ({'error': 'Failed to send message'}))

            return super().form_valid(form)

        return render(request, "index.html", {'form': form})

    async def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return render(request, self.template_name, {'form': form})
