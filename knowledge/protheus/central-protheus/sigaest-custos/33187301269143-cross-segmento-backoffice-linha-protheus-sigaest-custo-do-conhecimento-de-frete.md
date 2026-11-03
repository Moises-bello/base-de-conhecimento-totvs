---
article_id: 33187301269143
category: SIGAEST - CUSTOS
content_hash: aa38825ab1aab4047816c367cbe4f4e3e20947657fb014671cd628eff742a209
fetched_at: '2026-06-28T22:39:00.852240+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Custo do Conhecimento
  de Frete ao efetuar Retorno de Beneficiamento Em Terceiros
type: support-article
updated_at: '2025-07-02T11:17:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33187301269143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-do-Conhecimento-de-Frete-ao-efetuar-Retorno-de-Beneficiamento-Em-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33187305154071) Tempo aproximado para leitura: **00:03:15 min**

**Dúvida**

Ao incluir a amarração de uma Nota de Conhecimento de Frete a uma [Nota de Retorno de Beneficimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063627613-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-processo-de-Remessa-para-Beneficiamento-de-OP-Em-Terceiros), apresenta o Help informando que que não vai gerar a RE5 para a OP e quando confirmamos com Sim, o Custo do Conhecimento de Frete/Despesa não é agregado ao Produto Acabado. É possível de alguma forma que esse Conhecimento seja apropriado diretamente ao Custo da OP no Produto Acabado, quando a mesma ja foi encerrada?

![conhecimento frete.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/33187777584407)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

**Conceito padrão:** Esse cenário ocorre, devido ao efetuar o processo **de Retorno de Beneficiamento da OP da** ***quantidade Total*** **dos componentes** enviados para Beneficiamento, é gerada o ***apontamento da Ordem de Produção Total*** e nesse caso a OP é encerrada, **não é permitido e inclusão de movimentações para essa OP**, pois a mesma esta encerrada impede qualquer tipo de movimentação.

**Caso,** clicar em Sim no Help apresentado, na inclusão do Conhecimetno de Frete, o Custo é apropriado aos Componentes (MP) da Nota de Retorno, e **não ao Produto Acabado**.

**Pergunta:** É possível de alguma forma incluir o Conhecimento de Frete para que o Custo seja apropriado ao Produto Acabado (PA) para esse cenario com a OP encerrada?

**Resp.:** Nesse caso, somente é possível efetuar a inclusão do Conhecimento de Frete em cenários em que os retornos foram parciais, ou mesmo, situações em que inclua uma Nota do Serviço para a OP **antes do retorno Total dos Componentes** que foram enviados.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Como efetuar o processo de Remessa para Beneficiamento de OP Em Terceiros?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063627613-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-processo-de-Remessa-para-Beneficiamento-de-OP-Em-Terceiros)

[SIGAEST - Processo para recebimento de Beneficiamento com MP de Terceiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025818694-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-para-recebimento-de-Beneficiamento-com-MP-de-Terceiros)
