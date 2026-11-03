---
article_id: 1500008500402
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 13ccafe45df31247b82fe16305c585ff503ef418be8508accc22e049d9388b47
fetched_at: '2026-06-28T22:39:19.323131+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: Cross Segmentos / Totvs Backoffice / Escrituração  e Relatórios Oficiais /
  - Como escriturar diferencial de aliquotas em SP quando há saldo credor?
type: support-article
updated_at: '2024-10-08T21:23:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008500402-Cross-Segmentos-Totvs-Backoffice-Escritura%C3%A7%C3%A3o-e-Relat%C3%B3rios-Oficiais-Como-escriturar-diferencial-de-aliquotas-em-SP-quando-h%C3%A1-saldo-credor
---

**Dúvida**Como escriturar diferencial de alíquotas em SP quando há saldo credor ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O diferencial de alíquotas deve ser recolhido na apuração do ICMS para as compras fora do estado da seguinte forma:

MV\_estado = SP  
MV\_art117 = .F.  
MV\_p9sped = .T.  
MV\_p9auto = T  
MV\_rf3thred = como T e como F

Fornecedor = fora do estado de SP

TES  
Calcula icms = sim  
L fiscal icms = outros  
Cst = 90  
mat consumo = sim  
Calc dif icms = sim

O lançamento da nota fiscal em compras:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012454502/mceclip1.png) ​

valor do diferencial 60,00

Este valor será levado para apuração do icms e se houver saldo credor anterior deverá ser deduzido

Neste caso ao configurar a apuração do icms não gerar Guia icms complementar:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012454562/mceclip2.png)

Apuração ICMS:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012801201/mceclip3.png)

Dessa forma não será gerado GNRE pois está sendo deduzido do saldo credor.
