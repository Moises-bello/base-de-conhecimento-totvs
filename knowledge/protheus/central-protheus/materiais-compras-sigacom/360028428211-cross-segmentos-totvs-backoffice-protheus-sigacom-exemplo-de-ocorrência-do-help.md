---
article_id: 360028428211
category: Materiais - Compras (SIGACOM)
content_hash: f6cf78443a17c23986f65e06fb2fdc79692ce986a03ebfdf8ce6f6b180297d90
fetched_at: '2026-06-28T22:41:08.872673+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de ocorrência
  do Help EXISTSCR na Solicitação de Compras
type: support-article
updated_at: '2022-05-12T21:15:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028428211-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-ocorr%C3%AAncia-do-Help-EXISTSCR-na-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**

Exemplo de ocorrência do Help EXISTSCR na Solicitação de Compras

**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Após configurar a alçada por centro de custo e ao mesmo tempo, bloqueio de solicitação de compras **MV\_APROVSC** e **MV\_APRSCEC**, incluir uma solicitação de compras com dois itens onde em um deles foi informado dados de entidade contábil, o sistema pode bloquear o primeiro item para liberação via rotina Liberação de Documento (MATA094), pois pode existir controle de Alçadas por entidade contábil e o outro item para liberação na própria rotina de Solicitação de Compras (MATA110).

Nessa situação é possível somente liberar o item pela rotina Liberação de Documentos e o outro item ao tentar liberar o sistema informa que deve ser liberado pela rotina de liberação de documentos o que não procede.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028488371/mceclip1.png)

A mensagem EXISTSCR é apresentada somente quanto existir bloqueio com registro na tabela SCR.

Dessa forma atualizado com os últimos pacotes disponíveis no Portal do Cliente, quando o sistema encontrar Grupo de Aprovação (MATA114) que possua os flags da aba tipo de documento com Solicitação de Compras, informações de entidade contábil e que se enquadre nas informações de entidade contábil compatível com a Solicitação de Compras o sistema direciona a aprovação para o aprovador específico conforme o grupo de aprovação.

![](https://totvssuporte.zendesk.com/attachments/token/xbSQjiraovpwRkwwsspXjAGwg/?name=inline766016485.png)​​

Essa liberação é executada a partir da rotina Liberação de Documento (MATA094).

Dessa forma existe a possibilidade de um item da solicitação de compras bloquear pela rotina MATA110 e o outro item bloquear para liberar no MATA094 porque se enquadrou na configuração do grupo de aprovação.  
Se não for utilizar pela rotina de liberação de documentos deve tirar o flag do grupo que o sistema indicou. Para identificar qual grupo de aprovação o sistema apontou, na Solicitação de Compras pressione o botão Outras Ações > Log Aprov., nesta opção será apresentado para qual aprovador foi direcionado e para qual grupo.

![](https://totvssuporte.zendesk.com/attachments/token/JgdG2UxEQhZSpJR77c5DET8C3/?name=inline-1899338691.png)

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
