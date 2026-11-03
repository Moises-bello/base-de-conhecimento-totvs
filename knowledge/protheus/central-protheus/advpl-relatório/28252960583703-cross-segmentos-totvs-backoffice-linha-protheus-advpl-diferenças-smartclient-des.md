---
article_id: 28252960583703
category: ADVPL - Relatório
content_hash: 22dc80243f074bdb1a02601966952721f58eb9e42b0445b0117addc0a0ef7f70
fetched_at: '2026-06-28T22:40:22.971726+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Diferenças SmartClient
  DeskTop e SmartClient HTML (WebApp)
type: support-article
updated_at: '2025-01-07T13:45:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28252960583703-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Diferen%C3%A7as-SmartClient-DeskTop-e-SmartClient-HTML-WebApp
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28252965980183)*Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**  
Quais as funções e componentes não suportados ou com comportamento diferenciado entre as versões HTML e Desktop?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**As funções e Classes com diferenças de comportamento são:**

* **Funções**

[CpyS2T](https://tdn.totvs.com/display/tec/CpyS2T)  
[CpyT2S](https://tdn.totvs.com/display/tec/CpyT2S)  
[WinExec](https://tdn.totvs.com/display/tec/WinExec)  
[ShellExecute](https://tdn.totvs.com/display/tec/ShellExecute)  
[ExecInClient](https://tdn.totvs.com/display/tec/ExecInClient)  
[ExecInDLLClose](https://tdn.totvs.com/display/tec/ExecInDLLClose)  
[ExecInDLLOpen](https://tdn.totvs.com/display/tec/ExecInDLLOpen)  
[ExecInDLLRun](https://tdn.totvs.com/display/tec/ExecInDLLRun)  
[ExeDLLRun2](https://tdn.totvs.com/display/tec/ExeDLLRun2)  
[ExeDLLRun3](https://tdn.totvs.com/display/tec/ExeDLLRun3)  
[AddCSSRule](https://tdn.totvs.com/display/tec/AddCSSRule)  
[CSSDictAdd](https://tdn.totvs.com/display/tec/CSSDictAdd)  
[ComputerName](https://tdn.totvs.com/display/tec/ComputerName)  
[GetComputerName](https://tdn.totvs.com/display/tec/GetComputerName)  
[GetRmtInfo](https://tdn.totvs.com/display/tec/GetRmtInfo)  
[GetRemoteType](https://tdn.totvs.com/display/tec/GetRemoteType)  
[Funções de Controle de Impressão](https://tdn.totvs.com/pages/viewpage.action?pageId=6063562)  
[Funções de Manipulação de arquivos, discos e IO](https://tdn.totvs.com/pages/viewpage.action?pageId=6063692)  
[GetCredential](https://tdn.totvs.com/display/tec/GetCredential)  
[CGetFile](https://tdn.totvs.com/display/tec/cGetFile)  
[GetClientIP](https://tdn.totvs.com/display/tec/GetClientIP)  
[SetKey](https://tdn.totvs.com/display/tec/SetKey+no+Webapp)

* **Componentes** :

[TIBrowser (descontinuado)](https://tdn.totvs.com/pages/viewpage.action?pageId=6063246)  
[TMediaPlayer (descontinuado)](https://tdn.totvs.com/pages/viewpage.action?pageId=29426503)  
[TMSGraphic (descontinuado)](https://tdn.totvs.com/pages/viewpage.action?pageId=6063262)  
[TMSPrinter (descontinuado](https://tdn.totvs.com/pages/viewpage.action?pageId=6063264))  
[TPageView (descontinuado)](https://tdn.totvs.com/pages/viewpage.action?pageId=6063273)  
[TOleContainer (descontinuado)](https://tdn.totvs.com/pages/viewpage.action?pageId=223930443)  
[TSVG](https://tdn.totvs.com/display/tec/TSVG)  
[TSystemTray (descontinuado)](https://tdn.totvs.com/pages/viewpage.action?pageId=26119165)  
[TSrvObject](https://tdn.totvs.com/display/tec/TSrvObject)  
[TWebEngine](https://tdn.totvs.com/display/tec/TWebEngine)

**Solução**  
 As funções acima são suportadas no SmartClient HTML(WebApp) apenas com a utilização do WebAgent, para mais informações [**clique aqui.**](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)

**Saiba mais**

**[Diferenças entre as versões HTML e Desktop](https://tdn.totvs.com/pages/viewpage.action?pageId=118885352#SmartClientHTMLDiferen%C3%A7asentreasvers%C3%B5esHTMLeDesktop-CpyS2T)**

[**TOTVS | WebAgent**](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)
