---
content_hash: a75e83102a8a1b9adcf324edf1e19d95262e5bc4ea2acfe9210b85b292f50f73
fetched_at: '2026-06-29T00:09:21.992987+00:00'
page_id: '422545940'
product: rm
source: tdn-rm
title: Bloco G (Livro ICMS-GI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545940
version: 3
---

**G001: Abertura do Bloco G**   
Preenchido pela rotina.

**G020: Guia de Informações Econômico-Fiscais**   
Preenchido pela rotina.

**G025: Documentos Registrados**   
Gerado um registro totalizando as operações de entrada e outro totalizando as operações de saídas, agrupando pelo código do modelo do documento, série e subsérie.

**G030: Cupons Registrados**   
Gerado um registro totalizando as operações de entrada e outro totalizando as operações de saídas, agrupando pelo código do modelo do documento, número série ECF e CRO. Serão considerados apenas lançamentos com código modelo de documento 2D.

**G050: Mapa-Resumo de Operações**   
Gerado registro diário mesmo que os valores sejam zerados.

**G400: ICMS - Consolidação por CFOP**   
Esse registro totaliza a movimentação do período selecionado na rotina, agrupando os valores pelo CFOP até o segundo nível, que é o nível fiscal. Serão selecionados apenas lançamentos associados a CFOP "Fiscal".

**G410: ICMS - Totalização das Operações**   
Esse registro totaliza a movimentação do período selecionado na rotina, agrupando os valores pela Origem/Destino selecionada no cadastro do CFOP.

**G420: ICMS - Saldos da Apuração**   
Considera os saldos apurados de acordo com o período selecionado na rotina.

**G430: ICMS - Totalização dos Ajustes da Apuração**   
Esse registro é gerado com os valores dos lançamentos de Outros Débitos/Créditos do período.

**G440: ICMS - Totalização das Obrigações a Recolher**   
Esse registro será gerado com as informações das guias geradas no período de apuração.

**G450: ICMS - Totalização das Operações Interestaduais**   
Totaliza as operações interestaduais.

**G460: ICMS - Subtotais por UF**   
Totaliza as operações do período por UF de Origem/Destino (DLAF.CODETD)

**G990: Encerramento do Bloco G**   
Preenchido pela rotina.
