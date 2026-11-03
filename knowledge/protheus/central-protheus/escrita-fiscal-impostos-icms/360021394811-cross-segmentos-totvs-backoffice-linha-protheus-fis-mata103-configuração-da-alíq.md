---
article_id: 360021394811
category: Escrita Fiscal - Impostos - ICMS
content_hash: 588b991d82396d7558cc1c3b7b8cab72926e56f2e003fbe320ae3f53fc1f2a17
fetched_at: '2026-06-28T22:39:24.025843+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS-Mata103 - Configuração
  da alíquota do FRETE - CTE'
type: support-article
updated_at: '2021-07-20T14:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021394811--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Mata103-Configura%C3%A7%C3%A3o-da-al%C3%ADquota-do-FRETE-CTE
---

**Dúvida**Como configurar a alíquota na rotina mata116 / mata103 do CTE   
  
   
 **Ambiente**Protheus - mata103 / mata116 - Sigacom - Sigafis – A partir da versão 11.80]  
  
   
**Solução**

Para calcular o ICMS ST na entrada de conhecimento de frete pela rotina MATA116 preencha os parâmetros a seguir:

**MV\_FRETEST:**  Deve ter a alíquota interna do Estado considerada a padrão. Ex.: SP18MG18;

**MV\_M116FOR**: Define a origem dos impostos para gerar a nota de conhecimento de frete **T=**fornecedor do frete **F=** fornecedor da nota de origem. Ex.: F;

**MV\_ICMPAD**: Define a alíquota de ICMS aplicada em operações dentro do Estado onde a empresa está localizada (17 ou 18%). Ex.: 18;

Se o produto da operação tem alíquota de ICMS diferenciada, o B1\_ICMPAD ou equivalente da tabela SBZ, ou ainda a exceção fiscal deve ter a alíquota definida para que o sistema faça o cálculo correto.
