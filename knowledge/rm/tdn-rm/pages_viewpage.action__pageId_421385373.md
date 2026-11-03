---
content_hash: 9f3dbc2eadcb4eec512b93d9fae41444b54ec0baba0fee5565704aaf8c3a223c
fetched_at: '2026-06-29T00:09:15.409055+00:00'
page_id: '421385373'
product: rm
source: tdn-rm
title: Cancelamento de Liberação 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385373
version: 8
---

Para contratos que geraram movimentos e/ou lançamentos financeiros por meio da liberação de períodos, é possível realizar seu cancelamento por meio do processo "Cancelamento de Liberação.

**Abaixo estão algumas situações em que o cancelamento da liberação pode ser realizado:**

* O cancelamento da liberação de qualquer período é permitido desde que o status do seu movimento esteja como **PENDENTE**.
* Quando o status do movimento gerado é **diferente de PENDENTE**, o usuário deve criar um período de estorno manualmente e realizar a medição correspondente para efetivar o estorno do período.
* É permitido gerar automaticamente um período de estorno para períodos complementares, respeitando as mesmas regras do período principal.
* Se um período foi liberado e o movimento gerado está como **PENDENTE** no BackOffice, o cancelamento pode ser feito diretamente através da função "Cancelar Movimento" no BackOffice. Isso gera automaticamente um período de estorno no contrato correspondente.
* Ao cancelar os períodos do contrato, o sistema gera automaticamente um período de estorno correspondente. Caso o cancelamento dos períodos seja feito em massa, será criado apenas um período de estorno para todos os períodos cancelados.

Observação:

O cancelamento do movimento diretamente pelo BackOffice gerando período de estorno no Contrato só é permitida desde que as quantidades dos itens do movimento estejam iguais as originais enviadas pelo Contrato.

**Observação:**  
O processo de cancelamento cancelará todos os movimentos gerados para o período correspondente. Será adicionado automaticamente um período de estorno já liberado contendo as medições referentes ao período cancelado.

**Situação onde o cancelamento da liberação gerando estorno automático NÃO pode ser realizado:**

* Quando o movimento gerado apresenta status diferente de "**pendente**" no BackOffice.
* Não é permitido realizar o cancelamento do período que já teve a retenção liberada e que apresenta movimentação diferente de pendente;  
  **Obs.:** Caso haja retenção no período a ser estornado e ela já tenha sido liberada, o estorno automático será realizado. O status da retenção contratual será alterado para "Período cancelado" e uma linha de retenção contratual de estorno será gerada com o código de período "000XEX" e status "Liberado".
* Não é permitida a inclusão de períodos de estorno parciais enquanto a movimentação do período de origem estiver pendente, pois nesse caso é necessário realizar o cancelamento da movimentação e efetuar um estorno total. É importante seguir esse procedimento para garantir a integridade das informações e evitar possíveis erros ou inconsistências nos registros.
* No caso de medições com rateio por município, o estorno automático só será realizado se todos os movimentos gerados pela medição estiverem com o status pendente.
* Não será gerado um período de estorno automático para o último período liberado, pois não há um período subsequente liberado para realizar a reversão.
* Se um período de estorno for gerado automaticamente por meio do processo de Cancelamento de Liberação, não será possível criar manualmente um período de estorno para o mesmo período que foi cancelado.
* Ao realizar o processo de "Cancelamento de liberação" no contrato, não será gerado um período de estorno automático para o último período criado.

   

  Informação cancelamento de periodo

  Ao executar o "Cancelamento de Liberação", o movimento é excluído e o período volta ao estado de medição no Totvs Obras e Projetos.

  ## Cancelamento de Liberação de Período com o [Parâmetro "Última Medição"](https://tdn.totvs.com/pages/viewpage.action?pageId=421385359&draft=true) Marcado

  Ao realizar o cancelamento de uma liberação onde o campo **"Última Medição do Contrato"** foi utilizado, observe os seguintes impactos:

* **Status do Contrato:** O contrato retorna ao status anterior (se utilizar controle de saldo).
* **Gestão de Saldo:** O saldo que já foi devolvido ao planejamento **não retorna automaticamente** ao contrato. Para recuperá-lo, é obrigatória a criação de um novo aditivo.
* **Manutenção da Flag:** O campo "Última Medição do Contrato" **permanece marcado** mesmo após o cancelamento. Cabe ao usuário decidir manualmente se deve desmarcá-lo ou não.

###
