---
content_hash: ef023bfa5b68e431ca0ee77f5a68d8ff3a848f9a9fbec2fe638998ebfc7ea7fa
fetched_at: '2026-06-29T00:09:26.124459+00:00'
page_id: '423938268'
product: rm
source: tdn-rm
title: Cancelamento de Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelamento+de+Movimento
version: 4
---

O processo de Cancelamento de Movimentos tem o intuito de fazer com que as rotinas tratadas dentro de um movimento (por exemplo, rotinas contábeis, financeiras, de estoque, entre outras) sejam desfeitas, não sendo somente um processo para alteração do Status do movimento, mas retirando todas as integrações executadas por este movimento, atingindo o objetivo de um sistema integrado a outros módulos.  
Por questões de critérios de integração e responsabilidade das informações entre os módulos, somente o aplicativo que criou o movimento pode cancelá-lo. Portanto, um movimento criado pelo sistema de Gestão da Produção não poderá ser cancelado dentro do sistema de Gestão de Estoque, devendo o processo ser revertido no sistema de Gestão da Produção.

**Ao Efetuar o Cancelamento de Movimentos**

Se forem selecionados diversos movimentos e um destes já estiver cancelado, o sistema apresentará um log de execução, ao final do processo, informando que este movimento não pôde ser cancelado por já estar nesta condição, mas executa o processo de cancelamento para todos os outros movimentos selecionados.  
Caso este movimento esteja integrado com alguns processos em outros aplicativos:

* Ordem de Produção no sistema de Gestão da Produção;
* Ordem de Serviço no sistema de Gestão de Manutenção;
* Empréstimo ou Compra de EPI (Equipamento de Proteção Individual) no sistema de Gestão de Pessoas;
* Compra de Bens no sistema de Gestão Patrimonial;
* Aprovação por Workflow no sistema de Gestão do Relacionamento com o Cliente), o sistema irá cancelar e excluir o atendimento vinculado àquele movimento, durante o processo de cancelamento. Caso o movimento tenha afetado o Orçamento, ao efetuar o cancelamento, o sistema inverte o efeito do valor desta movimentação, de acordo com seu efeito no

**Controle Orçamentário**

Caso o movimento tenha gerado lançamentos financeiros (sistema de Gestão Financeira), ao cancelar este movimento, os lançamentos financeiros também serão cancelados.  
Caso o movimento tenha sido gerado pela rotina de Cotação (Ordem de Compras), ao efetuar o cancelamento, o sistema reabrirá o processo de Cotação, permitindo que a Ordem de Compras seja novamente gerada.  
Se trata de um processo irreversível, não sendo possível desfazê-lo.

**Melhorias com a Migração do Cancelamento de Movimentos**

Quando uma Solicitação de Compras dá origem a uma Cotação, e esta Cotação, por sua vez, gera 2 movimentos de Ordem de Compras, caso 1 destes movimentos seja cancelado e a Cotação não esteja parametrizada para 'Permitir Cotação Parcialmente Gerada', não mais será necessário utilizar a rotina de 'Gerar Mov. a Partir de Itens Não Cotados', pois, com o Faturamento Parcial, este movimento poderá ser recebido sem qualquer impedimento, já que, quando do cancelamento da Ordem de Compras, a quantidade do movimento de Ordem de Compras cancelado 'retorna' para o movimento de Solicitação de Compras, permitindo a continuação do processo por Faturamento ou nova Cotação.  
Quando existe uma Solicitação de Compras, com somente 1 Item, este Item passa pelo processo de Cotação onde existem 2 Fornecedores, e cada um destes Fornecedores gera uma 'parte' da quantidade deste Item para as Ordens de Compra destes Fornecedores, ao se cancelar uma destas Ordens de Compra, caso a Cotação não permita ser parcialmente gerada, o movimento de Solicitação de Compras será alterado com a Quantidade restante (que foi cancelada no movimento), permitindo que o Faturamento deste movimento de Solicitação de Compras ocorra, sem a necessidade de efetuar uma nova Cotação para este Item.  
Quando a Cotação 1, com somente 1 Item, gerar uma Ordem de Compras, e a Cotação 2, com 2 Itens, gerar 2 Ordens de Compras (uma para cada Item), sendo que um dos Itens será inserido na outra Ordem de Compras da Cotação 1, ao cancelar este movimento de Ordem de Compras que possuirá itens das 2 Cotações, o sistema permitirá que o processo do movimento seja completamente desfeito, de modo a refazer a Cotação e a geração de suas Ordens de Compra, de acordo com a necessidade. Lembrando que, para que o processo seja completamente desfeito, todos os demais movimentos relacionados às Cotações 1 e 2 deverão ser cancelados.  
Todo o processo de cancelamento contará com um log de execução, que apresentará detalhes sobre cada movimento selecionado para a execução do Cancelamento e o efeito atingido.

Integração EAI 2.0

Quando na base de dados existir algum pacote de integração que faça uso de mensagens de Lançamentos Financeiros, o envio do cancelamento destes lançamentos financeiros para o EAI irá ocorrer somente no final do processo de Cancelar Movimentos.

Este recurso está disponível nas versões da Biblioteca RM: 12.1.32.348 e superiores, 12.1.2205.161 e superiores,  12.1.2209.106 e superiores

Para maiores informações sobre a integração dos lançamentos financeiros com EAI consulte o documento [Mensagem EAI](https://tdn.totvs.com/display/LRM/Mensagem+EAI).
