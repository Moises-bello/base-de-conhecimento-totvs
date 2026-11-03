---
article_id: 8210243303575
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e43673af9cd0b3c68d79fc1aa7e781244ef0d310e4862eeee67a661625182d36
fetched_at: '2026-06-28T22:42:02.444137+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED Fiscal
  - Registros C197/D197 não gera, mesmo havendo dados na tabela CDA
type: support-article
updated_at: '2022-08-16T18:59:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8210243303575-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-Fiscal-Registros-C197-D197-n%C3%A3o-gera-mesmo-havendo-dados-na-tabela-CDA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o Sped Fiscal  não é gerado o registro C197/D197 mesmo havendo dados na tabela CDA.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir da versão 12.1.25  
  
**Causa**  
Esse incidente ocorre pois o campo **CDA\_IFCOMP** está em branco. O campo em questão é alimentado com base no campo **Obs.Lanc.Fis - CC7\_IFCOMP** na amarração ao **cadastro de TES**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8210042981143/mceclip0.png)

**Solução**Para os novos lançamentos basta incluir a informação no **cadastro de TES** e utilizar este cadastro na escrituração.

Quanto às Notas Fiscais já lançadas, além de proceder com o preenchimento do campo é preciso realizar o **Reprocessamento** das notas no caminho abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/zxqRSyblw5GanolfUGq1bdFg1/?name=image.png)
