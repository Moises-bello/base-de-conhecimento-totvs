---
article_id: 4413951615511
category: Faturamento - Integrações
content_hash: 6950d456766849534ba1af9646dea90d0d23df31593da6b75bd96a22e456f74c
fetched_at: '2026-06-28T22:38:26.648439+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Fonte MATA410BO
  envia dois arquivos Json ao invés de um único
type: support-article
updated_at: '2021-11-23T18:36:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413951615511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Fonte-MATA410BO-envia-dois-arquivos-Json-ao-inv%C3%A9s-de-um-%C3%BAnico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Na integração via mensagem única, o fonte MATA410B realiza o envio de dois arquivos Json, um com a chave de transmissão da nota e outro sem.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Causa**As mensagens enviadas pelo fonte MATA410B tem o objetivo de comunicar, aos sistemas integrados via mensagem única, as atualizações de status dos pedidos incluídos.

A primeira mensagem enviada tem o objetivo de informar o faturamento do pedido, contendo apenas informações de faturamento, sem a chave de transmissão da nota.

A segunda mensagem tem o objetivo de informar a separação do produto para envio, ou seja, com a nota fiscal já emitida, essa possui a chave de transmissão à SEFAZ.   
  
**Solução**Para diferenciar as mensagens o sistema atribui valores diferentes à tag "Status", o pedido faturado possui a tag com a informação "Faturado", porém informando que a nota não foi transmitida, por isso sem a chave da NF-e:

![Sem_chave_NFe.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413946588183/Sem_chave_NFe.jpg)

A segunda mensagem possui o status "Empacotado", a informação da nota esta como "Transmitida" e a chave da NF-e é informada no arquivo:

![Com_chave_NFe.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413939412375/Com_chave_NFe.jpg)
