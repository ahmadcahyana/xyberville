from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from xyberville.apps.users.printing import MyPrint
from xyberville.apps.users.decorators import super_user_required
from xyberville.apps.arsip.models import Pengantar
from .forms import PengantarCreationForm


@super_user_required
def index(request):
    pengantar = Pengantar.objects.all()
    context_data = {
        'pengantar': pengantar,
        'title': 'Pengantar',
        'page': 'pengantar',
        'sub_page': 'pengantar_index',
    }

    return render(request, 'backoffice/pengantar/index.html', context_data)


def print_surat_pengantar(request, id):
    pengantar = get_object_or_404(Pengantar, id=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pengantar.pdf"'

    buffer = BytesIO()

    report = MyPrint(buffer, 'Letter')
    pdf = report.print_pengantar(pengantar)

    response.write(pdf)
    return response


@super_user_required
def add(request):
    form = PengantarCreationForm(data=request.POST or None)
    if form.is_valid():
        form.save()

        messages.success(request, 'Surat Pengantar berhasil di tambahkan')
        return redirect('backoffice:pengantar:print_surat_pengantar')

    context_data = {
        'form': form,
        'title': 'Tambah Warga',
        'page': 'users',
        'sub_page': 'users_add',
        'form_title': 'Surat Pengantar'
    }
    return render(request, 'backoffice/forms.html', context_data)
