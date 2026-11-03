---
article_id: 1500007495161
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 75ba664b8a3d96fcf7a69a0e5459d58d5ee006a097d544e4a9c4f0d59e96e2ce
fetched_at: '2026-06-28T22:38:38.429108+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Verificar Pedido
  com Liberação Parcial
type: support-article
updated_at: '2022-08-29T17:32:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007495161-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Verificar-Pedido-com-Libera%C3%A7%C3%A3o-Parcial
---

**Duvida**Existe algum campo no pedido de venda ou relatório que indique a quantidade já faturada pelo pedido, quando o mesmo for faturado parcialmente?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Não há nenhum campo no pedido de venda e nenhum relatório para esta finalidade, neste caso pode utilizar a consulta genérica relacional com as tabelas **SC6** e **SF2** , filtrar todos os pedidos que possuem número de nota preenchido, no campo **C6\_NOTA.**

Outra opção é a consulta genérica da **SC9**, onde a indicação de faturamento do pedido se dá pelos campo **C9\_BLEST** e **C9\_BLCRED** que ficam com conteúdo igual a **10** quando houve faturamento e se foi parcial, existe o campo **C9\_SEQUEN**, indicando se há sequencias de liberação do pedido.  
  
em último caso , criar o próprio relatório em Miscelâneas, relatórios Totvs, na dúvida de uso dessa ferramenta, contate a equipe de ADVPL para auxiliar.

Saiba Mais sobre criação de relatórios: 

[MP-ADVPL-RELATORIO-TOTVS-REPORT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018079912-MP-ADVPL-RELATORIO-TOTVS-REPORT)

[MP - TEC - Exemplo de criação utilizando RELATÓRIO TOTVS (PREPORT.PRW)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046862153-MP-TEC-Exemplo-de-cria%C3%A7%C3%A3o-utilizando-RELAT%C3%93RIO-TOTVS-PREPORT-PRW-)
