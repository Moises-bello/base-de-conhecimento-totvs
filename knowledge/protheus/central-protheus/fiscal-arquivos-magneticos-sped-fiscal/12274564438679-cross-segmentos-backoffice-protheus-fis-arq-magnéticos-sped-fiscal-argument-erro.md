---
article_id: 12274564438679
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: d65f421f5024891a5429f85a41325004fe45acc887c2f438eff8c927ff158654
fetched_at: '2026-06-28T22:42:01.033387+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - argument error in function Len() on REGC171(SPEDFISCAL.PRW)
type: support-article
updated_at: '2023-03-05T01:21:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12274564438679-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-argument-error-in-function-Len-on-REGC171-SPEDFISCAL-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar o Sped Fiscal ocorre o seguinte erro: **Error log: argument error in function Len() on REGC171(SPEDFISCAL.PRW)**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**O erro **argument error in function Len() on REGC171** ocorre devido a falta de preenchimento do campo **Tanque - CD6\_TANQUE** para determinada NF de entrada **Numero NF - CD6\_DOC**  
  
Através do pacote de correção abaixo, foi realizada correção da rotina para que não ocorra o error.log quando não houver conteúdo no campo **Tanque - CD6\_TANQUE**, porém, essa informação é obrigatória para geração do registro **C171 - Armazenamento de Combustível** conforme layout do Manual da EFD ICMS/IPI, sendo assim, caso não seja encontrada informação no referido campo, não haverá geração do **registro C171.**  
  
**Solução**

O pacote pode ser acessado no endereço:

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1095603>; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1095604>; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1095605>;
