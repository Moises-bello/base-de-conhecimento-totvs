---
article_id: 24339487959703
category: Gestão de Transportes (TMS)
content_hash: 8e262cb87f4d4a4b4425c57a265c40bf6a7a53714f8de267359c6faad1458f79
fetched_at: '2026-06-28T22:45:32.516285+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - RDMAKES para o CTe e MDFe
type: support-article
updated_at: '2026-05-22T19:37:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24339487959703-Log%C3%ADstica-Linha-Protheus-TMS-RDMAKES-para-o-CTe-e-MDFe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24339487937303) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Quais são os **RDMAKES** utilizados para o **CTe** e **MDFe**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Os **RDMAKES** utilizados para o **CTe**, **CTe Simplificado** e **MDFe** são o **CTESEFAZ3**, **RTMSR35**, **CTESEFAZS,** **MDFSEFAZ3** e **RTMSR34**. Um fonte **RDMAKE** pode ser customizado pelo cliente conforme sua necessidade.

* **CTe:**
  + **CTESEFAZ3** - Responsável em gerar o **XML** do **CTe**. Ele é executado durante a transmissão.
  + **RTMSR35** - Impressão do **DACTE**.
* **CTe Simplificado:**
  + **CTESEFAZS** - Responsável em gerar o **XML** do **CTe Simplificado**. Ele é executado durante a transmissão.
* **MDFe:**
  + **MDFSEFAZ3** - Responsável em gerar o **XML** do **MDFe**. Ele é executado durante a transmissão.
  + **RTMSR34** - Impressão do **DAMDFE**.

Para que a impressão do **CTe** ou **MDFe** ocorra, os **rdmakes RTMSR34** e **RTMSR35** devem estar compilados em seu ambiente.  
  
**Obs.:** Conforme legislação vigente, a impressão de **DACTE** não está prevista para o **CTe Simplificado**, por isso não há um layout disponível para utilização.  
  
**Glossário**  
**CTe** - Conhecimento de Transporte Eletrônico;  
**DACTE** - Documento Auxiliar de Conhecimento de Transporte Eletrônico;  
**DAMDFE** - Documento Auxiliar de Manifesto de Documentos Fiscais Eletrônico;  
**MDFe** - Manifesto de Documentos Fiscais Eletrônico;  
**XML** - Extensible Markup Language.  
  
**Anexo**  
Em anexo, segue os **RDMAKES** com as seguintes datas:

* **CTESEFAZ3** - 24/04/2026
* **CTESEFAZS** - 23/04/2026
* **RTMSR35** - 26/02/2026
* **MDFSEFAZ3** - 01/04/2026
* **RTMSR34** - 18/12/2025
