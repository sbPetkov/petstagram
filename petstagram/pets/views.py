from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.pets.forms import PetForm, PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class PetCreateView(CreateView):
    # model = Pet
    # fields = ('name', 'date_of_birth', 'pet_photo')
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': 'Svilen',
            'pet_slug': self.object.slug
        })


# def add_pet(request):
#     form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             created_pet = form.save()
#             return redirect('details pet', username='Svilen', pet_slug=created_pet.slug)
#
#     context = {
#         'pet': form
#     }
#     return render(request, 'pets/pet-add-page.html', context)


class PetDetailView(DetailView):
    model = Pet   # object or pet in the template
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = "pet_slug"

# def details_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     context = {
#         "pet": pet
#     }
#     return render(request, 'pets/pet-details-page.html', context)


class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'Svilen'
        return context

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug,
        })


# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()
#     form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('details pet', username=username, pet_slug=pet_slug)
#
#     context = {
#         'form': form,
#         'username': username,
#         'pet': pet
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse('index')

    extra_context = {
        'username': 'Svilen',
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    # or this code to get data in the delete form
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     form = self.form_class(instance=self.object)
    #     context['form'] = form
    #
    #     return context

# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     pet_form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         pet_form.save()
#         return redirect('index')
#
#     context = {
#         'pet_form': pet_form,
#         'username': username,
#         'pet': pet
#     }
#     return render(request, 'pets/pet-delete-page.html', context)
