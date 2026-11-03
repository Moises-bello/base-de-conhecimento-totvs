---
article_id: 360024253612
category: ADVPL - Classe e Função
content_hash: b5bde4b0beeb4f2e993ea63f8e4639025518c4eb24bb741b1a900549c96797ec
fetched_at: '2026-06-28T22:40:14.581904+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe FWMSPrinter
type: support-article
updated_at: '2021-09-30T21:20:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024253612-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWMSPrinter
---

**Dúvida**Quanto a geração automática (sem INTERFACE) de arquivos PDF gostaríamos de saber qual é a classe de relatórios recomendada pela Totvs para que seja criada esta solução?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**

```
lAdjustToLegacy := .F.   
lDisableSetup  := .T.  
  
oPrinter := FWMSPrinter():New("Danfe.rel", IMP_PDF, lAdjustToLegacy, , lDisableSetup)// Ordem obrigátoria de configuração do relatório  
oPrinter:SetResolution(72)  
oPrinter:SetPortrait()  
oPrinter:SetPaperSize(DMPAPER_A4)   
oPrinter:SetMargin(60,60,60,60) // nEsquerda, nSuperior, nDireita, nInferior   
oPrinter:cPathPDF := "c:\directory\" // Caso seja utilizada impressão em IMP_PDF
```

**Saiba Mais  
[FWMsPrinter](https://tdn.totvs.com/display/public/PROT/FWMsPrinter)**
