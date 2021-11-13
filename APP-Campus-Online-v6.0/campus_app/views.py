from django.urls import reverse_lazy
from .models import Imagem, Noticia, TextoMateria, Video, WhatsAppAccount
from django.contrib.auth.models import Group
from .forms import NoticiaForm, WhatsAppAccountCreateForm, TextoMateriaForm, VideoForm, ImagemForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.dates import DayArchiveView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import datetime

def ShowNoticiaLongForm(request, pk):
    
    noticia = Noticia.objects.get(id = pk)
    imagem = Imagem.objects.get(noticia_id = pk)
    video = Video.objects.get(noticia_id = pk)
    texto_materia = TextoMateria.objects.get(noticia_id = pk)
    context = {
        'noticia': noticia,
        'imagem': imagem,
        'video': video,
        'texto_materia': texto_materia
    }
    return render(request, 'show_noticia_long_form.html', context)

class HomeView(TemplateView):

    template_name = "campus_app/home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')[:20]
        context['data'] = datetime.date.today()
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


class NoticiaDataView(DayArchiveView):

    template_name = "campus_app/noticia_archive_day.html"
    date_field = "dia_publicacao"
    queryset = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')
    allow_future = True
    allow_empty = True

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        queryset = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')
        context['noticias'] = queryset
        context['data'] = datetime.date(self.get_year(), self.get_month(), self.get_day())
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


class NoticiaView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):

    permission_required = 'campus_app.view_noticia'
    template_name = "campus_app/noticia_list.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-data_publicacao').all
        context['perfil'] = Group.objects.filter(user = self.request.user)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

      
class NoticiaCreate(LoginRequiredMixin, PermissionRequiredMixin, FormView):

    permission_required = 'campus_app.add_noticia'
    template_name = 'campus_app/noticia_form.html'
    form_class = NoticiaForm
    success_url = reverse_lazy('noticia_list')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@login_required
def NoticiaCreateLongForm(request):

    if request.method == 'POST':
        noticia_form = NoticiaForm(request.POST)

        if noticia_form.is_valid():
            noticia_form.save()
            return redirect('noticia_list')        

        else:
            context = {
                'noticia_form': noticia_form,
            }

    else:
        context = {
            'noticia_form': NoticiaForm(),
        }

    return render(request, 'campus_app/noticia_create_long_form.html', context)

@login_required
def TextoCreateLongForm(request):

    if request.method == 'POST':
        TextoMateria_form = TextoMateriaForm(request.POST)

        if TextoMateria_form.is_valid():
            TextoMateria_form.save()
            return redirect('noticia_list')        

        else:
            context = {
                'TextoMateria_form': TextoMateria_form
            }
            return render(request, 'campus_app/texto_create_long_form.html', context)
    else:
        context = {
            'TextoMateria_form': TextoMateriaForm()
        }
        return render(request, 'campus_app/texto_create_long_form.html', context)

@login_required
def ImagemCreateLongForm(request):
    
    if request.method == 'POST':
        imagem_form = ImagemForm(request.POST)

        if imagem_form.is_valid():
            imagem_form.save()
            return redirect('noticia_list')        

        else:
            context = {
                'imagem_form': imagem_form
            }
            return render(request, 'campus_app/imagem_create_long_form.html', context)
    else:
        context = {
            'imagem_form': ImagemForm()
        }
        return render(request, 'campus_app/imagem_create_long_form.html', context)

@login_required
def VideoCreateLongForm(request):
    
    if request.method == 'POST':
        video_form = VideoForm(request.POST)

        if video_form.is_valid():
            video_form.save()
            return redirect('noticia_list')        

        else:
            context = {
                'video_form': video_form
            }
            return render(request, 'campus_app/video_create_long_form.html', context)
    else:
        context = {
            'video_form': VideoForm()
        }
        return render(request, 'campus_app/video_create_long_form.html', context)


class NoticiaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'campus_app.change_noticia'
    model = Noticia
    form_class = NoticiaForm
    success_url = reverse_lazy('noticia_list')
    template_name = 'campus_app/noticia_update_form.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

@login_required
def NoticiaUpdateLongForm(request, pk):
    
    noticia = get_object_or_404(Noticia, id = pk)

    noticia_form = NoticiaForm(instance=noticia)

    if(request.method == 'POST'):
        noticia_form = NoticiaForm(request.POST, instance=noticia)
        
        if(noticia_form.is_valid()):
            noticia = noticia_form.save(commit=False)
            noticia.titulo = noticia_form.cleaned_data['titulo']
            noticia.resumo = noticia_form.cleaned_data['texto']
            noticia.prioridade = noticia_form.cleaned_data['prioridade']
            noticia.link_foto = noticia_form.cleaned_data['link_foto']
            noticia.autoria_midia = noticia_form.cleaned_data['autoria_midia']
            noticia.link_video = noticia_form.cleaned_data['link_video']
            noticia.save()

            return redirect('noticia_list')
        else:
            context = {
                'noticia_form': noticia_form
            }
            return render(request, 'campus_app/noticia_update_long_form.html', context)
    elif(request.method == 'GET'):
        context = {
            'noticia_form': noticia_form
        }
        return render(request, 'campus_app/noticia_update_long_form.html', context)

