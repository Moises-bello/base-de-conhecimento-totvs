---
content_hash: 9cdf5d26f7f1ea12c27ec7b32a1ff6d49c78958890489463820febe25fa2feb8
fetched_at: '2026-06-29T00:09:12.732445+00:00'
page_id: '417700481'
product: rm
source: tdn-rm
title: Fechamento de Consumo
type: documentation
url: https://tdn.totvs.com/display/LRM/Fechamento+de+Consumo
version: 1
---

**Fechamento de Consumo**   
Este processo carrega todos os pedidos de antibiótico do período. Todos os itens de pedidos em estado 1 (cabeçalho validado):  
Caso já esteja fechado (data fim e dose informados), não tem nada a fazer, caso contrário, tenta fechar.  
Se não tiver dispensações, não tem como fechar, caso contrário, processa as dispensações.  
Se a última dispensação for mais recente que 8 dias antes da data atual, o item não é fechado.  
Se tiver dispensação sem dose ou sem via informadas, não tem como fechar, caso contrário fecha o item com a data da última dispensação e com a somatória das doses, dividindo porvia de administração.  
Se conseguir fechar todos os itens do pedido, o pedido passa para o estado 2 (pendente de validar o fechamento de consumo).  
Se a soma das doses das dispensações der menos de zero, o item não é fechado.  
Se a soma das doses das dispensações der igual à zero, o item é excluído. Caso todos os itens sejam excluídos, o pedido também será.  
   
Descrições dos status.  
   
Quantidade de pedidos carregados com status 1:  (pedido importado);  
Quantidade de pedidos carregados com status 2:  (após a 1a validação na tela de Pedido de ATB);  
Quantidade de pedidos carregados com status 3:  (após realizar o processo de fechamento de consumo e o status anterior era 2);  
Quantidade de pedidos carregados com status 4:  (caso o usuário informe a data  final e a dose na tela de dispensações, ao salvar o pedido);
