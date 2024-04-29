# Neste exemplo, aplicamos os princípios SOLID da seguinte forma:

# SRP: Dividimos as responsabilidades em classes separadas: UsuarioService para operações de criação, UsuarioRepository para operações de busca e UsuarioProfileService para operações de atualização de perfil.
# OCP: Utilizamos interfaces implícitas do Python, permitindo que novas funcionalidades sejam adicionadas sem modificar o código existente.
# DIP: Não há dependência direta da classe Usuario do Django; em vez disso, utilizamos o serviço de usuário do Django (User) de forma abstraída.
# LSP: As subclasses (neste caso, não há explicitamente subclasses) podem ser substituídas pela classe base User do Django sem impactar o comportamento esperado.

from django.contrib.auth.models import User

# Classe responsável por operações relacionadas à criação de usuários
class UsuarioService:
    def criar_usuario(self, username, email, password):
        return User.objects.create_user(username, email, password)

# Classe responsável por operações relacionadas à busca de usuários
class UsuarioRepository:
    def buscar_usuario_por_id(self, user_id):
        return User.objects.get(id=user_id)

# Classe responsável por operações relacionadas à atualização de perfil de usuários
class UsuarioProfileService:
    def atualizar_perfil(self, user, new_data):
        user.first_name = new_data.get('first_name', user.first_name)
        user.last_name = new_data.get('last_name', user.last_name)
        user.email = new_data.get('email', user.email)
        user.save()
 

