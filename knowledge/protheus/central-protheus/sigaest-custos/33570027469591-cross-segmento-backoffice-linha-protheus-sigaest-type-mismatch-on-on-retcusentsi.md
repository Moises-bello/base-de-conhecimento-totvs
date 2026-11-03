---
article_id: 33570027469591
category: SIGAEST - CUSTOS
content_hash: 6c78f4896280c6d362e1306541646db60e0552ca5a72cb5da8e53c94fe10fd21
fetched_at: '2026-06-28T22:39:02.361044+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - type mismatch on
  +  on RETCUSENT(SIGACUSA.PRX) 15/05/2025 19:26:39 line : 4782'
type: support-article
updated_at: '2025-07-18T20:54:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33570027469591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-type-mismatch-on-on-RETCUSENT-SIGACUSA-PRX-15-05-2025-19-26-39-line-4782
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33570027460119) Tempo aproximado para leitura: **00:03:30 min**  
  
**Dúvida**

Ao incluir um Documento de Entrada apresenta o error.log abaixo. Como corrigir?

**type mismatch on +  on RETCUSENT(SIGACUSA.PRX) 15/05/2025 19:26:39 line : 4782**

[TOTVS build: 7.00.240223P-20250326]  
**Called from A103XCUSTO(MATA103XEST.PRW) 27/11/2024 14:35:19 line : 720**  
Called from A103CUSTO(MATA103.PRW) 27/12/2024 18:52:09 line : 17055  
Called from A103GRAVA(MATA103.PRW) 27/12/2024 18:52:09 line : 15078  
Called from A103NFISCAL(MATA103.PRW) 27/12/2024 18:52:09 line : 3680  
Called from FWFORMBROWSE:EXECUTE(FWFORMBROWSE.PRW) 27/06/2025 17:07:23 line : 1148  
Called from {|| OSELF:EXECUTE("A103NFISCAL",              3,             0,"INCLUIR",              3,"","INCLUIR","",               3) }(FWFORMBROWSE.PRW) 27/06/2025 17:07:23 line : 580  
Called from ::MSDIALOG:ACTIVATE  
Called from FWMBROWSE:ACTIVATE(FWMBROWSE.PRW) 27/06/2025 17:07:23 line : 696  
Called from FWMBROWSE(MSLIB.PRW) 27/06/2025 17:07:23 line : 10488  
Called from MBROWSE(MSLIB.PRW) 27/06/2025 17:07:23 line : 171  
Called from MATA103(MATA103.PRW) 27/12/2024 18:52:09 line : 293  
Called from \_\_EXECUTE(APLIB090.PRW) 27/06/2025 17:07:18 line : 733  
Called from MDIEXECUTE(APLIB260.PRW) 27/06/2025 17:07:18 line : 923  
  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para correção desse error.log verificar o release e aplicar em Base de Homologação os pacotes abaixo e testar antes de sua base Oficial.

**12.1.2410:**[**https://r.totvs.io/p/1196774****;**](https://r.totvs.io/p/1196774)

**12.1.2310:**[**https://r.totvs.io/p/1196775****;**](https://r.totvs.io/p/1196775)

**TAMBÉM RECOMENDAMOS MANTER PACOTE ACUMULADO BACKOFFICE ATUALIZADO VEJA NO LINK ABAIXO:**

[***https://tdn.totvs.com/x/2hgdHw***](https://tdn.totvs.com/x/2hgdHw)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
