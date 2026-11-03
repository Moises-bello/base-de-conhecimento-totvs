---
article_id: 360018845611
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: c67f7abc23b3da3658a640fdff3097a9a82a87bd527ea005fef6bf5c138a708c
fetched_at: '2026-06-28T22:39:20.366150+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o FECP
  (Fundo de Combate à pobreza) nas operações com ICMS ST?
type: support-article
updated_at: '2024-04-16T10:03:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018845611-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-FECP-Fundo-de-Combate-%C3%A0-pobreza-nas-opera%C3%A7%C3%B5es-com-ICMS-ST
---

**Dúvida**Como calcular o FECP (Fundo de combate à pobreza) nas operações com ICMS ST?   
  
**Ambiente**Protheus - Livros Fiscais - a partir da versão 11.80.   
  
**Solução**Para cálculo do FECP (Fundo de combate à pobreza) nas operações com ICMS ST deverá ser utilizado a rotina FISA080 (UF x UF).

Informe os campos abaixo:   
UF Origem -   
UF Destino -  
Aliq FECP -

TES:  
Isen FECP = Não  
Sit Trib ICM = 10, 30 ou 70.

**Importante - Operações com Substituição Tributária**

**Para que o FCP-ST seja calculado corretamente é obrigatório o uso de um CST de Substituição Tributária: 10, 30 ou 70. Esta regra é válida para todos os estados, em operações de entrada e saída.**

Segue documentação FISA080:

<https://tdn.totvs.com/display/public/PROT/CADUF+-+UFxUF>

Documentação sobre os Fundos de combate a pobreza:

<https://tdn.totvs.com/pages/releaseview.action?pageId=701693062>

\*\*\*
