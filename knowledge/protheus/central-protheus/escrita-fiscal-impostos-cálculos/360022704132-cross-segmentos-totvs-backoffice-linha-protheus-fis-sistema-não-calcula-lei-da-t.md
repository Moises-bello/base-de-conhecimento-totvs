---
article_id: 360022704132
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 11318172a810e09ea59363e26627582585b3fdc9219a0b7e3c80136243855e6f
fetched_at: '2026-06-28T22:39:31.147874+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Sistema não calcula
  Lei da Transparência (IBPT)
type: support-article
updated_at: '2025-11-14T22:03:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022704132-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Sistema-n%C3%A3o-calcula-Lei-da-Transpar%C3%AAncia-IBPT
---

**Dúvida**

O sistema não está gerando as informações de valor aproximado de tributos (IBPT).

Os campos abaixo não são preenchidos ao finalizar a nota.  
F2\_TOTIMP, F2\_TIPIMP, F2\_TOTMUN, F2\_TOTEST, F2\_TOTFED  
D2\_TOTMUN, D2\_TOTEST, D2\_TOTFED, D2\_TOTIMP.

**Ambiente**Protheus - Fiscal - A partir da versão 11.80   
  
   
**Solução**

Para que ocorra o preenchido na/s tabela/s SF2 e/ou SD2 são:

* 1 - Os parâmetros abaixo configurados de forma correta.  
  MV\_FISCTRB  
  MV\_ENTETRB  
  MV\_FISALCT

* 2 - O produto em questão utilizado possuir o campo B1\_POSIPI(NCM) preenchido ou caso seja serviço B5\_NBS estar preenchido;

* 3 - O NCM ou NBS preenchido, deve existir na tabela CLK;

* 4 - O registro na tabela CLK, teve ser referente ao Estado Origem que está sendo efetuando a venda (CLK\_UF) e dentro da data de vigência (CLK\_DTINIV / CLK\_DTFIMV);

* 5 -  O Cliente em questão deve Consumidor Final (A1\_TIPO = F).

Para mais informações, link abaixo poderá auxiliar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=145365032>
