---
article_id: 360036571013
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c66663358880703411c131db13c72b71209c39d8db148eeea73ff5953d1197b6
fetched_at: '2026-06-28T22:38:44.166518+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Qual o processo para exclusão
  de Documento de Saída que possui o RA Compensado?
type: support-article
updated_at: '2025-09-11T11:02:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036571013-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Qual-o-processo-para-exclus%C3%A3o-de-Documento-de-Sa%C3%ADda-que-possui-o-RA-Compensado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34862300524311)** **Tempo aproximado para leitura:****00:04:10 min**

**Dúvida**

Qual o processo para exclusão de Documento de Saída que possui o RA Compensado?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Quando um Pedido de Vendas é vinculado a um RA (Recebimento Antecipado) e o Documento de Saída é preparado, o título do RA é automaticamente compensado no Financeiro.

Caso seja necessário excluir o Documento de Saída, o sistema deve estornar automaticamente a compensação do RA, retornando o título à situação de aberto.

Importante ressaltar que não é possível realizar estorno ou manutenção manual do RA em rotinas financeiras quando este está vinculado a um documento, o vínculo e o controle de estorno são feitos exclusivamente pelo processo de Exclusão do Documento de Saída (MATA521A), **qualquer tentativa de manutenção manual resultará em inconsistências**.

Em alguns cenários, ao tentar excluir o Documento de Saída, pode ser exibida a mensagem:

"Não foi possível excluir a compensação associada ao título deste Documento de Saída. Não será possível excluir o Documento de Saída."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34862333472279)

**O que avaliar neste caso:**

1 - Verificar se existem fontes customizados interceptando o processo de emissão do documento e/ou título;

2 - Avaliar se houve manutenção manual nos títulos do RA ou nas tabelas de vínculo, como **FIE (Pedidos x Adiantamento)** e **FR3 (Pedidos x Compensação)**, pois divergências nesses relacionamentos podem impedir o estorno automático do Documento de Saída;

3 - Conferir também se o valor originalmente compensado no RA coincide com o valor a ser estornado na exclusão.

**Em ambiente sem customizações e com dados íntegros, o comportamento correto é:**

* Documento de Saída é excluído;
* Compensação do RA é desfeita automaticamente;
* RA volta a ficar em aberto.

**Saiba mais:**

[Adiantamento no Pedido de Vendas](https://tdn.totvs.com/x/-pgcKw)

[FAT0149 - Recebimento Antecipado (RA/Adiantamento) no Pedido de Venda (MATA410)](https://tdn.totvs.com/x/GkD2Dw)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Como vincular ou Desvincular RA no Pedido de Vendas pela Rotina MATA410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017422212-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-vincular-ou-Desvincular-RA-no-Pedido-de-Vendas-pela-Rotina-MATA410)
