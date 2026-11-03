---
article_id: 1500008686282
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 07ccc706b4b81d952bf251d574fbc1dd9ca959332807195f96d56866b02db9ca
fetched_at: '2026-06-28T22:42:40.814933+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamento de produção por produto
type: support-article
updated_at: '2022-11-30T02:13:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008686282-Manufatura-Linha-Protheus-SIGAPCP-Apontamento-de-produ%C3%A7%C3%A3o-por-produto
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:40 min  
  
Dúvida**Como realizar o **apontamento de produção** por **produto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O **apontamento de produção** por **produto** não exigirá informar o número da **OP - Ordem de Produção** ao efetuar um **apontamento** e pode ser realizado através da rotina **MATA250 - Produção Simples**, quando o **produto** está parametrizado para isso, através do campo **B1\_APOPRO - Ap. p/ Prod.**  
  
Dessa forma, quando não for informado o número da **OP** no **apontamento**, o Sistema irá selecionar automaticamente as **OPs** disponíveis conforme configuração do parâmetro **MV\_OPAPOPR - Gerar ordem de produção no apontamento por produto**.
