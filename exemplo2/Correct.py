# Classe para representar um pedido genérico
class Pedido:
    def processar(self):
        pass

# Interface para notificação
class NotificacaoService:
    def enviar_notificacao(self, mensagem):
        pass

# Classe de serviço para processar pedidos
class PedidoService:
    def __init__(self, notificacao_service: NotificacaoService):
        self.notificacao_service = notificacao_service

    def processar_pedido(self, pedido: Pedido):
        # Lógica para processar o pedido...
        pedido.processar()

        # Enviar notificação após o processamento do pedido
        self.notificacao_service.enviar_notificacao("Pedido processado com sucesso!")
