---
article_id: 360047569294
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: e66023bf25566b3cdb913408600cad7c1b068105b660f0600b88fa6f276acc42
fetched_at: '2026-06-28T22:39:20.378485+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o ST
  do FRETE com a alíquota do produto?
type: support-article
updated_at: '2021-07-13T17:24:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047569294-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-ST-do-FRETE-com-a-al%C3%ADquota-do-produto
---

**Dúvida**Como Calcular o ST do FRETE com a alíquota do produto?

**Ambiente**Protheus - fiscal -  A partir da versão 11.80  
  
**Solução**

Para calcular o ICMS ST na entrada de conhecimento de frete pela rotina MATA116 preencha os parâmetros a seguir:

**MV\_FRETEST:**  Deve ter a alíquota interna do Estado considerada a padrão. Ex.: SP18MG18;

**MV\_M116FOR**: Define a origem dos impostos para gerar a nota de conhecimento de frete **T=**fornecedor do frete **F=** fornecedor da nota de origem. Ex.: F;

**MV\_ICMPAD**: Define a alíquota de ICMS aplicada em operações dentro do Estado onde a empresa está localizada (17 ou 18%). Ex.: 18;

Se o produto da operação tem alíquota de ICMS diferenciada, o B1\_ICMPAD ou equivalente da tabela SBZ, ou ainda a exceção fiscal deve ter a alíquota definida para que o sistema faça o cálculo correto.
