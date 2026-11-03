---
article_id: 360033434834
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1baa5dfef306f514a6bce07e755b4e81d606600f311ea4231f24372d46f3d640
fetched_at: '2026-06-28T22:42:10.312395+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar a
  linha 026 da DAPIMG?
type: support-article
updated_at: '2022-08-17T20:04:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033434834-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-026-da-DAPIMG
---

**Dúvida**Como gerar a linha 026 da DAPIMG?  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Considerado através do registro de Entrada, nos casos em que:

* O campo **CFOP** do documento de entrada (**D1\_CF**) contenha: 2101/2102/2111/2113/2116/2117/2118/2120/2121/2122/2124/2125/2126/2401/2403/2501/2651/2652.
* O campo **D1\_CF** contenha = 2653 e No cadastro da TES o Campo**Credita ICM**S (**F4\_CREDICM** ) esteja diferente de Não.
* No cadastro da TES o Campo **Material de consumo** (**F4\_CONSUMO** diferente de **Sim**)ou SF4\_CONSUMO<>"S").
* No campo **D1\_CF** contenha o CFOP2949 e o campo **Tipo Docto.** (**D1\_TIPO**) Seja **Complemento de ICMS.**

Verificar as notas fiscais com as CFOPs para a linha 26, e analisar se os campos FT\_VALCONT e F3\_VALCONT onde os mesmos devem estar preenchidos com valores. Esse erro pode ocorrer quando existe valores na coluna de **ICMS**Outros/Isentos ou Tributado, mas não existe valor na coluna **Valor contábil**

Link: <http://tdn.totvs.com/display/public/PROT/DAP0019_Linha_026_da_DAPIMG>
