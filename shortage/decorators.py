from django.shortcuts import redirect
from django.http import HttpResponse

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func (request, *args, **kwargs):
            group=None 
            #Traitement SSO here
            print(request.user)
            if request.user.groups.exists():#test if user exists in groups
                # print(request.user)
                group=request.user.groups.all()[0].name#rutern name of user
                if group in allowed_roles:
                    return view_func (request, *args, **kwargs)
                else:
                    return HttpResponse('you are not autrozied to view page')
        return wrapper_func
    return decorator

