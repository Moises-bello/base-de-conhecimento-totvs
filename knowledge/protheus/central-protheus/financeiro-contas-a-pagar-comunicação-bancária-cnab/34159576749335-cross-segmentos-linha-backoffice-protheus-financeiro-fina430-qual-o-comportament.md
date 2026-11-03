---
article_id: 34159576749335
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 0baec6eac60227fb724cd3c9b60be1903d8926cbff010a740ffb6d083ecf795f
fetched_at: '2026-06-28T22:37:55.112780+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - Financeiro - FINA430 - Qual o
  comportamento do parâmetro MV_DTCNBXP no retorno CNAB
type: support-article
updated_at: '2025-08-13T18:49:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34159576749335-Cross-Segmentos-Linha-BackOffice-Protheus-Financeiro-FINA430-Qual-o-comportamento-do-par%C3%A2metro-MV-DTCNBXP-no-retorno-CNAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34159576725015) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Qual o comportamento do parâmetro **MV\_DTCNBXP** no retorno **CNAB**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O parâmetro **MV\_DTCNBXP** determina a data de contabilização online para as baixas a pagar do financeiro.

Porém, no retorno **CNAB** esse parâmetro não será acatado, conforme documentação oficial o mesmo tem relevância somente para as rotinas:  **FINA080**, **FINA090 e FINA091.**

**Saiba mais:** [**Utilização do parâmetro MV\_DTCNBXP**](https://tdn.totvs.com/pages/releaseview.action?pageId=620785310)
