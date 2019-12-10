from django.contrib.auth.views import (PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import _UserCreationForm, _UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name="accounts/dashboard.html"
    login_url = 'login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = Group.objects.filter(user = self.request.user)
        return context

class _PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name='accounts/edit_password.html'
    form_class = PasswordChangeForm
    success_url = 'senha-alterada-com-sucesso' 

class _PasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name='accounts/password_change_done.html'

class _PasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = PasswordResetForm
    email_template_name = 'accounts/password_reset_mail.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = 'nova-senha-solicitada'

class _PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class _PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = 'senha-redefinida-com-sucesso'

class _PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

class CreateUser(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    template_name = 'accounts/user_form.html'
    permission_required = 'auth.add_user'
    form_class = _UserCreationForm
    success_url = 'usuario-inserido-com-sucesso'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserCreated(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'accounts/user_create_done.html'
    permission_required = 'auth.add_user'

@login_required
def UpdateUser(request, pk):
    if not request.user.has_perm('auth.change_user'):
        raise PermissionDenied
    data = {}
    user = User.objects.get(pk=pk)
    if User.objects.filter(pk=pk, is_superuser=True):
       raise PermissionDenied
    form = _UserChangeForm(request.POST or None, instance=user) 
    if form.is_valid(): 
        form.save() 
        return redirect('users')
    data['form'] = form
    data['user'] = user
    return render(request, 'accounts/user_form.html', data)

class UsersView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'accounts/users.html'
    permission_required = 'auth.view_user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

