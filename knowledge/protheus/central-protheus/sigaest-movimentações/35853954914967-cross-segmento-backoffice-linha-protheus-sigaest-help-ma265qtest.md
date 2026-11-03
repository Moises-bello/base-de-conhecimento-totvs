---
article_id: 35853954914967
category: SIGAEST - MOVIMENTAÇÕES
content_hash: e0cb765134a8e9f2902abca81424fe6eada220bdf8d42074f936a8e118b0ef99
fetched_at: '2026-06-28T22:38:55.583168+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP MA265QTEST
type: support-article
updated_at: '2026-03-24T20:23:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35853954914967-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-MA265QTEST
---

O erro HELP MA265QTEST ocorre quando o saldo a estornar foi consumido por outro processo, como controle de lote, saldo vencido ou pedido reservado. Recomenda-se verificar esses pontos e, se o problema persistir, enviar o relatório MATR282 ao suporte para análise de desbalanceamento de saldos entre tabelas, informando os parâmetros MV\_ARQPROD, MV\_INTDL, MV\_INTWMS e MV\_WMSNEW.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35853954897047) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Durante um processo de estorno ou movimento, é apresentado o HELP MA265QTEST

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35853945458199)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
no padrão o HELP **MA265QTEST** é apresentado quando o saldo que tenta estornar foi consumido por algum processo ou rotina. Dessa forma, será necessário estornar todas as movimentações posteriores a esse endereçamento, voltando o saldo para o mesmo e sendo possível estornar.  
   
Caso não tenha nenhuma movimentação após esse endereçamento e mesmo assim o help persista, revise se esse produto controla lote, se o saldo do Lote esta vencido, ou se o produto consta em um pedido de venda reservado, ou em outros processos que empenham saldo do produto.  
  
Caso mesmo assim persista a apresentação do HELP MA265QTEST para esse cenário precisamos que envie ao suporte, o relatório MATR282 parametrizado como indicado no link abaixo para analisarmos se é o caso de desbalanceamento de saldos entre as tabelas.  
   
Informe também como como consta seguintes parâmetros:  
MV\_ARQPROD  
MV\_INTDL  
MV\_INTWMS  
MV\_WMSNEW  
[SIGAEST - MATR282 - Parametrização para identificar divergência de saldos entre tabelas SB2 X SB8 X SBF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF?source=search)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações de Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
