---
article_id: 360034894014
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: bb575b8e5c91d3f515cc2dcfe1a43fdb775d69c3c0b438fe54ebab2588ce1ca9
fetched_at: '2026-06-28T22:39:20.417454+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar Apuração
  de ICMS-ST na Aba de Saídas?
type: support-article
updated_at: '2021-07-13T17:26:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034894014-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-Apura%C3%A7%C3%A3o-de-ICMS-ST-na-Aba-de-Sa%C3%ADdas
---

**Dúvida**Como gerar Apuração de ICMS-ST na Aba de Saídas?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para gerar informações de ICMS ST na Aba de Saídas e para gerar informações do P9autotext, observar a configuração abaixo:

**Parâmetros:**

**MV\_ESTADO** = preenchido.  
**P9AUTOTEXT** = De acordo com o estado.  
**MV\_USASPED** = .T.  
**MV\_P9SPED** = .T.  
**MV\_P9AUTO** = T

**MV\_STUF**=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

**MV\_STUFS**=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

**MV\_SUBTRIB** = preenchido com estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do ICMS ST).

**Importante:**

Quando os parâmetros:  
**MV\_USASPED** = .T. os parâmetros MV\_P9AUTO/MV\_P9SPED devem estar preenchidos = T  
**MV\_USASPED** = .F. os parâmetros MV\_P9AUTO/MV\_P9SPED = devem estar preenchidos = F

Configuração de TES:

Cred ICMS ST (F4\_CREDST) = 2 = Retido ST

**Importante:**

Ao preencher o campo Cred ICMS ST (F4\_CREDST) = 4 Subst.Ttrib., as informações não serão levadas para o livro de ICMS.

Assuntos relacionados:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020388031-MP-FIS-Protheus-Conceito-da-pergunta-Imprime-Cr%C3%A9dito-ST-na-Apura%C3%A7%C3%A3o-de-ICMS-MATA953-?source=search>

<https://tdn.totvs.com/pages/viewpage.action?pageId=235313074>

<https://tdn.totvs.com/pages/releaseview.action?pageId=238035285#FIS0009_Manual_Utiliza%C3%A7%C3%A3o_SPEDFISCAL-REGISTROE200,E210eE250>
