---
article_id: 41328660755735
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: cac93569185e040af8ef0d27a9e7c3bcbee0446dfb2a8444329c8cca5bb80387
fetched_at: '2026-06-28T22:42:40.894625+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloco K - O campo DT_SAIDA deve estar
  compreendido no período da ordem de produção
type: support-article
updated_at: '2026-06-18T20:52:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41328660755735-Manufatura-Linha-Protheus-SIGAPCP-Bloco-K-O-campo-DT-SAIDA-deve-estar-compreendido-no-per%C3%ADodo-da-ordem-de-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41328660722327) Tempo aproximado para leitura: **00:00:56 min**  
  
**Ocorrência**  
Ao processar o Bloco K ocorre a mensagem **O campo DT\_SAIDA deve estar compreendido no período da ordem de produção. Caso não tenha sido informada a data final da produção, esse campo deve ser maior ou igual a DT\_INI\_OP.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
Esta mensagem ocorre quando a data de encerramento da **OP - Ordem de Produção** registrada no campo **C2\_DATRF - Data Encerramento** é anterior à data do último apontamento da **OP** registrada no campo **D3\_EMISSAO - Data Emissão**.  
  
**Solução**  
Para solucionar essa ocorrência, verifique qual é a data do último apontamento desta **OP** e altere o conteúdo do campo **C2\_DATRF** com a data do último apontamento.
