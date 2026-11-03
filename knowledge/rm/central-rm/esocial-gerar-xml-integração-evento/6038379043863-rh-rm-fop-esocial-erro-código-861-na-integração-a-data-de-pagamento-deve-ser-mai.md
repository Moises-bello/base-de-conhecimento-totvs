---
article_id: 6038379043863
category: eSocial - Gerar XML/ Integração Evento
content_hash: 8fb3017b19507013126c69f5d8d22086fa111f841344cb528cecf1d91b8051d8
fetched_at: '2026-06-28T22:47:12.270699+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 861 na integração: A data de pagamento
  deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho'
type: support-article
updated_at: '2024-06-26T15:08:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6038379043863-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-861-na-integra%C3%A7%C3%A3o-A-data-de-pagamento-deve-ser-maior-ou-igual-ao-m%C3%AAs-anterior-de-rescis%C3%A3o-do-contrato-de-trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao transmitir o evento S-1210 para o governo é retornado a inconsistência **Código do Erro: 861 -** **A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho.**

**![861.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6038328469655/861.PNG)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Conforme mensagem apresentada, a inconsistência geralmente é apresentada quando não foi enviado o evento **S-2299 (Desligamento)** anterior ao envio do evento **S-1210 (Pagamento da Remuneração).**  
  
**Solução**O erro 861 geralmente é apresentado devido à existência do erro 726. Dessa forma, para sanar a inconsistência,  deverá realizar as validações do erro 726 conforme artigo abaixo:  
     • [Validação dos erros 724 e/ou 726 no envio do evento S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025168831-RH-RM-FOP-eSocial-Valida%C3%A7%C3%A3o-dos-erros-724-e-ou-726-no-envio-do-evento-S-1210)
