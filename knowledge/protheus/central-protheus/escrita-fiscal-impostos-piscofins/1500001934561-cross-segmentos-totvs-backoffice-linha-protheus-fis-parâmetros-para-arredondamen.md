---
article_id: 1500001934561
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 08002d7f94374ad748f42b038575834a9ffd699f6ef2793e5c98ca6f6080c275
fetched_at: '2026-06-28T22:39:36.830664+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Parâmetros para
  arredondamento de PIS e COFINS apuração
type: support-article
updated_at: '2024-03-22T13:15:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001934561-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Par%C3%A2metros-para-arredondamento-de-PIS-e-COFINS-apura%C3%A7%C3%A3o
---

**Dúvida**Quais são os parâmetros de arredondamento PIS COFINS apuração?  
  
**Ambiente**  
Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**Para realizar a configuração de **arredondamento** de **PIS** e **COFINS** é necessário configurar os parâmetros abaixo;

1 - Verifique no **Configurador** os **parâmetros**:

**MV\_RNDSOBR** = Indica se no truncamento dos impostos, o valor referente a terceira casa decimal (sobras) continuam a ser consideradas (.T.), ou não (.F.);   
**MV\_RNDPS2** = Informe o critério de arredondamento do PIS de apuração. As opções válidas são: .T. arredonda, .F trunca;  
**MV\_RNDCF2** = Informe o critério de arredondamento do COFINS de apuração. As opções validas são: .T. arredonda, .F. trunca;
