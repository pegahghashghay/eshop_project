import datetime

from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsModelForm, ProfileForm
from django.views.generic.edit import FormView, CreateView
from site_module.models import SiteSetting
from .models import ContactUs, UserProfile
from contact_module.mongo import contact_us
from contact_module.mongo import creatprofille

def contact_us_page(request):
    if request.method == 'POST':
        # contact_form = ContactUsForm(request.POST)
        # current_contact = ContactUsForm(request.POST(pk=1))
        contact_form = ContactUsModelForm(request.POST)
        # contact_us(request.user, datetime.date)
        if contact_form.is_valid():
            # print(contact_form.cleaned_data)
            # contact = ContactUs(
            #     title=contact_form.cleaned_data.get('title'),
            #     full_name=contact_form.cleaned_data.get('full_name'),
            #     email=contact_form.cleaned_data.get('email'),
            #     message=contact_form.cleaned_data.get('message'),
            # )
            #
            # contact.save()
            # return redirect('home_page')
            contact_form.save()
            # contact_us()


    else:
        # contact_form = ContactUsForm()
        contact_form = ContactUsModelForm()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context


    return render(request, 'contact_module/contact_us_page.html', {
        'contact_form': contact_form
    })

# class ContactUsView(View):
#     def get(self,request):
#         contact_form = ContactUsModelForm()
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form})
#
#
#     def post(self,request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#         return render(request, 'contact_module/contact_us_page.html', {
#                     'contact_form': contact_form
#                 })


# class ContactUsView(CreateView):
#     form_class = ContactUsModelForm
#     template_name = 'contact_module/contact_us_page.html'
#     success_url = '/contact-us/'
#

def store_file(file):
    with open('temp/image.jpg', "wb+")as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'




    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_module/create_profile_page.html', {
            'form': form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            # store_file(request.FILES['profile'])
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            # print(all)
            return redirect('/contact-us/create-profile')

        # profille(full_name='peg',massseg='hello')
        return render(request, 'contact_module/create_profile_page.html', {
            'form': submitted_form
        })



class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'










# from django.views.generic import ListView
#
# from site_module.models import SiteSetting
# from .forms import ContactUsModelForm
# from django.views.generic.edit import CreateView
#
# from .models import UserProfile
#
#
# class ContactUsView(CreateView):
#     form_class = ContactUsModelForm
#     template_name = 'contact_module/contact_us_page.html'
#     success_url = '/contact-us/'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
#         context['site_setting'] = setting
#
#         return context
#
#
# def store_file(file):
#     with open('temp/image.jpg', "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
#
#
# class CreateProfileView(CreateView):
#     template_name = 'contact_module/create_profile_page.html'
#     model = UserProfile
#     fields = '__all__'
#     success_url = '/contact-us/create-profile'
#
#
# class ProfilesView(ListView):
#     model = UserProfile
#     template_name = 'contact_module/profiles_list_page.html'
#     context_object_name = 'profiles'
#
#
#
#


