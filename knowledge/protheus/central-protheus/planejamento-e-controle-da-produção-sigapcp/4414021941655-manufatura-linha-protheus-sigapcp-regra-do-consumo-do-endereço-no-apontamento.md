---
article_id: 4414021941655
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9cfd904b2afb98ee1be1f8c18d89901a189c7555397b94e9b69285d0e14ba2f5
fetched_at: '2026-06-28T22:42:45.840113+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Regra do consumo do endereço no apontamento
type: support-article
updated_at: '2024-04-23T16:22:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414021941655-Manufatura-Linha-Protheus-SIGAPCP-Regra-do-consumo-do-endere%C3%A7o-no-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Qual a regra utilizada pelo Sistema para definir de qual endereço será utilizado o saldo do componente no momento do apontamento?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Quando o empenho é realizado sem informar o endereço o Sistema buscará o saldo disponível do endereço no momento do apontamento.  
Caso tenha mais de um endereço com saldo disponível será considerado, respeitando a sequência: **BE\_PRIOR - Prioridade** **+** **BE\_LOCALIZ - Endereço**
