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




### Exemplo 2: Processamento de Pedidos em Django com Aplicação dos Princípios SOLID

**Cenário:**
Um sistema Django que processa pedidos de diferentes tipos, como pedidos de pizza e marmitas. A classe PedidoService é responsável por receber o pedido, validar os dados e enviar para a cozinha.

**Análise dos Problemas:**

**SRP (Princípio da Responsabilidade Única):**
A classe `PedidoService` viola o SRP ao assumir responsabilidades que não estão diretamente relacionadas ao processamento de pedidos, como o envio de notificações por email. Isso dificulta a compreensão e manutenção do código.

**OCP (Princípio Aberto-Fechado):**
A classe `PedidoService` está fechada para modificação, o que significa que adicionar novos tipos de pedidos exigiria alterar o código existente. Isso torna o código menos flexível e dificulta a extensão.

**DIP (Princípio da Inversão de Dependência):**
A classe `PedidoService` depende diretamente da classe `EmailService` para enviar notificações, o que a torna menos flexível e mais acoplada a uma implementação específica.

**LSP (Princípio da Substituição de Liskov):**
A classe `PedidoService` não segue o LSP, pois substituir um objeto `Pedido` por um objeto `PedidoUrgente` pode resultar em comportamentos inesperados, como a não consideração do tempo de espera para o preparo do pedido.

**Solução com Aplicação dos Princípios SOLID:**

Para resolver esses problemas e aplicar os princípios SOLID, podemos adotar as seguintes medidas:

1. **SRP (Princípio da Responsabilidade Única):**
   - Divida a responsabilidade da classe `PedidoService` em classes menores e mais focadas, como `PedidoService` para a lógica principal de processamento de pedidos e `NotificacaoService` para enviar notificações por email, SMS ou outro canal.

2. **OCP (Princípio Aberto-Fechado):**
   - Utilize interfaces para definir o comportamento das classes de pedido, permitindo a adição de novos tipos de pedidos sem modificar o código original. Por exemplo, `IPedido`.

3. **DIP (Princípio da Inversão de Dependência):**
   - Aplique a injeção de dependência para fornecer as dependências necessárias às classes, tornando o código mais flexível e desacoplado. Por exemplo, o `PedidoService` pode receber o `NotificacaoService` como parâmetro no construtor.

4. **LSP (Princípio da Substituição de Liskov):**
   - Garanta que as subclasses de pedido (como `PizzaPedido` e `MarmitaPedido`) implementem a interface `IPedido` de forma consistente, respeitando o comportamento esperado da superclasse.

