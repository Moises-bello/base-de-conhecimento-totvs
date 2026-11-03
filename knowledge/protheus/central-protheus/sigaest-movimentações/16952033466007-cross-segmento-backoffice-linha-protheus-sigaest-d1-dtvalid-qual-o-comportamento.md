---
article_id: 16952033466007
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 6e050f75e125e6edf5d2d4f9ffcd0c72549d1b9b1d766e42172ad8eefe52d5c9
fetched_at: '2026-06-28T22:38:55.447475+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - D1_DTVALID qual o
  comportamento padrão do campo
type: support-article
updated_at: '2023-08-22T20:05:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16952033466007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-D1-DTVALID-qual-o-comportamento-padr%C3%A3o-do-campo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16952059491607) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Na rotina Documento de Entrada qual o comportamento do campo ***Validade Lote (D1\_DTVALID)*** ao incluir um novo docuemnto de entrada para produtos que controlam Lote?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16952657328791)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Ao incluir um documento de Entrada e na linha de itens, quando informar produtos que controlam Lote, seguem abaixo as considerações e comportamento padrão da rotina:

***- 1 -*** A Data de Validade do Lote do produto automaticamente é considerada a data base do sistema. ***Observações importantes:*** Não impede que seja digitado manualemnte uma Data de Validade diferente da sugerida automaticamente.

***- 2 -*** Também é possível no cadastro de produtos, na aba MRP, configurar o ***campo Prazo Validade (B1\_PRVALID)*** em ***quantidade de dias***, que automaticamente o campo é populado com o determinado no campo. Veja exemplo no print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16952554240791)

***- 3 -*** Caso o Lote (D1\_LOTECTL) informado no campo exista no ambiente, ou ja foi movimentado alguma vez, é apresentado o ***HELP A240DTVALI*** ao clicar em Fechar, o sistema ajusta com a data de Validade existente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16952867287191)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16952907939351)

***- 4 -*** Para os cenário em que precisa informar uma Data de Validade específica para cada inclusão de Lote, somente é possível através de customziação com os Pontos de Entrada abaixo:

***MTA103OK - Altera o resultado da validação padrão para inclusão/alteração de registros de entrada, por customizações do cliente***  
[***https://tdn.totvs.com/pages/releaseview.action?pageId=6087790***](https://tdn.totvs.com/pages/releaseview.action?pageId=6087790)

***MT100TOK - Valida a inclusão de NF***  
***<https://tdn.totvs.com/pages/releaseview.action?pageId=6085400>***

***MT100LOK - Alterações de Itens da NF***  
***<https://tdn.totvs.com/pages/releaseview.action?pageId=6085397>***

***Saiba Mais:***

*[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
