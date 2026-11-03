---
article_id: 12397931782295
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9e5e72b1f3ad015d69a6eb84222642f29c29782969531cfec9eb9a996cb47533
fetched_at: '2026-06-28T22:42:00.907727+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 02    COD_INF_ITEM Código do item do registro C177?
type: support-article
updated_at: '2023-02-14T14:06:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12397931782295-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-02-COD-INF-ITEM-C%C3%B3digo-do-item-do-registro-C177
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o campo **02  COD\_INF\_ITEM Código do item do registro C177 (Complemento do Item)?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para gerar o **campo 02 COD\_INF\_ITEM** do **registro C177,** o sistema valida as informações do campo **Código Item -** **FT\_INFITEM,** conforme trecho abaixo do código fonte.  
  
**aAdd (aReg[nPos], (cAliasSFT)->FT\_INFITEM) //02 - COD\_INF\_ITEM**

O campo em questão é gatilhado com base no preenchimento do campo **Inf. item - F4\_INFITEM** do cadastro de **TES** utilizado na escrituração do documento fiscal.
