---
article_id: 32419291127447
category: Financeiro
content_hash: 5be019e776ccdc3d54318cf5709c7ace89818478400c462037e052dd0daed708
fetched_at: '2026-06-28T22:38:04.195613+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - (FINA710)
  - Novo Gestor Financeiro não apresenta informações
type: support-article
updated_at: '2025-05-28T19:42:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32419291127447-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-Financeiro-FINA710-Novo-Gestor-Financeiro-n%C3%A3o-apresenta-informa%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32419307127063) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao acessar o **Novo Gestor Financeiro**, a tela não abre e não apresenta informações.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32419291116183)  
**Ambiente**Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - A partir do release 12.1.2310  
  
**Causa**Este incidente ocorre, devido à falha na leitura do front da tela do **Novo Gestor Financeiro** efetuado pela pasta **http-root** localizada na **Protheus\_data**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32419307127447)  
**Solução**

• Acesse localmente ou via FTP a pasta **Protheus\_data**. Localize a subpasta **http-root**.

• Renomeie a pasta **http-root** para **http-root.old**.  
• Reinicie todos os serviços do **Protheus**.  
• Após a reinicialização, acesse novamente o **Novo Gestor Financeiro (FINA710).**

**Saiba mais**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração e Funcionalidade do Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Configura%C3%A7%C3%A3o-e-Funcionalidade-do-Novo-Gestor-Financeiro)  
[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)
