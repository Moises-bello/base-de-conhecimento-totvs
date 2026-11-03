---
article_id: 115011204548
category: ADVPL - Relatório
content_hash: 9cbbc1ff78cac759ba3e797a244b462a7997564548e609d9b6ba5e11dcf86858
fetched_at: '2026-06-28T22:40:22.791356+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Desabilitar impressão
  da página de parâmetros nos relatórios Treport
type: support-article
updated_at: '2022-06-21T17:41:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011204548-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Desabilitar-impress%C3%A3o-da-p%C3%A1gina-de-par%C3%A2metros-nos-relat%C3%B3rios-Treport
---

**Dúvida**Como desabilitar impressão da página de parâmetros nos relatórios?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Pode ser utilizado o método ShowParamPage - A Define que será impressa a página de parâmetros do relatório.

Exemplo

```
oReport := TReport():New........  
oReport:ShowParamPage()  
oReport:lParamPage := .F.
```

**Saiba mais**  
[ADV0002\_IMP\_TREPORT\_SHOWPARAMPAGE](http://tdn.totvs.com/display/PROT/ADV0002_IMP_TREPORT_SHOWPARAMPAGE)  
[TReport](https://tdn.totvs.com.br/display/framework/TReport)
