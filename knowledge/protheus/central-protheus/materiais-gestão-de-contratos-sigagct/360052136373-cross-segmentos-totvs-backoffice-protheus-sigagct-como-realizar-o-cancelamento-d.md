---
article_id: 360052136373
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a7e12c7f7eadd996d3865848701f239bc4801c36e7bf4e547518701b1e529802
fetched_at: '2026-06-28T22:37:21.654296+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o cancelamento
  de um Contrato no Gestão de Contratos ?
type: support-article
updated_at: '2026-02-09T13:40:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052136373-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-cancelamento-de-um-Contrato-no-Gest%C3%A3o-de-Contratos
---

**Dúvida**

Como realizar o cancelamento de um contrato no módulo de Gestão de Contratos ?

**Ambiente**

Protheus – Gestão de Contratos – A partir da versão 12.1.23  
  
**Solução**

Para a mudança de status do Contrato para o status "Cancelado", pode-se utilizar a opção existente na rotina de Manutenção conforme sequência abaixo:

Em SIGAGCT->Atualizações->Contratos->Manutenção:

Posicionado sobre o contrato em questão.

![](https://totvssuporte.zendesk.com/attachments/token/RHrLHeqzsXwN8lhDzCVNYYLgE/?name=inline-1718822643.png)

![](https://totvssuporte.zendesk.com/attachments/token/sWnmQNx517Szahk0lk8sbz2ff/?name=inline-2029019440.png)

![](https://totvssuporte.zendesk.com/attachments/token/HKYlExkWXrDmxajCL2KO2tq6d/?name=inline956153296.png)

![](https://totvssuporte.zendesk.com/attachments/token/FS5NnGHVfJDJayfOljgCcpUro/?name=inline1069000548.png)

***Obs1:***

 - Realizando a alteração do status para "Cancelado" os títulos provisórios (PR) existentes para o contrato provenientes de sua inclusão serão excluídos.

 - O Saldo do contrato será mantido, ou seja, não será zerado devido ao cancelamento.

 - As medições realizadas e os Pedidos/Títulos provenientes dessas medições já realizadas não serão estornados ou excluídos.

- Um contrato no qual foi realizado o Cancelamento (Contrato com Status Cancelado), não possui mais a possibilidade de inclusão/estorno de medições ou de sofrer qualquer outra movimentações .

- Atualmente o processo de cancelamento de contrato não possui uma funcionalidade para a informação de um motivo de cancelamento.

- A Data em que o contrato foi cancelado pode ser retirada do campo Dt Ult Statu (CN9\_DTULST) que guarda a data de ultima atualização de Status do contrato.

***Obs2:***

**Perg.:** Tem alguma forma de reverter o cancelamento do contrato, para que possa estornar a medição?

Segue abaixo as Mensagens que ocorrem ao tentar estornar um contrato cancelado.

**Help: CNTA120\_10**

**Problema:** Ação não disponível para contrato cancelado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38267852012183)

**Resp.:*****Importante:***

Por Conceito do Módulo de Gestão de Contratos, a situação de "Cancelado" em contrato é definitiva/irreversível, não sendo possível realizar a exclusão ou Mudança de Situação para outro Status de um Contrato Cancelado.

***Saiba Mais:***

[MP - SIGAGCT - Ciclo de vida do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026376592-MP-SIGAGCT-Ciclo-de-vida-do-Contrato?source=search)

[MP - SIGAGCT - Existe a possibilidade de excluir ou estornar um contrato com status Finalizado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024697991-MP-SIGAGCT-CNTA300-Manuten%C3%A7%C3%A3o-de-Contratos-retornar-status-finalizado)

[MP - SIGAGCT - É possível alterar um contrato da situação de Solicitação de Finalização para Vigente ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022098611-MP-Gest%C3%A3o-de-contratos-Como-alterar-a-situa%C3%A7%C3%A3o-de-um-contrato-de-solicita%C3%A7%C3%A3o-de-finaliza%C3%A7%C3%A3o-para-vigente-novamente)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
