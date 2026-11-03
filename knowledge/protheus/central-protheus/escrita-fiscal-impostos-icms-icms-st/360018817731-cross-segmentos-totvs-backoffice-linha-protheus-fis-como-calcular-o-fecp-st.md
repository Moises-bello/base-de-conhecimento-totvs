---
article_id: 360018817731
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 1b6123fc087271e5399f1f9c705859d21417883ef459dce554d01d322fa8fcd7
fetched_at: '2026-06-28T22:39:20.371099+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o FECP
  ST?
type: support-article
updated_at: '2024-02-07T20:07:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018817731-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-FECP-ST
---

**Dúvida**Como configurar o sistema para calcular o FECP (fundo de combate a pobreza) sobre o ST?  
  
**Ambiente**Protheus – Livros Fiscais– A partir da versão 11.80  
  
**Solução**

O FECP deverá ser configurado pela rotina FISA080- UFXUF:

UF Origem  - Informe o estado de origem   
UF Destino - Informe o estado de destino   
Aliq FECP - Informe % do FECP

TES:

Isen FECP = Não

**Importante - Operações com Substituição Tributária**

Para que o **FCP-ST** seja calculado corretamente é **obrigatório** o uso de um CST de Substituição Tributária: 10, 30 ou 70. Esta regra é válida para **todos** os estados, em operações de entrada e saída.

Link da documentação:

UF x UF (FISA080)

<https://tdn.totvs.com/display/PROT/CADUF+-+UFxUF>

Tratamento dos Fundos Estaduais de Combate à Pobreza

<https://tdn.totvs.com/pages/releaseview.action?pageId=701693062>
