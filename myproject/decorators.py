from django.shortcuts import redirect
from django_otp.plugins.otp_totp.models import TOTPDevice


def otp_rec_required(original_function):
    def wrapper_function(*args, **kwargs): 
        try:
           
            user_totp = TOTPDevice.objects.get(user_id=args[0].user.id)
        except:
            return redirect('/account/two_factor/setup/')
        
        user_device = args[0]
    
        user_device = args[0].user.staticdevice_set.get_or_create(name='backup')[0]

        if user_device.token_set.count() == 9:
            return redirect('/account/two_factor/disable/')
        elif user_device.token_set.count() == 0:
            return redirect('/account/two_factor/backup/tokens/')
        return original_function(*args, **kwargs)
    return wrapper_function