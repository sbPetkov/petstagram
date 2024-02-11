from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


def index(request):
    pet_name_pattern = request.GET.get('pet_name_pattern', None)

    photos = Photo.objects.all()

    if pet_name_pattern:
        photos = photos.filter(pets__name__icontains=pet_name_pattern)

    context = {
        'pet_photos': photos,
        'pet_name_pattern': pet_name_pattern
    }

    return render(request, 'common/home-page.html', context)


def like_pet_photo(request, pk):
    # pet_photo = PhotoLike.objects.get(pk=pk, user=request.user)
    pet_photo = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo:
        pet_photo.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{pk}')





