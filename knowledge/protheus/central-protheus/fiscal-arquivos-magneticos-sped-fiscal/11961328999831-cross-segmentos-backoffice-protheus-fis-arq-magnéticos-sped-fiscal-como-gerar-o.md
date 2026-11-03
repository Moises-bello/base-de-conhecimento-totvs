---
article_id: 11961328999831
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: aedda4c15fb4023b31dc63345d567d67c5278a2557afc1006a60d5f84b4e4535
fetched_at: '2026-06-28T22:42:01.204876+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro C175 em notas de entrada no Sped Fiscal?
type: support-article
updated_at: '2023-02-01T19:29:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11961328999831-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C175-em-notas-de-entrada-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao gerar o Sped Fiscal o registro **C175** - **Operações com Veículos novos** não é apresentado.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Primeiramente configure o produto junto ao parâmetro **MV\_VEICNV*****.***

***![MV_VEICNV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414750781719/MV_VEICNV.gif)***

Preencha no cadastro de produto no campo *Grupo* ***"*****B1\_GRUPO*****"*** o conteúdo informado no parâmetro **MV\_VEICNV*****.***

***![B1_GRUPO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414751382295/B1_GRUPO.gif)***

Faça o processo de escrituração da nota conforme a necessidade da empresa.

Após, acesse "**Complementos Fiscais**" da nota "**Veículos Automotores**" e alimente-os os campos da tabela **CD9**:

![veiculo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414744947607/veiculo.gif)

Após o processo informado, gere o arquivo do Sped Fiscal onde será apresentado o registro:

![](https://totvssuporte.zendesk.com/attachments/token/W52rP3DeoscSRIkJyQMBTDjEr/?name=image.png)
