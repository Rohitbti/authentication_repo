from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,FormView
from .forms import MyPasswordResetForm, MyUserCreationForm
from django.urls import reverse_lazy
from .forms import LoginForm, MyPasswordChangeForm,MyPasswordResetForm,SetPasswordForm
from django.contrib.auth import authenticate, get_user_model,login,logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import MyUser
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from authentication.EmailBackEnd import EmailBackEnd
from django.contrib.auth import update_session_auth_hash
from django.utils.safestring import mark_safe

class signup_view(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password1')
            )
            new_user.save()
            form = MyUserCreationForm()
            messages.success(request,"Registration done you can sign in now.")
            return redirect("/login",{'form':form})
    else:
        form = MyUserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'register.html', context=context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # user=EmailBackEnd.authenticate(request,username=email, password=password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user'] = user.first_name
                request.session.set_expiry(36000)
                # return redirect("/home",{'username':user})
                return redirect("/home")
            else:
                messages.error(request,'Invailid credentials')
        else:
            messages.error(request,'Error validating the form')
    return render(request,"login2.html",{'form':form})
def home(request):
    return render(request,"home.html")
def logout_user(request):
    logout(request)
    messages.success(request,"Log out Successfully")
    return HttpResponseRedirect("/login")

def change_password_view(request):
    form = MyPasswordChangeForm(request.user)
    if request.method == "POST":
        form = MyPasswordChangeForm( request.user,request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"Password Changed successfully")
            update_session_auth_hash(request, form.user)
            return redirect("/home",{'username':user})
    return render(request,"change_password.html",{'form':form})

def reset_password_view(request):
    if request.method == "POST":
        password_reset_form = MyPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            # data = password_reset_form.cleaned_data['email']
            data = password_reset_form.cleaned_data['username']
            print(data)
            # associated_users = MyUser.objects.filter(Q(email=data))
            associated_users = MyUser.objects.filter(Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "reset_Email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
            else:
                messages.error(request,'This User not exist')
        else:
            messages.error(request,'Validation failed')
    password_reset_form = MyPasswordResetForm()
    return render(request=request, template_name="reset_password.html", context={"form":password_reset_form})

class PasswordResetConfirmView(FormView):
    template_name = "reset_password_confirm.html"
    success_url = '/login'
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        UserModel = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
            print(user)
        except (TypeError, ValueError, OverflowError,UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password= form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, mark_safe('Password has been reset.<br/>You can sign in now with new password'))
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been successfull.')
                return self.form_invalid(form)
        else:
            messages.error(request,'The reset password link is no longevalid.')
            return self.form_invalid(form)