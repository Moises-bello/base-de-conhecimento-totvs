---
article_id: 360060554134
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: f7efffbb746c476713bc776599f5e5472fc5631eac417d881d0ff0279ea780d5
fetched_at: '2026-06-28T22:39:36.989695+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: MP - FIS - PARÂMETRO ARREDONDAMENTO PIS COFINS RETENÇÃO
type: support-article
updated_at: '2021-04-28T14:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060554134-MP-FIS-PAR%C3%82METRO-ARREDONDAMENTO-PIS-COFINS-RETEN%C3%87%C3%83O
---

**Dúvida**  
Quais são os parâmetros de arredondamento PIS COFINS retenção?  
  
**Ambiente**  
Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**  
Para realizar a configuração de **arredondamento** de **PIS** e **COFINS** retenção é necessário configurar os parâmetros abaixo;

1 - Verifique no **Configurador** os **parâmetros**:

**MV\_RNDPIS** = Informe o critério de arredondamento do PIS de retenção. As opções validas são: .T. arredonda, .F. trunca;

**MV\_RNDCOF** = Informe o critério de arredondamento do COFINS de retenção. As opções validas são: .T. arredonda, .F. trunca; 

**MV\_RNDCSL** = Informe o critério de arredondamento da CSLL de retenção. As opções válidas são: .T. arredonda, .F. trunca; 

Mais informações no link abaixo:

https://tdn.totvs.com/pages/releaseview.action?pageId=6076816
