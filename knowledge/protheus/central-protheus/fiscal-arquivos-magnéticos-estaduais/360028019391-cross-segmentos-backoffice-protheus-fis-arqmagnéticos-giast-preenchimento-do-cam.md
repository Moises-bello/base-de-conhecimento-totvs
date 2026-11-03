---
article_id: 360028019391
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 6d6df17e560a54157d27dc98c06a4870c1ddc832431a240addb548a2f20e83b3
fetched_at: '2026-06-28T22:42:11.655643+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIAST Preenchimento
  do campo Data de vencimento do ICMS devido a UF de destino (aba EC n° 87/15)
type: support-article
updated_at: '2022-08-18T13:54:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028019391-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIAST-Preenchimento-do-campo-Data-de-vencimento-do-ICMS-devido-a-UF-de-destino-aba-EC-n-87-15
---

**Dúvida**  
Como preencher o campo **Data de Vencimento do ICMS devido à UF de Destino**, dentro da aba **EC N° 87/15** da **GIAST**?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**A **GIAST** é gerada pela rotina pela **MATA950**. A informação para preencher o campo **Data de Vencimento do ICMS devido à UF de Destino** (dentro da aba EC N° 87/15) da **GIAST** vem da guia de recolhimento referente ao **Difal** gerada através da apuração, pelo campo **F6\_DTVENC** - Vencimento.  
Para que a data do vencimento seja preenchida no registro **A4** referente ao vencimento do **Difal**, o campo **F6\_DTVENC** - Vencimento, deverá estar preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027881871/mceclip0.png)
