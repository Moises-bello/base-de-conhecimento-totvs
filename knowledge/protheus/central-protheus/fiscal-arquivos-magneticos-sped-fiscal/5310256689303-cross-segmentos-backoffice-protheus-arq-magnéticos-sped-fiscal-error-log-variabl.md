---
article_id: 5310256689303
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: eb3acebd2a1bb740ebacf21859a7deed9b843daba558a4df1aa05cec78568c67
fetched_at: '2026-06-28T22:42:00.838516+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Arq. Magnéticos - SPED FISCAL - Error
  Log  -  variable does not exist CMODREF on REGC500(SPEDFISCAL.PRW) 12/01/2022 19:10:31
  line : 9425'
type: support-article
updated_at: '2022-07-25T16:58:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5310256689303-Cross-Segmentos-Backoffice-Protheus-Arq-Magn%C3%A9ticos-SPED-FISCAL-Error-Log-variable-does-not-exist-CMODREF-on-REGC500-SPEDFISCAL-PRW-12-01-2022-19-10-31-line-9425
---

**Ocorrência**  
Ao gerar o Sped Fiscal no *layout* 16 é gerado o *Error Log* abaixo:

**variable does not exist CMODREF on REGC500(SPEDFISCAL.PRW)** 12/01/2022 19:10:31 line : 9425

**Ambiente**

Cross Segmento - TOTVS Backoffice (**Linha Protheus**) - A partir da versão **12.1.27.**  
  
  
**Causa**  
Ao preparar documentos de **Nota Fiscal Consumo Fornecimento de Gás (Código 28)** e **Nota Fiscal D'Água Canalizada (Código 29)** para entradas e saídas, ocorre o *Errorlog* da variável não encontrada  
  
**Solução**Para correção do erro é preciso aplicar o pacote de correção abaixo de acordo com a *release* utilizada:

12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1060092> ;

12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1060093> ;
