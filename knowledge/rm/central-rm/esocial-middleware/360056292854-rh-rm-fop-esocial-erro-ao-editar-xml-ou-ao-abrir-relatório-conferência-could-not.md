---
article_id: 360056292854
category: eSocial - Middleware
content_hash: 0843c19b740a06cc010f8a78de657ba0e03d8612fa99f6c1ccce212f67d9bc05
fetched_at: '2026-06-28T22:47:05.627112+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao editar XML ou ao abrir relatório conferência:
  Could not load file or assembly ''CefSharp.Core.dll'' or one of this dependences'
type: support-article
updated_at: '2023-12-21T19:28:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056292854-RH-RM-FOP-eSocial-Erro-ao-editar-XML-ou-ao-abrir-relat%C3%B3rio-confer%C3%AAncia-Could-not-load-file-or-assembly-CefSharp-Core-dll-or-one-of-this-dependences
---

**Ocorrência**Ao realizar a edição de XML ou ao abrir o relatório Conferência INSS/FGTS ocorre o erro **Could not load file or assembly 'CefSharp.Core.dll' or one of this dependences**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este incidente ocorre por falta de componentes do Visual C++ necessários no ambiente para a correta execução do processo.  
  
**Solução**Para solucionar este incidente deverá possuir os pacotes Redistribuíveis do Visual C++ para Visual Studio superiores à versão 2013 e 2015 (vc\_redist.x86.exe e vc\_redist.x64.exe) disponíveis para *download* na página da *Microsoft*:

Visual C++ 2013  
- [vc\_redist.x86.exe](https://download.microsoft.com/download/2/E/6/2E61CFA4-993B-4DD4-91DA-3737CD5CD6E3/vcredist_x86.exe)  
- [vc\_redist.x64.exe](http://download.microsoft.com/download/7/b/a/7bafb681-05f8-4d13-98af-9bc6c93b3536/vcredist_x64.exe)

Visual C++ 2015   
- [vc\_redist.x86.exe](https://aka.ms/vs/16/release/vc_redist.x86.exe)  
- [vc\_redist.x64.exe](https://aka.ms/vs/16/release/vc_redist.x64.exe)
