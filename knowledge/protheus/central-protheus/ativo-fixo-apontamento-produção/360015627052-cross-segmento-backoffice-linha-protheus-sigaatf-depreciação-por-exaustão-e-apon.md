---
article_id: 360015627052
category: Ativo Fixo - Apontamento Produção
content_hash: 7bb3938460fc789ea1887df6b0aae9dbb6bd5143d047dbbb547ba6ca7135b5e9
fetched_at: '2026-06-28T22:41:57.522821+00:00'
product: protheus
section_id: 1500001546922
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - DEPRECIAÇÃO POR EXAUSTÃO
  E APONTAMENTOS DE PRODUÇÃO - ATFA110
type: support-article
updated_at: '2022-07-22T13:16:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015627052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-DEPRECIA%C3%87%C3%83O-POR-EXAUST%C3%83O-E-APONTAMENTOS-DE-PRODU%C3%87%C3%83O-ATFA110
---

**Dúvida**

Procedimentos referente a rotina de apontamento de produção

**Ambiente**  
Protheus – Ativo Fixo – A partir da versão 11.80  
  
**Solução**

Rotina Apontamento de Produção (ATFA110), é possível calcular o método de depreciação por Exaustão linear e Exaustão por saldo residual.  
Os ativos imobilizados para este novo método de depreciação são informados no Cadastro de Ativo (ATFA012), e são utilizados para calcular e depreciar determinados tipos de bens através dos apontamentos de produção em que não pode ser determinada pelo tempo de vida útil.  
Para bens deste tipo, a depreciação é calculada por meio do que foi produzido em um determinado período, com a estimativa de produção total.

Este método de depreciação resulta em uma despesa baseada na produção esperada pelo imobilizado.  
Neste método é obrigatório o preenchimento dos campos **Prod. Período** (N3\_PRODMES) e **Prod. Previst**. (N3\_PRODANO), que determinam, respectivamente, unidade produzida por mês e unidade produzida no período.

**Características do cálculo:**

A alíquota é variável e definida em função das unidades produzidas no período.

**Fórmula para determinar a alíquota:**

Taxa de depreciação = Número de unidades produzidas no período / Número de unidades estimadas a serem produzidas durante a vida útil do bem.

**Fórmula para determinar o valor da depreciação:**

Depreciação = Valor Original Atualizado do Bem \* Taxa de depreciação

Onde:

Valor original do bem: é considerado como valor original o valor de aquisição do bem, que dependendo da forma de atualização deste valor, pode conter as ampliações e as reavaliações sofridas desde sua aquisição.

***Exemplo de cálculo: unidades produzidas***

Valor do ativo                          30.000,00  
Vida útil (anos)                        5,00  
Expectativa de produção        5.000,00

Outras informações  para utilização da rotina atfa110

[Depreciação por exaustão e apontamentos de produção Depreciação por exaustão e apontamentos de produção](http://tdn.totvs.com/pages/viewpage.action?pageId=36307623)

[Apontamento de Produção (ATFA110 - SIGAATF)](http://tdn.totvs.com/pages/viewpage.action?pageId=312159891)

[Métodos de depreciação gerencial](https://tdn.totvs.com/pages/releaseview.action?pageId=6067612)
