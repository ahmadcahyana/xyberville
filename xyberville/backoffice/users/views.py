
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from xyberville.apps.users.decorators import super_user_required
from xyberville.apps.users.models import User
from xyberville.apps.logs.models import UserLogs
from xyberville.apps.profiles.models import Profile
from .forms import WargaCreationForm, WargaEditForm, WargaFilterForm


@super_user_required
def index(request):
    users = User.objects.all().select_related('profile')
    form = WargaFilterForm(data=request.POST or None)
    context_data = {
        'users': users,
        'form': form,
        'title': 'Users',
        'page': 'users',
        'sub_page': 'users_index',
    }

    return render(request, 'backoffice/users/index.html', context_data)


@super_user_required
def detail(request, id):
    user = get_object_or_404(User, id=id)
    try:
        profiles = user.profile.keluarga.daftar_keluarga()
    except AttributeError:
        profiles = None

    context_data = {
        'user': user,
        'profiles': profiles,
        'title': user.name,
        'page': 'users',
        'sub_page': 'user_detail'
    }
    return render(request, 'backoffice/users/detail.html', context_data)


@super_user_required
def add(request):
    form = WargaCreationForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save(employee=request.user)

        messages.success(request, 'User has been added')
        return redirect('backoffice:users:index')

    context_data = {
        'form': form,
        'title': 'Tambah Warga',
        'page': 'users',
        'sub_page' : 'users_add'
    }
    return render(request, 'backoffice/forms.html', context_data)


@super_user_required
def edit(request, id):
    user = get_object_or_404(User, id=id)
    initial = {
        'username': user.username,
        'nik': user.profile.nik,
        'alamat': user.profile.alamat,
        'rt': user.profile.rt,
        'rw': user.profile.rw,
        'province': user.profile.province,
        'regency': user.profile.regency,
        'district': user.profile.district,
        'village': user.profile.village,
        'kode_pos': user.profile.kode_pos,
        'kewarganegaraan': user.profile.kewarganegaraan,
        'wna': user.profile.wna,
        'paspor': user.profile.paspor,
        'paspor_kadaluarsa ': user.profile.paspor_kadaluarsa,
        'kelamin': user.profile.kelamin,
        'tempat_lahir': user.profile.tempat_lahir,
        'tanggal_lahir': user.profile.tanggal_lahir,
        'nomor_akta_lahir': user.profile.nomor_akta_lahir,
        'golongan_darah': user.profile.golongan_darah,
        'agama': user.profile.agama,
        'status_pernikahan': user.profile.status_pernikahan,
        'nomor_akta_nikah': user.profile.nomor_akta_nikah,
        'tanggal_pernikahan': user.profile.tanggal_pernikahan,
        'nomor_akta_cerai': user.profile.nomor_akta_cerai,
        'tanggal_perceraian': user.profile.tanggal_perceraian,
        'hubungan_keluarga': user.profile.hubungan_keluarga,
        'penyandang_cacat': user.profile.penyandang_cacat,
        'ibu': user.profile.ibu,
        'ayah': user.profile.ayah,
        'pendidikan': user.profile.pendidikan,
        'pekerjaan': user.profile.pekerjaan,
        'telepon': user.profile.telepon,
        'mobile': user.profile.mobile,
        'keluarga': user.profile.keluarga,
        'status_penduduk': user.profile.status_penduduk,
        'status_tempat_tinggal': user.profile.status_tempat_tinggal,
        'photo': user.profile.photo
    }

    form = WargaEditForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=user,
        initial=initial
    )

    if form.is_valid():
        form.save()
        UserLogs.objects.create(
            user=request.user,
            user_edited=user,
            action=UserLogs.ACTION.edited
        )
        messages.success(request, 'Detail warga berhasil di ubah')
        return redirect('backoffice:users:index')

    context_data = {
        'form': form,
        'title': 'Edit Customer',
        'photo': user.profile.photo if user.profile.photo else None,
        'page': 'users',
        'sub_page': 'user_edit',
    }
    return render(request, 'backoffice/forms.html', context_data)
