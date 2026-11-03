---
content_hash: 712007e7ec53f39f34a29597a9ad58d6da92f5d8d11c25f068b4fa236e8b7567
fetched_at: '2026-06-29T00:09:26.089033+00:00'
page_id: '423938255'
product: rm
source: tdn-rm
title: Cancelamento de Registros (Integração ERP TOTVS X Portal de Compras Paradigma)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938255
version: 3
---

**Objetivo**

Permitir que o usuário cancele ordens de compra no ERP TOTVS (linha RM) que estejam integradas ao Portal de Compras Paradigma (WBC – Web Business Center), exclua itens da cotação ou pedidos integrados, receba os cancelamentos realizados através do Portal de Compras Paradigma (WBC – Web Business Center) e também estorne os itens não recebidos.  
 A execução de qualquer um destes processos por parte do usuário do ERP TOTVS irá refletir nos respectivos pedidos que se encontram no Portal de Compras Paradigma.

**Sobre o processo**

O cancelamento de registros consiste em, quando o usuário cancelar ou concluir um pedido, ou cancelar uma cotação no ERP TOTVS, o item ou o pedido seja excluído no Portal de Compras Paradigma (WBC – Web Business Center).   
A conclusão ou cancelamento do registro pode ser realizada através do menu processos do respectivo movimento ou cotação.  
O código do pedido no ERP TOTVS e no Portal de Compras Paradigma (WBC – Web Business Center) será o mesmo para facilitar o rastreamento e a visualização dos pedidos entre os dois sistemas

**Conclusão do Pedido**

Ao concluir um Item de Movimento no ERP TOTVS, será enviado para o Portal de Compras Paradigma os dados para exclusão do item correspondente. Para realizar a conclusão do pedido é necessário acessar o menu **"Processos | Concluir Pedido"** no movimento gerado.   
 ***Importante!*** Se o pedido possuir mais de um item e um item apenas for concluído, o pedido no Portal não será excluído. Somente será excluído o item que foi concluído, o registro do movimento continuará lá com os outros itens que não foram concluídos.

**Cancelamento de Movimento**

Ao cancelar um movimento no ERP TOTVS, será enviado para o Portal de Compras Paradigma os dados da integração contendo os registros que deverão ser cancelados.   
Para realizar o cancelamento do pedido é necessário acessar o menu "Processos | Cancelamento de Movimento" no movimento gerado.

**Estorno de Item não Recebido**

O Estorno de item não recebido poderá ser executado mesmo que o movimento esteja integrado ao Paradigma. Entretanto não será reaberto os itens da requisição, uma vez que eles não possuem o serviço de reabrir o item da requisição que está vinculado ao item de cotação que será reaberto.  
 No ERP TOTVS, uma vez estornado o item, a cotação será reaberta e em seguida poderá ser excluído o item da cotação, retornando este item para a solicitação de compra. Caso o usuário queira integrar este item novamente, deverá ser criado uma nova solicitação e integrar a mesma ao Portal de Compras Paradigma.

1. Estorno de Item do Pedido: Ao estornar um item de movimento no ERP TOTVS, será enviado para o Portal de Compras Paradigma os dados para exclusão do item correspondente.   
   O EAI\_RM irá preparar os dados para serem enviados para o Portal de Compras Paradigma. Os dados enviados conterão o item de movimento que está sendo estornado e que foi integrado ao Portal de Compras Paradigma fazendo a exclusão do respectivo item do pedido de compra no Portal de Compras Paradigma.
2. Estorno de todos os Itens do Pedido: Ao estornar um movimento no ERP TOTVS, será enviado para o Portal de Compras Paradigma os dados para cancelamento dos itens correspondentes.  
   O EAI\_RM irá preparar os dados para serem enviados para o Portal de Compras Paradigma. Os dados enviados conterão os Itens do Movimento que está sendo estornado e que foram integrados ao Portal de Compras Paradigma fazendo o cancelamento dos respectivos Pedidos de Compra no Portal de Compras Paradigma.

**Cancelamento da Cotação**

Ao cancelar uma cotação no ERP TOTVS, será enviado para o Portal de Compras Paradigma os dados para cancelamento.   
O cancelamento é feito acessando o menu "Processos | Cancelar Cotação".  
O EAI\_RM irá preparar os dados para serem enviados para o Portal de Compras Paradigma. Os dados enviados conterão os Itens da Solicitação de Compras que estão relacionados aos Itens da Cotação que está sendo cancelada e que foram integrados ao Portal de Compras Paradigma fazendo o cancelamento do respectivo Item da Requisição de Compra no Portal de Compras Paradigma.

**Exclusão de Item da Cotação**

Ao excluir um item da cotação no ERP TOTVS, será enviado para o Portal de Compras Paradigma os dados para cancelamento do item correspondente. A exclusão de itens da cotação é feito dentro da aba itens da cotação, selecionando o item e clicando em "Excluir".  
***Importante!***

* O item da cotação pode ser excluído quando a cotação estiver com status paradigma igual a "Pendente de Envio", "Parcialmente Integrado" ou "Integrado". Além de respeitar o status paradigma para exclusão de item da cotação também será respeitada a regra referente ao status da cotação.
* Caso seja excluído um item da cotação e ele for o único item que não está integrado, se o status do paradigma for "Parcialmente Integrado" ele será alterado para "Integrado".
* Caso sejam excluídos todos os itens da cotação que estejam integrados, se o status do paradigma for "Parcialmente Integrado" ele será alterado para "Não Integrado".
* Caso o item que esteja sendo excluído tenha sido cotado e retornado pelo Paradigma, o mesmo será excluído no ERP e não será enviado para cancelamento no Paradigma, pois uma vez que o mesmo já foi encerrado no Paradigma não poderá ter seu item de requisição cancelado.
* Caso o item da cotação no Paradigma tenha sido encerrado sem vencedor é necessário que o mesmo seja liberado para ser utilizado em uma nova Cotação. No paradigma esta opção está disponível para escolha por parte do usuário. Entretanto, como não é possível desabilitar a opção de "Não Liberar" no Paradigma, este controle ficará a cargo do usuário, sendo que se o mesmo marcar a opção para não liberar o item da cotação, o mesmo ficará permanentemente bloqueado.

**Cancelamento de Requisição de Compra pelo Portal de Compras Paradigma**

Ao cancelar uma requisição de compra no Portal de Compras Paradigma, o respectivo registro neste portal ficará como "Cancelado".  
 No ERP TOTVS o usuário poderá executar o processo que irá consultar no Portal de Compras Paradigma todas as requisições de compra que foram canceladas através do Portal e realizar a exclusão dos respectivos itens de cotação relacionados a estas requisições de compra.  
 Caso todos os itens da cotação tiverem sido cancelados no Portal, a cotação será cancelada.  
 Este processo é chamado de **"Retorno de Requisições Canceladas pelo Paradigma"** e está disponível na visão de cotação no menu **"Processo".**
