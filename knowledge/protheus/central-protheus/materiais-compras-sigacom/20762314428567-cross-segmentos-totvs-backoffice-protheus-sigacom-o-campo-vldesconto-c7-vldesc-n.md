---
article_id: 20762314428567
category: Materiais - Compras (SIGACOM)
content_hash: 72cc9d3a1be16422ce736589ec2ed293a0f87f921e8fd6d3f80b0b5db1d88783
fetched_at: '2026-06-28T22:41:10.082279+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O campo Vl.Desconto
  (C7_VLDESC)  não é atualizado quando o percentual de desconto é zerado na Aba de
  Descontos.
type: support-article
updated_at: '2024-01-22T15:10:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20762314428567-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-campo-Vl-Desconto-C7-VLDESC-n%C3%A3o-%C3%A9-atualizado-quando-o-percentual-de-desconto-%C3%A9-zerado-na-Aba-de-Descontos
---

**Dúvida**O campo Vl.Desconto (C7\_VLDESC) não é atualizado quando o percentual de desconto é zerado na Aba de Descontos.

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Solução**

O parâmetro **MV\_LMPDESC** determina se os valores de desconto dos itens devem ser zerados quando a soma dos percentuais de desconto (na pasta Descontos) for igual a zero.

1. No módulo Configurador (SIGACFG), acesse Ambiente / Cadastro / Parâmetros (CFGX017) e ajuste o conteúdo do parâmetro MV\_LMPDESC de acordo com a opção desejada.
2. No módulo Compras (SIGACOM), acesse Atualizações / Pedidos / Pedidos de Compra.
3. Ao incluir um Pedido de Compra, se os percentuais de descontos estiverem zerados na pasta Descontos, os valores de desconto dos itens também serão zerados, desde que, o parâmetro MV\_LMPDESC esteja ativo.

**Saiba mais:**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**
