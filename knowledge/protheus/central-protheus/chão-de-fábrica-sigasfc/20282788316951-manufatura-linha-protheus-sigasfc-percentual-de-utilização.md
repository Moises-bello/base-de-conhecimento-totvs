---
article_id: 20282788316951
category: Chão de Fábrica (SIGASFC)
content_hash: 902c9f7d91a8228812b1ffb640b44f5218345a0c9995fe55dcb9a29401235d82
fetched_at: '2026-06-28T22:42:49.881010+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Percentual de utilização
type: support-article
updated_at: '2024-01-03T11:55:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20282788316951-Manufatura-Linha-Protheus-SIGASFC-Percentual-de-utiliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20282788314519) Tempo aproximado para leitura: **00:00:59 min** **Dúvida**Como é calculado o percentual de utilização na rotina **SFCC580 - Gerencial de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Solução**O percentual de utilização é o número de horas produtivas do período dividido pela número de horas em que o recurso esteve disponível menos as paradas que não alteram eficiência e que foram selecionadas na aba **Parâmetros** do **SFCC580.**  
  
**Exemplo**Se o recurso está disponível 24 horas, de acordo com o calendário, e no intervalo teve 1,5 apontada como parada que altera eficiência, 1 hora de parada que não altera eficiência e 2 horas produtivas .   
(2/(24-1))\*100 =   
(2/23)\*100 =   
0,086956\*100=  
8,6956
