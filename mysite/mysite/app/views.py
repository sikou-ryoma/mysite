from django.views.generic import View, TemplateView, FormView
from django.shortcuts import render, redirect
from .models import Profile, Work, Post
from .forms import ContactForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        work_data = Work.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })
# プロフィールデータからトップの画像のみ読み出し


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]        
        return render(request, 'app/profile.html', {
            'profile_data': profile_data,        
        })

class ContactView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.first()
        form = ContactForm()
        return render(request, 'app/contact_form.html', {'form': form, 'profile_data': profile_data})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('app:complete'))
        profile_data = Profile.objects.first()  # フォームが無効な場合でもプロフィールデータを表示するために必要
        return render(request, 'app/contact_form.html', {'form': form, 'profile_data': profile_data })

class CompleteView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.first()
        return render(request, 'app/complete.html', {'profile_data': profile_data})
