---
article_id: 17271067888023
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 9c8f4c590a3147ded14836c94a8e1f126e0f7eca23cdbf3611e5c0124a171ce8
fetched_at: '2026-06-28T22:38:57.016311+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 - argument
  #0 error, expected N->L, function dbgoto on A261ESTORN(MATA261.PRX)'
type: support-article
updated_at: '2023-09-04T20:38:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17271067888023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-argument-0-error-expected-N-L-function-dbgoto-on-A261ESTORN-MATA261-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17271097485975) Tempo aproximado para leitura: **00:01:39 min****Ocorrência**Ao tentar estornar uma Transferência (MATA261) ocorre o error.log: **"*argument #0 error, expected N->L, function dbgoto on A261ESTORN(MATA261.PRX)"***

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Normalmente este error.log ocorre em ambientes que possuem o Ponto de Entrada ***[MA261IN](https://tdn.totvs.com/display/public/PROT/MA261IN+-+Preenche+valores+de+campos+na+tela+de+estorno)***  
 com customizáveis dentro do mesmo. Exemplo abaixo:   
![](https://totvssuporte.zendesk.com/attachments/token/wIi7hi7ygkLTHKUKWLBVmT4PM/?name=image.png)  
  
**Solução**

Para solução paliativa, desabilite-o os customizáveis presentes no ambiente.

Procedimentos para desativar as customizações:  
1 - [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como desabilitar customizações através do catálogo de personalização do Configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-atrav%C3%A9s-do-cat%C3%A1logo-de-personaliza%C3%A7%C3%A3o-do-Configurador-)

2 - E insira também a chave IXBLOG = NORUN no Appserver do Protheus.

Posteriormente, é recomendável reavaliar as customizações presentes no Ponto de Entrada ***[MA261IN](https://tdn.totvs.com/display/public/PROT/MA261IN+-+Preenche+valores+de+campos+na+tela+de+estorno)*** a fim de que o error.log não ocorra mais:

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
