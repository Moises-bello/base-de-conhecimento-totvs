---
article_id: 40314735280535
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: cfa34f0a106a9f5eee4b50a45eb5951bd24bd4a0afd00781cd09019ae385e024
fetched_at: '2026-06-28T22:42:42.096465+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Conceito do parâmetro MV_USATRT
type: support-article
updated_at: '2026-05-08T14:10:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40314735280535-Manufatura-Linha-Protheus-SIGAPCP-Conceito-do-par%C3%A2metro-MV-USATRT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40314735273111) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida:**  
Qual o conceito do parâmetro **MV\_USATRT - Habilitar/Desabilitar o uso do campo D4\_TRT na rotina de apontamento de produção a fim de evitar conflito com o produto WMS**?.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Quando o parâmetro **MV\_USATRT** está desativado, no momento de realizar a requisição dos componentes com base no empenho registrado na tabela **SD4 - Empenhos**, o Sistema busca o primeiro registro empenhado da tabela **SD4** para a **OP - Ordem de Produção** que está sendo apontada, e tenta suprir toda a necessidade da requisição com esse registro e somente após zerar o saldo desta sequência, busca o próximo registro empenhado.  
E quando o parâmetro **MV\_USATRT** está ativo, o Sistema considera todas as sequências do mesmo item simultaneamente no apontamento.   
  
**Exemplos**  
Para uma **OP** com quantidade planejada de 20 peças, foram gerados os empenhos na tabela **SD4** para o mesmo componente A onde:  
**D4\_TRT - Seq. Estrutura** de sequência 001 com quantidade de 10  
**D4\_TRT** de sequência 002 com quantidade de 10  
O apontamento será parcial com quantidade de 10 peças nesta **OP.**  
  
Com o parâmetro **MV\_USATRT = F**, o Sistema irá requisitar a quantidade de 10 peças na primeira sequência, ou seja, onde o campo **D4\_TRT** é igual à 001, será empenhado 10 peças.  
Com o parâmetro **MV\_USATRT = T**, o Sistema irá requisitar 5 unidades de cada sequência, mantendo a proporcionalidade do empenho, ou seja, para a sequência **D4\_TRT** igual à 001 irá requisitar a quantidade de 5 e para a sequência 002, a quantidade de 5.
