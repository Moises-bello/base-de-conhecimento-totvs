---
article_id: 26078355803031
category: Financeiro - Contas a Receber
content_hash: 899b24c81d883c4b954c157800f7c0683ec1b0ccfb191306c10e06bb06d98910
fetched_at: '2026-06-28T22:38:12.723195+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN -  ExecAuto FINA330 MaIntBxCR
  - Como deixar o mesmo histórico do ExecAuto igual ao da compensação manual.
type: support-article
updated_at: '2024-09-02T20:21:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26078355803031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-ExecAuto-FINA330-MaIntBxCR-Como-deixar-o-mesmo-hist%C3%B3rico-do-ExecAuto-igual-ao-da-compensa%C3%A7%C3%A3o-manual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26078347731735) Tempo aproximado para leitura: **00:00:10****min****Dúvida**Como deixar o mesmo histórico do ExecAuto igual ao da compensação manual.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
**Solução**Por legado compensação via ExecAuto e compensação manual são funções diferentes, dessa forma podem apresentar comportamentos e gravações distintas.  
  
Para que a compensação via ExecAuto tenha o mesmo comportamento que a compensação via tela é necessário ativar o parâmetro MV\_CMP330

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26078355793815)

Caso o parâmetro esteja com seu conteúdo igual a T (Verdadeiro), a compensação será realizada utilizando a rotina padrão do módulo Financeiro, onde existe todo o tratamento na forma da rotina manual.

Caso o parâmetro esteja com seu conteúdo igual a F (Falso - Padrão) o sistema segue da forma convencional, utilizando a rotina de compensação automática atual

**SAIBA MAIS:**

**[Utilização do parâmetro MV\_CMP330](https://tdn.totvs.com/pages/releaseview.action?pageId=631323696)**

**[Compensação contas a receber- FINA330 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=505768648)**

**[Rotina automática de Compensação Contas a Receber - FINA330 (MaIntBxCr)](https://tdn.totvs.com/pages/releaseview.action?pageId=631326214)**
