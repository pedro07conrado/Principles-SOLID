# Neste exemplo, a classe Usuario viola os princípios SOLID:

# SRP: A classe Usuario possui múltiplas responsabilidades, incluindo criação, busca e atualização de perfil de usuário.
# OCP: A classe Usuario está fechada para modificação, tornando difícil estender ou adicionar novas funcionalidades sem modificar o código existente.
# DIP: A classe Usuario possui uma dependência direta da classe User do Django, tornando o código menos flexível e fortemente acoplado.
# LSP: Não é garantido que a substituição da classe Usuario por uma subclasse possa ser feita sem afetar o comportamento do código. Por exemplo, se a subclasse não implementar o método atualizar_perfil, o comportamento esperado será comprometido.

from django.contrib.auth.models import User

# Classe que viola os princípios SOLID
class Usuario:
    # Método para criar um usuário
    def criar_usuario(self, username, email, password):
        return User.objects.create_user(username, email, password)
    
    # Método para buscar um usuário por ID
    def buscar_usuario_por_id(self, user_id):
        return User.objects.get(id=user_id)
    
    # Método para atualizar o perfil de um usuário
    def atualizar_perfil(self, user, new_data):
        user.first_name = new_data.get('first_name', user.first_name)
        user.last_name = new_data.get('last_name', user.last_name)
        user.email = new_data.get('email', user.email)
        user.save()
