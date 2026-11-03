---
article_id: 360015530791
category: Encargos
content_hash: f7a1d15ee7b4427a10d5f2a836f6d3bbe43b75d349a27372545b48a9d0781671
fetched_at: '2026-06-28T22:46:53.383566+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Número do PIS/PASEP/CI não classificado'
type: support-article
updated_at: '2025-03-13T11:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015530791-RH-RM-FOP-SEFIP-N%C3%BAmero-do-PIS-PASEP-CI-n%C3%A3o-classificado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**No módulo **Folha de Pagamento**, ao gerar o arquivo **SEFIP** e importar para o aplicativo, é apresentada a seguinte mensagem de erro: **300822 - NRO DO PIS PASEP NÃO CLASSIFICADO**.

![asfsafsafsa.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360010530152/asfsafsafsa.jpg)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois antes do processo de geração da **SEFIP** não foi realizada a rotina **Liberação de Flags de FGTS**.  
  
**Solução**1. Acesse **Encargos | Liberação de Flags FGTS**;2. Realize a geração da **SEFIP** novamente e importe para o aplicativo.
