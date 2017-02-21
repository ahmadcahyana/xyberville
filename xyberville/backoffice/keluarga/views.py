from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from xyberville.apps.users.decorators import super_user_required
from xyberville.apps.keluarga.models import Keluarga
from xyberville.apps.logs.models import KeluargaLogs
from .forms import KeluargaCreationForm, KeluargaEditForm


@super_user_required
def index(request):
    keluarga_ = Keluarga.objects.all()
    context_data = {
        'keluarga_': keluarga_,
        'title': 'Keluarga',
        'page': 'keluarga',
        'sub_page': 'keluarga_index',
    }

    return render(request, 'backoffice/keluarga/index.html', context_data)


def add(request):
    form = KeluargaCreationForm(data=request.POST or None)
    if form.is_valid():
        form.save(employee=request.user)

        messages.success(request, 'Keluarga baru sudah ditambakan')
        return redirect('backoffice:users:index')

    context_data = {
        'form': form,
        'title': 'Tambah Keluarga',
        'page': 'keluarga',
        'sub_page': 'keluarga_add'
    }
    return render(request, 'backoffice/forms.html', context_data)


@super_user_required
def details(request, id):
    keluarga = get_object_or_404(Keluarga, id=id)
    try:
        profiles = keluarga.kepala_keluarga.profile.keluarga.daftar_keluarga()
    except AttributeError:
        profiles = None

    context_data = {
        'keluarga': keluarga,
        'profiles': profiles,
        'page': 'keluarga',
        'sub_page': 'keluarga_detail'
    }
    return render(request, 'backoffice/keluarga/detail.html', context_data)


@super_user_required
def edit(request, id):
    keluarga = get_object_or_404(Keluarga, id=id)
    initial = {
        'nomor_kk': keluarga.nomor_kk,
        'kepala_keluarga': keluarga.kepala_keluarga,
        'alamat': keluarga.alamat,
        'rt': keluarga.rt,
        'rw': keluarga.rw,
        'telepon': keluarga.telepon,
        'mobile': keluarga.mobile,
        'province': keluarga.province,
        'regency': keluarga.regency,
        'district': keluarga.district,
        'village': keluarga.village
    }

    form = KeluargaEditForm(
        data=request.POST or None,
        instance=keluarga,
        initial=initial
    )

    if form.is_valid():
        form.save()
        KeluargaLogs.objects.create(
            user=request.user,
            keluarga=keluarga,
            action=KeluargaLogs.ACTION.edited
        )
        messages.success(request, 'Detail Keluarga berhasil di ubah')
        return redirect('backoffice:keluarga:index')

    context_data = {
        'form': form,
        'title': 'Edit Keluarga',
        'page': 'keluarga',
        'sub_page': 'keluarga_edit',
    }
    return render(request, 'backoffice/forms.html', context_data)

