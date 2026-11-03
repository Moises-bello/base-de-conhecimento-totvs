---
article_id: 1500003269981
category: Financeiro - Baixas a Receber
content_hash: 47e6f38da5c9cdda8dede63a3e88a14853bb82c63cf7e2d8a5f150c689943e87
fetched_at: '2026-06-28T22:37:43.827322+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: MP - SIGAFIN - FINA070 - Base de calculo do PCC está incorreto, não abate o
  valor do ISS
type: support-article
updated_at: '2025-07-30T17:57:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003269981-MP-SIGAFIN-FINA070-Base-de-calculo-do-PCC-est%C3%A1-incorreto-n%C3%A3o-abate-o-valor-do-ISS
---

**Dúvida**O sistema calcula a base de PCC incorreto não abate o valor do ISS, sendo que o parâmetro MV\_DESCISS = .T. ?  
  
**Ambiente**Microsiga Protheus -  – Financeiro –FINA070 -  A partir da versão 11.80  
  
**Solução**

**É necessário ajustar o conteúdo do parâmetro *MV\_TPABISS* para o valor adequado, conforme a descrição abaixo:**

* **MV\_TPABISS** *(Parâmetro exclusivo para notas de saída)*

  + Valor **1**: indica que o desconto do ISS será aplicado na duplicata quando o cliente for o responsável pelo recolhimento do imposto;
  + Valor **2**: indica que será gerado um título de abatimento referente ao ISS.

**Exemplo:**  
Para serviços prestados no município de **Barueri**, não deve haver abatimento do ISS no momento da baixa. Além disso, a base de cálculo do PCC deve considerar o valor bruto, ou seja, **sem dedução do ISS**."
