from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse
from django.db import transaction
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def delete_user_list(self, request, pk=None):
        # Obtiene el payload del ususario
        user_list = request.data
        # Declaracion de variables
        deleted_users = []
        # Crea un punto de restaura por si existe algun error durante el procesado
        rollback_point = transaction.savepoint()
        try:
            # Inicializa un proceso de transacciones
            with transaction.atomic():
                # Ejecuta las eliminaciones
                for user in user_list:
                    deleted_users.append({
                        'username': user['username']
                    })
                    User.objects.filter(pk=user['id']).delete()
            return JsonResponse(
                {"status": 200, "message": "Transaccion completada con éxito.", "deleted_users": deleted_users},
                safe=False)
        except:
            # Si existe algun error en el proceso se ejecuta un RollBack al punto de inicio
            transaction.savepoint_rollback(rollback_point)
            return JsonResponse({"status": 500, "message": "Ha ocurrido un error en el servidor."}, safe=False)

    # Metodo para actualizar password
    @action(detail=False, methods=['post'])
    def update_password(self, request, pk=None):
        # Obtiene el payload del ususario
        user = request.data
        # Valida si se enviaron datos
        if user is None:
            return JsonResponse({"status": 500, "message": "Error. No se enviaron datos."}, safe=False)
        # Si se enviaron los datos, verifica:
        else:
            # Primero: si llegaron los 2 passwords
            if ((user['password']) and (user['password2']) and (user['password']!='') and (user['password2']!='')):
                # Segundo: si los 2 passwords son iguales
                if ((user['password']) != (user['password2'])):
                    return JsonResponse({"status": 500, "message": "Error. Las contraseñas no coinciden."}, safe=False)
                else:
                    # Update: ejecuta la actualizacion del password
                    try:
                        # Busca el usuario que viene en el data para verificar si el usuario existe
                        filtered_user = User.objects.filter(pk=user['id']).get()
                        # Le asigna al usuario el password que envio en el request
                        filtered_user.set_password(user['password'])
                        # Guarda los cambios en la base de datos
                        filtered_user.save()
                        return JsonResponse({"status": 200, "message": "Contraseña actualizada correctamente."}, safe=False)
                    except:
                        return JsonResponse({"status": 500, "message": "Error. El usuario no existe."}, safe=False)
            else:
                return JsonResponse({"status": 500, "message": "Error. No se permiten contraseñas vacías."}, safe=False)
        return HttpResponse()

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
