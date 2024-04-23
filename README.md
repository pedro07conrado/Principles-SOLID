# Disciplina BCC3004 - Engenharia de Software
## Universidade Tecnológica Federal do Paraná
### Campus Campo Mourão

Este guia aborda os 4 princípios do SOLID aplicados à linguagem de programação utilizando o framework Django. Você encontrará exemplos práticos de como o SRP (Princípio da Responsabilidade Única), OCP (Princípio Aberto-Fechado), DIP (Princípio da Inversão de Dependência) e LSP (Princípio da Substituição de Liskov) podem ser aplicados para construir um código modular e fácil de manter.

## Exemplos

### Exemplo 1: Gerenciamento de Usuários

**Cenário:**
Em um sistema Django responsável pelo gerenciamento de **usuários**, a classe `Usuario` é encarregada de operações como criação, edição, exclusão, autenticação e recuperação de informações de perfil.

**Análise:**

**SRP (Princípio da Responsabilidade Única)**
A classe `Usuario` viola o SRP ao assumir múltiplas responsabilidades relacionadas ao gerenciamento de usuários, dificultando a compreensão, teste e manutenção do código.

**OCP (Princípio Aberto-Fechado)**
A classe `Usuario` é fechada para modificação, o que significa que a adição de novas funcionalidades, como recuperar histórico de logins, exigiria modificar o código existente.

**DIP (Princípio da Inversão de Dependência)**
A classe `Usuario` possui uma dependência direta da classe `User` do Django para operações de banco de dados, resultando em um código menos flexível e fortemente acoplado a uma implementação específica.

**LSP (Princípio da Substituição de Liskov)**
A classe `Usuario` não segue o LSP, pois a substituição por um objeto `SuperUsuario` pode levar a falhas em funcionalidades como edição de perfil.

**Solução:**

**SRP:** Dividir a classe `Usuario` em classes mais específicas e focadas, como `UsuarioService`, `UsuarioRepository` e `UsuarioProfileService`, cada uma com uma única responsabilidade bem definida.

**OCP:** Utilizar interfaces para definir comportamentos das classes, permitindo a adição de novas funcionalidades por meio de implementações de interfaces sem modificar o código original.

**DIP:** Aplicar injeção de dependência para prover as dependências necessárias às classes, tornando o código mais flexível e desacoplado.

**LSP:** Garantir que subclasses implementem os métodos da superclasse de forma consistente, sem introduzir comportamentos inesperados.
