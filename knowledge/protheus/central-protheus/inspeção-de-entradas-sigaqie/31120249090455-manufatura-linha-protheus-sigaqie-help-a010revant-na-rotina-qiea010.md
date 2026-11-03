---
article_id: 31120249090455
category: Inspeção de Entradas (SIGAQIE)
content_hash: 3b714dc4df45dcedf7d4d6d588ad1c08110d3f9830e3634d55841e9f8eb37935
fetched_at: '2026-06-28T22:42:26.999168+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help A010REVANT na rotina QIEA010
type: support-article
updated_at: '2025-04-03T14:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31120249090455-Manufatura-Linha-Protheus-SIGAQIE-Help-A010REVANT-na-rotina-QIEA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31120253595799) Tempo aproximado para leitura: **00:00:30 min****Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao tentar cadastrar uma especificação de produto na rotina **QIEA010 - Especificação de Produtos** é apresentado o *help* **A010REVANT - Revisão anterior é válida a partir de XXXX.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* **A010REVANT** é exibido na rotina **QIEA010** quando já há revisão da especificação de produto com **Data de Início de Vigência** igual ou inferior à data preenchida na revisão atual.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. No campo **Início de Vigência** selecione uma **data superior** à data de vigência da última revisão da especificação de produto.
