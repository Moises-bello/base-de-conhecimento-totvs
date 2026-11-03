---
article_id: 31120442597271
category: Inspeção de Processos (SIGAQIP)
content_hash: 77436efd57fe929dc409d6a276c2ba4fc3d5262e723e4d2baa0211a334a7ac94
fetched_at: '2026-06-28T22:42:25.758657+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help A010REVANT na rotina QIPA010
type: support-article
updated_at: '2025-04-03T14:15:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31120442597271-Manufatura-Linha-Protheus-SIGAQIP-Help-A010REVANT-na-rotina-QIPA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31120451583895) Tempo aproximado para leitura: **00:00:30 min****Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao tentar cadastrar uma especificação de produto na rotina **QIPA010 - Especificação de Produtos** é apresentado o *help* **A010REVANT - Revisão anterior é válida a partir de XXXX.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help* **A010REVANT** é exibido na rotina **QIPA010** quando já há revisão da especificação de produto com **Data de Início de Vigência** inferior à data preenchida na revisão atual.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. No campo **Início de Vigência** selecione uma **data superior ou igual** à data de vigência da última revisão da especificação de produto.
