---
article_id: 360044719494
category: MDe - Manifesto do Destinatario
content_hash: a0cf561249a539ef44930f649d2968010d7b97334559b7b116ce75c3d647816f
fetched_at: '2026-06-28T22:40:09.265489+00:00'
product: protheus
section_id: 1500001549162
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDE - Manifesto
  do destinatário 2020.001
type: support-article
updated_at: '2025-06-10T18:18:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044719494-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDE-Manifesto-do-destinat%C3%A1rio-2020-001
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2020.001 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**

Para a adequação à Nota Técnica **2020.001 Versão 1.50**.  
  
O prazo previsto para a Nota Técnica **2020.001 v1.50** é:  
Ambiente de Homologação (ambiente de teste das empresas): **01/07/2024**Ambiente de Produção: **01/08/2024****1. Atualização do ambiente TSS**Atualizar RPO de acordo com a release do seu TSS:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)  
  
Após os ajustes da NT 2020.001, agora é possível o destinatário registrar até 2 (dois) eventos de cada manifestação conclusiva por NF-e:

**Confirmação da Operação;**  
**Desconhecimento da Operação**  
**Operação não realizada.**Porém, somente terá validade a última manifestação registrada, exemplo: o destinatário pode confirmar uma operação, depois desconhecê-la e por fim confirmá-la novamente.

Caso seja realizado 2 eventos de Confirmação de operação e 2 de Desconhecimento ou operação não realizada, no monitoramento ficará da seguinte forma:

![image-2024-7-18_8-4-33.png](https://tdn.totvs.com/download/attachments/857579529/image-2024-7-18_8-4-33.png?version=1&modificationDate=1721301066750&api=v2)

Podemos observar que o segundo envio de cada evento o final do ID ficará com o numero 2.

E por fim, se for realizado o terceiro envio o TSS irá travar o envio para SEFAZ e retornará a seguinte mensagem:

![image-2024-7-18_9-54-48.png](https://tdn.totvs.com/download/attachments/857579529/image-2024-7-18_9-54-48.png?version=1&modificationDate=1721307288380&api=v2)

Importante

O ambiente de produção entrará em vigor no dia 01/08/2024, até está data, caso os clientes realizem o envio de um evento conclusivo com mais de uma ocorrência, a SEFAZ irá retornar a seguinte rejeição: "Rejeição: O numero de sequencia do evento informado e maior que o permitido".

A partir da data informada os clientes conseguirão registrar ate 2 ocorrências de cada evento conclusivo.

Para mais informações:

<https://tdn.totvs.com/pages/viewpage.action?pageId=857579529>

<https://tdn.totvs.com/pages/viewpage.action?pageId=857575538>
