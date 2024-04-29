# SRP: No primeiro exemplo, a responsabilidade de enviar notificações por email foi separada em uma classe NotificacaoService, enquanto no segundo exemplo essa responsabilidade foi misturada dentro da classe PedidoService.
# OCP: No primeiro exemplo, a classe PedidoService é flexível para aceitar diferentes implementações de notificação, enquanto no segundo exemplo a funcionalidade de notificação por email está diretamente incorporada na classe PedidoService, tornando-a menos flexível para extensão.
# DIP: No primeiro exemplo, a classe PedidoService depende de uma abstração NotificacaoService, permitindo diferentes implementações de notificação, enquanto no segundo exemplo há uma dependência direta para enviar notificações por email.
# LSP: Ambos os exemplos não têm subclasses específicas, mas ao seguir o primeiro exemplo, se houver subclasses (por exemplo, PizzaPedido e MarmitaPedido), elas devem implementar a interface Pedido de forma consistente para garantir o comportamento esperado.

# Classe para representar um pedido genérico
class Pedido:
    def processar(self):
        pass

# Classe de serviço para processar pedidos
class PedidoService:
    def processar_pedido(self, pedido: Pedido):
        # Lógica para processar o pedido...
        pedido.processar()

        # Envio de notificação por email após o processamento do pedido
        self.enviar_email_notificacao("Pedido processado com sucesso!")

    def enviar_email_notificacao(self, mensagem):
        # Lógica para enviar notificação por email...
        pass
