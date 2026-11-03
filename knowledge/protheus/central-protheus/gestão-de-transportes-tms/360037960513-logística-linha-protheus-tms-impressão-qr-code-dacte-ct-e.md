---
article_id: 360037960513
category: Gestão de Transportes (TMS)
content_hash: 9b161412b8027cbad4432fc6021445fbd87e35cc94236849e61520f7d8d3647e
fetched_at: '2026-06-28T22:45:29.315551+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Impressão QR Code DACTE CT-e
type: support-article
updated_at: '2023-07-20T14:39:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037960513-Log%C3%ADstica-Linha-Protheus-TMS-Impress%C3%A3o-QR-Code-DACTE-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16162917324823)***Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**Na impressão da **DACTE** do **CT-e** há o **QR Code**, e podem ocorre falhas no *layout* de impressão, fazendo alguns elementos sobreporem outros.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Causa**O erro ocorria no **Printer.exe** de impressão e, por consequência, no fonte de impressão da **DACTE.  
  
Solução**Para ajustar o *layout* de impressão, é necessário atualizar o**Printer.exe** da pasta **appserver** e **smartclient** do **Protheus** e a **LIB** do repositório.

* **Printer:**
  + [PRINTER\_WINDOWS\_X64.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=693168)
* **LIB:**
  + [LIB\_LABEL\_P12\_LOBO.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=989259)
  + [LIB\_LABEL\_P12\_HARPIA](https://suporte.totvs.com/portal/p/10098/download?e=1050526)

Após a atualização, a impressão da **DACTE** deve sair da seguinte forma:

![dacte___.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360050011253)

**Glossário  
CT-e**- Conhecimento de Transporte Eletrônico **DACTE**- Documento Auxiliar do Conhecimento de Transporte Eletrônico  
**LIB -** Library   
**QR Code***-*Quick Response **XML** - Extensible Markup Language