@login_required
def ImagemUpdateLongForm(request, pk):
    imagem = get_object_or_404(Imagem, id = pk)
    imagem_form = ImagemForm(instance=imagem)
    if(request.method == 'POST'):
        imagem_form = ImagemForm(request.POST, instance=imagem)
        if(imagem_form.is_valid()):
            imagem = imagem_form.save(commit=False)
            imagem.link_foto_long_form = imagem_form.cleaned_data['link_foto_long_form']
            imagem.autoria_midia_imagem = imagem_form.cleaned_data['autoria_midia_imagem']
            imagem.save()
        else:
            context = {
                'imagem_form': imagem_form
            }
            return render(request, 'campus_app/imagem_update_long_form.html', context)
    elif(request.method == 'GET'):
        context = {
            'imagem_form': imagem_form
        }
        return render(request, 'campus_app/imagem_update_long_form.html', context)

@login_required
def VideoUpdateLongForm(request, pk):
    video = get_object_or_404(Video, id = pk)
    video_form = VideoForm(instance=video)
    if(request.method == 'POST'):
        video_form = VideoForm(request.POST, instance=video)
        if(video_form.is_valid()):
            video = video_form.save(commit=False)
            video.link_video_long_form = video_form.cleaned_data['link_video_long_form']
            video.autoria_midia_video = video_form.cleaned_data['autoria_midia_video']
            video.save()
        else:
            context = {
                'video_form': video_form
            }
            return render(request, 'campus_app/video_update_long_form.html', context)
    elif(request.method == 'GET'):
        context = {
            'video_form': video_form
        }
        return render(request, 'campus_app/video_update_long_form.html', context)

@login_required
def TextoUpdateLongForm(request, pk):
    texto = get_object_or_404(TextoMateria, id = pk)
    texto_form = TextoMateriaForm(instance=texto)
    if(request.method == 'POST'):
        texto_form = TextoMateriaForm(request.POST, instance=texto)
        if(texto_form.is_valid()):
            texto = texto_form.save(commit=False)
            texto.subtitulo = texto_form.cleaned_data['subtitulo']
            texto.texto_materia = texto_form.cleaned_data['texto_materia']
            texto.save()
        else:
            context = {
                'texto_form': texto_form
            }
            return render(request, 'campus_app/texto_update_long_form.html', context)
    elif(request.method == 'GET'):
        context = {
            'texto_form': texto_form
        }
        return render(request, 'campus_app/texto_update_long_form.html', context)


class NoticiaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    
    permission_required = 'campus_app.delete_noticia'
    model = Noticia
    success_url = reverse_lazy('noticia_list')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

#@login_required
#def NoticiaDeleteLongForm(request, pk):
    #noticia = Noticia.objects.get(id = pk)
    #noticia.delete()
    #imagem = Imagem.objects.get(noticia_id = pk)
    #imagem.delete()
    #video = Video.objects.get(noticia_id = pk)
    #video.delete()
    #texto_materia = TextoMateria.objects.get(noticia_id = pk)
    #texto_materia.delete()
    #return redirect('noticia_list')

###################################### WhatsApp Account Views ######################################


class WhatsAppAccountView(TemplateView):

    template_name = "campus_app/whatsapp_account_list.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['whatsapp_accounts'] = WhatsAppAccount.objects.all()
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


class WhatsAppAccountCreate(FormView):

    model = WhatsAppAccount
    template_name = 'campus_app/whatsapp_account_create_form.html'
    form_class = WhatsAppAccountCreateForm
    success_url = reverse_lazy('whatsapp_account_list')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

        context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

    def form_valid(self, form):

        form.save()

        return super().form_valid(form)
        

class WhatsAppAccountUpdate(UpdateView):
    
    model = WhatsAppAccount
    form_class = WhatsAppAccountCreateForm
    success_url = reverse_lazy('whatsapp_account_list')
    template_name = 'campus_app/whatsapp_account_update_form.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'
    
        return context

    def form_valid(self, form):
        
        form.save()

        return super().form_valid(form)


class WhatsAppAccountDelete(DeleteView):

    model = WhatsAppAccount
    success_url = reverse_lazy('whatsapp_account_list')
    template_name = 'campus_app/whatsapp_account_delete_confirmation.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

