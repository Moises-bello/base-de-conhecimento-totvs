---
article_id: 4403752784663
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: d07f2c4194379d0f6fce9a804ce1ee7643ae13bfc978c370e72362ffa8c56c62
fetched_at: '2026-06-28T22:39:19.328474+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: MP - FIS - Qual o relatório disponível que demostre as notas de entrada com
  ICMS Complementar (Diferencial de alíquotas)?
type: support-article
updated_at: '2023-09-12T17:59:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403752784663-MP-FIS-Qual-o-relat%C3%B3rio-dispon%C3%ADvel-que-demostre-as-notas-de-entrada-com-ICMS-Complementar-Diferencial-de-al%C3%ADquotas
---

**Dúvida**

Qual o relatório disponível que demostre as notas de entrada com ICMS Complementar (Diferencial de alíquotas)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Solução**

Atualmente está disponível o relatório FISR004, o relatório foi desenvolvido com o intuito de demonstrar as notas de entrada com ICMS Complementar.

Serão consideradas as informações aonde o campos FT\_ICMSCOM esteja maior que zero, e campo FT\_ENTRADA esteja entre o período selecionado nas perguntas iniciais.

### 

### Campos demonstrados

Emissão: Campo FT\_ENTRADA

Nota Fiscal - Campo FT\_NFISCAL

Série: Campo FT\_SERIE

Fornecedor: Campo FT\_CLIEFOR

Loja: Campo FT\_LOJA

Nome Fornecedor: Campo A2\_NREDUZ

CNPJ: Campo A2\_CGC

UF: Campo A2\_EST

Valor: Campo FT\_VALCONT

Base de ICMS: Campo FT\_BASEICM

Valor de ICMS: Campo FT\_VALICM

ICMS Complementar: Campo FT\_ICMSCOM

Observações: Campo FT\_OBSERV

Informações adicionais:

https://tdn.totvs.com/pages/releaseview.action?pageId=697256674
