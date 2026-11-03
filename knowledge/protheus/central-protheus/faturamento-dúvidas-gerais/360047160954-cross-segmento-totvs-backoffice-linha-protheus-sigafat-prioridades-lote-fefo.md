---
article_id: 360047160954
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: be073111cc8ae10a24885a53d6cc1179f750c15f8ff7228690f1c158b05cb50f
fetched_at: '2026-06-28T22:38:28.655908+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Prioridades
  Lote (FEFO)
type: support-article
updated_at: '2022-12-15T20:29:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047160954-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Prioridades-Lote-FEFO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**É possível no momento de inserir um pedido de venda, que o sistema sugira o lote mais antigo para o mais novo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  A partir da versão 11.80.

**Solução**

O controle utilizado para escolha do lote é *FEFO* (First Expire First Out), se ao preencher no pedido um produto com lote e não informar o lote na linha do item, ele ira buscar o **próximo lote a vencer**e preencher no pedido.

Sendo assim se o primeiro lote estiver vencendo primeiro que os demais, o sistema irá trabalhar da forma que deseja, mas irá depender do vencimento do lote.

No caso de um controle diferenciado na liberação do estoque é necessário o uso de ponto de entrada.

Abaixo indicamos o ponto de entrada que possa te interessar:

**MA440GRLT**- Movimentar estoque antes da seleção lote x localização física  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6784285>

**Saiba mais**: [Uso de Lote, Endereçamento e Serie no Faturamento (SIGAFAT)](https://tdn.totvs.com/x/DpNvI)
