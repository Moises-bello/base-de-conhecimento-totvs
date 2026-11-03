---
article_id: 4421007160855
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 42cd60b91459a75e42f69e450318c1547cd83df7c3f31f3ef8adf81589373119
fetched_at: '2026-06-28T22:42:03.732829+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Registro C100 Situação
  Extemporânea documento de Saída
type: support-article
updated_at: '2022-01-31T20:47:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421007160855-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Registro-C100-Situa%C3%A7%C3%A3o-Extempor%C3%A2nea-documento-de-Sa%C3%ADda
---

**Dúvida**Como configurar o sistema para gerar o registro C100 do sped fiscal com a situação 01 extemporânea?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para configurar no sped fiscal registro **C100** Campo **06 COD\_SIT** **= 01 extemporânea** é necessário realizar as seguintes configurações:  
  
Preencher o campo **Extemporânea** "**CDT\_SITEXT" = R** e informar a data no campo **Data Recebimento** "**CDT\_DTAREC"** no complemento do documento fiscal;

![Screenshot_2.png](https://tdn.totvs.com/download/attachments/645491391/Screenshot_2.png?version=1&modificationDate=1634836802307&api=v2)

Mais informações no documento abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=645491391>
