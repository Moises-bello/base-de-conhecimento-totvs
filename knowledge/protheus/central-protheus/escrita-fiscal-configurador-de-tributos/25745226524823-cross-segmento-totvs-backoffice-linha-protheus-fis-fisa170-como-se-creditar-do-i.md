---
article_id: 25745226524823
category: Escrita Fiscal - Configurador de Tributos
content_hash: 224833ce3208fcece659579eee63d484e420624e868364cc82a9f202b66edd75
fetched_at: '2026-06-28T22:39:17.499944+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como se
  creditar do ICMS para as compras do CST 61?
type: support-article
updated_at: '2024-12-05T18:43:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25745226524823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-se-creditar-do-ICMS-para-as-compras-do-CST-61
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25745182101271) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como se creditar do ICMS para as compras do CST61?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**O credito do ICMS sobre os combustíveis do CST 61 conforme a orientação

Conforme [Nota Orientativa 01/2023 - ICMS Monofásico - setor de combustíveis](http://sped.rfb.gov.br/pagina/show/7176), os campos abaixo passam a ter tratativas especificas para notas com produtos monofásicos e CSTs 53 e 61:  
![](https://tdn.totvs.com/download/attachments/652398035/image-2024-5-27_14-43-5.png?version=1&modificationDate=1716831786093&api=v2)  
Para mais informações sobre como configurar os movimentos para calculo no Protheus, consulte a documentação [CFGTRIB - Cálculo de ICMS Monofásico Lei Complementar 192/2022](https://tdn.totvs.com/pages/viewpage.action?pageId=765332384).

MV\_estado = SP

Fornecedor = SP

TES

calcula icms = não

Lfiscal icms = não

CFOP = 1652

CST= 61

Quantidade = 1750 litros

valor unitário = 5,76

Valor do icms monofasico = 2.474,33

Configuração pelo FISA170

ID tributo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25745226506519)

Cadastro dos Perfis

* [2.2.1 Perfis](https://tdn.totvs.com/pages/releaseview.action?pageId=765332384#CFGTRIBC%C3%A1lculodeICMSMonof%C3%A1sicoLeiComplementar192/2022-2.2.1Perfis)

Regra de Base de Calculo  
![](https://totvssuporte.zendesk.com/attachments/token/yVsgan8RaSIhsbN8dexrFy4ew/?name=image.png)  
   
Regra de Alíquota  
![](https://totvssuporte.zendesk.com/attachments/token/Z3JKorwcfI4sDLBga9A1HAWiG/?name=image.png)  
   
Regra de Escrituração  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307741457047)  
   
   
Regra de Calculo Documentos Fiscais  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307750645655)  
![](https://totvssuporte.zendesk.com/attachments/token/FsFeHtNlAxSKlaqsWJevyoFqU/?name=image.png)  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307750651799)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307741468823)  
 Após salvar a regra de Calculo documentos fiscais, entrar para alterar a coluna ( outros ) 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307750656535)  
   
   
Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307741472535)

Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307750661911)  
Apuração do ICMS   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307741480343)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28307741481495)

Regra de escrituração de acordo com o boletim 

<https://tdn.totvs.com/pages/releaseview.action?pageId=889121120>
