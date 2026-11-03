---
article_id: 360034751473
category: Escrita Fiscal - Impostos - ICMS
content_hash: f0cc2ea164a3b2494710f6b48e5dbddd3d13e9c2196ec17b7d4ad4fc7b7dd0ba
fetched_at: '2026-06-28T22:39:25.966961+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Habilitar os Campos
  Cod. Reflexo (F3K_CODREF) e Valor (F3K_VALOR) Na Rotina FISA140 - Itens X Cod. Val.
  Declaratórios '
type: support-article
updated_at: '2023-03-08T17:09:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034751473-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Habilitar-os-Campos-Cod-Reflexo-F3K-CODREF-e-Valor-F3K-VALOR-Na-Rotina-FISA140-Itens-X-Cod-Val-Declarat%C3%B3rios
---

**Dúvida**Qual a configuração para ser apresentado os campos Cod. Reflexo (F3K\_CODREF) e Valor (F3K\_VALOR) na rotina FISA140 - Itens X Cod. Val. Declaratórios?  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para visualizar os campos Cod. Reflexo (F3K\_CODREF) e Valor (F3K\_VALOR) na rotina FISA140 - Itens X Cod. Val. Declaratórios, será necessário configurar o parâmetro MV\_GIAEFD conforme abaixo:

**MV\_GIAEFD**= .F. - Será apresentado na rotina Itens X Cod. Val. Declaratórios o campo Cod. Reflexo (F3K\_CODREF). 

**MV\_GIAEFD**= .T. - Será apresentado na rotina Itens X Cod. Val. Declaratórios o campo Valor (F3K\_VALOR).

Abaixo link contendo documentação completa referente a rotina FISA140 Itens X Cod. Val. Declaratórios:

<http://tdn.totvs.com/pages/releaseview.action?pageId=286029741>
