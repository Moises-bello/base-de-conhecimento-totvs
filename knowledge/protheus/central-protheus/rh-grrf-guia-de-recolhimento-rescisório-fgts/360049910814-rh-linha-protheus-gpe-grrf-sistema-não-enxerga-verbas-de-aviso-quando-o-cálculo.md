---
article_id: 360049910814
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: 431b44a8f72d6e1ab4c58d7b9996e56394bb1b74aa1960d25c2a0cc049cb5870
fetched_at: '2026-06-28T22:43:32.401447+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - GRRF - Sistema não enxerga verbas de Aviso quando
  o cálculo é do Tipo de Rescisão - Aviso Trabalhado
type: support-article
updated_at: '2021-04-30T18:19:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049910814-RH-Linha-Protheus-GPE-GRRF-Sistema-n%C3%A3o-enxerga-verbas-de-Aviso-quando-o-c%C3%A1lculo-%C3%A9-do-Tipo-de-Rescis%C3%A3o-Aviso-Trabalhado
---

**Ocorrência**GRRF - Sistema não enxerga verbas de Aviso quando o cálculo é do Tipo de Rescisão - Aviso Trabalhado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12  
  
**Solução**Existe uma regra em que quando o aviso prévio for do tipo **1-Trabalhado** ou **3 - Ausência/Dispensa**, os valores relativos a essas verbas devem ser mantidos na coluna **Rem. Mês Resc** para que não ocasione o erro 392 na validação do arquivo GRRF.  
  
Por isso, nas situações onde o aviso prévio do funcionário foi trabalhado, porém o mesmo possui o direito na indenização dos 3 dias de salário para cada ano trabalhado e é pago no Identificador 0111 (Aviso Indenizado), na geração da GRRF eletrônica ajustada de acordo com especificação do layout para não preenchimento do campo 'Aviso Prévio Indenizado' em caso de aviso misto e que o valor do Aviso Prévio Indenizado seja somado à Coluna Rem. Mês Rescisão.  
  
**Importante**  
Material disponibilizada pelo desenvolvimento:  
[2780157 DRHGCH-2250 DT GRRF de rescisão com aviso misto](https://tdn.totvs.com/pages/releaseview.action?pageId=360453851)
