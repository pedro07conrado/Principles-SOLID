Disciplina BCC3004 (Engenharia de Software) do Curso de Bacharelado em Ciência da Computação, da Universidade Tecnológica Federal do Paraná, Campus Campo Mourão. Explicação dos 4 princípios do SOLID para uma linguagem de programação.
Neste guia,vamos analisar SRP (Single Responsibility Principle), OCP (Open-Closed Principle), DIP (Dependency Inversion Principle) e LSP (Liskov Substitution Principle) na prática, ultilizando Django. Com isses principios SOLID em Djnago, demonstrando como esses principios podem ser ultilizados para construir um código modular e fácil de manter. 

**EXEMPLOS**


**EXEMPLO 1:Gerenciamento de Usuários**

**Cenário:**
Um sistema Django que gerencia **usuários**. A classe ´´Usuario´´ possui métodos para criar, editar e excluir usuários, além de métodos para autenticar e recuperar informações do perfil.

**Análise:**

**SRP (Single Responsibility Principle - Princípio da Responsabilidade Única)**
A classe ´´Usuario´´ viola o SRP ao ter diversas responsabilidades relacionadas ao gerenciamento de usuários. Isso torna o código mais difícil de entender, testar e manter.

**OCP (Open/Closed Principle - Princípio Aberto-Fechado)**
A classe ´´Usuario´´ é fechada para modificação, pois adicionar novas funcionalidades, como recuperar o histórico de logins, exigiria modificar o código existente.

**DIP (Dependency Inversion Principle - Princípio da Inversão de Dependência)**
A classe ´´Usuario´´ depende diretamente da classe ´´User´´ do Django para realizar operações no banco de dados. Isso torna o código menos flexível e acoplado a uma implementação específica.

**LSP (Liskov Substitution Principle - Princípio da Substituição de Liskov)**
A classe ´´Usuario´´ não segue o LSP, pois se você substituir um objeto ´´Usuario´´ por um objeto ´´SuperUsuario´´, algumas funcionalidades, como editar o perfil, podem não funcionar corretamente.

**Solução:**

**SRP:** Dividir a classe 'Usuario' em classes menores e mais focadas, como ´´UsuarioService´, ´´UsuarioRepository´´ e ´´UsuarioProfileService´´. Cada classe terá uma única responsabilidade bem definida.

**OCP:** Utilizar interfaces para definir o comportamento das classes. Dessa forma, novas funcionalidades podem ser adicionadas através de classes que implementam as interfaces existentes, sem modificar o código original.

**DIP:** Utilizar injeção de dependência para fornecer as dependências necessárias para as classes. Isso torna o código mais flexível e desacoplado.

**LSP:** Garantir que as subclasses implementem os métodos da superclasse de forma consistente e que não introduzam comportamentos inesperados







