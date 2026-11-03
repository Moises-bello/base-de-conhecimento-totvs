---
article_id: 4416741712151
category: Escrita Fiscal - CIAP
content_hash: d93dc3c28aa20322b0792855d070e9dd179ce26ca42598114c8b9f1f4c3dffba
fetched_at: '2026-06-28T22:39:33.967114+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -Valor Zerado no Livro
  CIAP Após Realizar as Apropriações
type: support-article
updated_at: '2021-12-22T14:24:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416741712151-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valor-Zerado-no-Livro-CIAP-Ap%C3%B3s-Realizar-as-Apropria%C3%A7%C3%B5es
---

**Dúvida**Por que o valor do livro CIAP fica zerado mesmo após realizar as apropriações?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Ao emitir o livro CIAP modelo **C** deve ser respeitado o prazo de 1 ano ao incluir as informações nos parâmetros **Data Fiscal De** e **Data Fiscal Até**.

**Exemplo:**   
01/01/2011 a 31/12/2011 - Neste livro somente são impressas as informações referentes ao período de 12 meses de apropriação do bem.
