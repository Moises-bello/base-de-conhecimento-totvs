---
article_id: 18537249318423
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 3d9562d68bf4d1989bd7530856b384ba7e881f1f121f35c241f21294b424ff9a
fetched_at: '2026-06-28T22:38:56.986569+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Requisitar
  ou Devolver saldo maior que o empenho
type: support-article
updated_at: '2025-03-12T12:23:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18537249318423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Requisitar-ou-Devolver-saldo-maior-que-o-empenho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18537222796823) Tempo aproximado para leitura: **00:04:15 min** **Dúvida**

Na rotina **Movimentações Internas (MATA241)** ao Requisitar ou Devolver saldo informando uma Ordem de produção (D3\_OP), quando a quantidade maior que o empenho, apresenta o HELP **"A quantidade da requisição é maior que o saldo empenhado deste produto para esta OP. Ao requisitar essa quantidade o empenho não sera baixado."** Qual o conceito e funcionalidade?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18537398097175)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O Help é apresentado  quando utiliza um Tipo de Movimentação com o campo ***Atualiza Empenho (F5\_ATUEMP)*** igual a **Sim**, nesse caso é um alerta que a operação Devolve ou Requisita com saldo ***maior que a quantidade empenhada na OP***. ***Esse cenário não se trata de um erro***

Ao apresentar o HELP deve analisar se pode ou não continuar com a movimentação, ou mesmo se deseja efetuar o processo de ajustes de empenho manualmente na rotina MATA381 **antecedendo a movimentação interna manual**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18538192445335)

Para efetuar movimentações nesse cenário pela rotina manual o ***limite de saldo atualizando empenho*** é o que foi definido na abertura da OP, ou mesmo na rotina Ajustes de Empenhos (MATA381).

Ou seja, não é possível ajustar empenhos Requisitando ou Devolvendo saldo pela rotina Movimentações Internas (MATA241), esse cenário **é limitado ao que consta empenhado na tabela SD4**.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
