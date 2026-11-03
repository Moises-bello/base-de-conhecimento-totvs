---
article_id: 31996414541975
category: esocial - Periódicos
content_hash: eb2c79c265a5f035d0a36b9d7380976a767418a91f82ce8efa3b1116542f7e79
fetched_at: '2026-06-28T22:47:09.354060+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Erro de Schema nrDoc na transmissão dos eventos S-2299/S-1200
  com o Governo
type: support-article
updated_at: '2026-05-26T19:31:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31996414541975-RH-RM-FOP-eSocial-Erro-de-Schema-nrDoc-na-transmiss%C3%A3o-dos-eventos-S-2299-S-1200-com-o-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31996382006679) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
Ao transmitir S-2299/S-1200 ao Governo é apresentada a mensagem **Erro de schema:** **Element '{http://www.esocial.gov.br/schema/evt/evtDeslig/v\_S\_01\_03\_00}nrDoc':[facet 'pattern'] The value '' is not accepted by the pattern '\d{8,12}'.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre devido aos schemas do TSS estarem desatualizados, não conforme com os schemas da versão do leiaute S-1.3 NT 03/2025, onde estes, aceitam na tag nrDoc 15 dígitos para informar número do contrato do empréstimo do Crédito do Trabalhador.  
  
**Solução**  
Siga as orientações da documentação abaixo para atualizar os schemas do TSS, e após conclusão, reenviar o evento S-1200/S-2299.

[Cross Segmentos - TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)
