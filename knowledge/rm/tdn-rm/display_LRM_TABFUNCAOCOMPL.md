---
content_hash: bb4da5a3e9c0a165ab8eb2c34261d22f7373371054497f0c47a5b82d3b4701f0
fetched_at: '2026-06-29T00:09:59.959883+00:00'
page_id: '452718465'
product: rm
source: tdn-rm
title: TABFUNCAOCOMPL
type: documentation
url: https://tdn.totvs.com/display/LRM/TABFUNCAOCOMPL
version: 2
---

**TABFUNCAOCOMPL**

A função TABFUNCAOCOMPL irá retornar o Campo Complementar de determinada função.

**Parâmetros:**

* Código da Função (CODFUNCAO) que servirá como filtro;
* Campo Complementar que deverá ser retornado;
* Tipo de retorno (V - Valor/Decimal, I - Inteiro,  S - String, D - Data), de acordo com o campo informado;

**Exemplo:**

TABFUNCAOCOMPL ('00002', 'TESTE1180', 'S') Neste exemplo iremos verificar o preenchimento do campo complementar: "TESTE1180" para a função: "00002".  
   
**TABREQUISICAO**

A função TABREQUISICAO irá retornar o preenchimento de um campo qualquer de uma deternada requisição.

**Parâmetros:**

* Inteiro que identifique a Requisição que conterá o campo;

0 – Aumento de Quadro (VREQAUMENTOQUADRO);

1 – Desligamento (VREQDESLIGAMENTO);

2 – Promoção (VREQPROMOCAO);

3 – Substituição (VREQSUBSTITUICAO);

4 – Transferência (VREQTRANSFERENCIA);

5 – Transferência com Promoção (VREQTRANSFPROMOCAO);

6 – Treinamento (VREQTREINAMENTO);

7 – Geral (VREQGERAL);

* Campo da Requisição que deverá ser retornado;
* Código da Requisição (IDREQ);
* Tipo do campo que será retornado (V - Valor/Decimal, I - Inteiro,  S - String, D - Data), de acordo com o campo informado;

**Exemplo:**

TABREQUISICAO(0,'CHAPAREQUISITANTE',15,'S')

Neste exemplo iremos verificar o preenchimento do campo "CHAPAREQUISITANTE" para a requisição do tipo: " 0 - Aumento de Quadro" identificada pelo código 15.
