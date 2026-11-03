---
article_id: 40778849105431
category: TOTVS Linha Logix
content_hash: e06a80430f5644f572e6019baa5c0aaa950e2a789a4032f4f1a096827e82453c
fetched_at: '2026-06-28T22:49:50.733747+00:00'
product: totvs
section_id: 360002878311
source: central-ciclo-vida
title: Cross Segmentos - Linha Logix- NFE - Rejeição 452 - Resposta assíncrona - tpResposta
  = 1 - para um lote contendo apenas uma única NF-e.
type: support-article
updated_at: '2026-05-27T19:34:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40778849105431-Cross-Segmentos-Linha-Logix-NFE-Rejei%C3%A7%C3%A3o-452-Resposta-ass%C3%ADncrona-tpResposta-1-para-um-lote-contendo-apenas-uma-%C3%BAnica-NF-e
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40778849093143) Tempo aproximado para leitura:  **00:01:05 min**  
  
**Ocorrência**  
Ao enviar a **NFe - Nota Fiscal Eletrônica**, a **SEFAZ - Secretaria da Fazenda** retorna a mensagem de **Rejeição** **452 - Resposta assíncrona (tpResposta = 1) para um lote contendo apenas uma única NF-e.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Logix) - Nota Fiscal Eletrônica (NFE) - Todas as versões  
  
**Causa**  
A **Rejeição 452** ocorre quando é solicitada a resposta **assíncrona - tpResposta = 1 -** para um lote contendo apenas uma única **NFe**.  
De acordo com as regras da **SEFAZ**, a solicitação assíncrona só é permitida para lotes com mais de uma **NFe**. Para lotes unitários, a transmissão deve ocorrer de forma **síncrona - tpResposta = 0**.  
  
**Solução**  
O ajuste para evitar essa rejeição será realizado nos aplicativos responsáveis pela transmissão da **NF-e**, como:  
  
**TSS – TOTVS Sped Service**  
**TC2.0 - Totvs Colaboração**  
  
**Cronograma de Implantação da SEFAZ**  
A **SEFAZ** definiu o seguinte cronograma para entrada da **Rejeição 452** em seus ambientes:  
  
**Homologação:** Junho/2025  
**Produção:** Outubro/2025  
  
Para contemplar essa nova exigência, se faz necessário a atualização do TSS, conforme orienta a documentação abaixo:

[Cross Segmentos - Linha Logix - NFE - Atualização do TOTVS Service SOA para a correta utilização do OBF40000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025034751-Cross-Segmentos-Linha-Logix-NFE-Atualiza%C3%A7%C3%A3o-do-TOTVS-Service-SOA-para-a-correta-utiliza%C3%A7%C3%A3o-do-OBF40000)  
   
**Importante**  
No Sistema **Logix** não há nenhuma alteração a ser realizada. O **ERP** continuará operando normalmente.
