---
content_hash: f8379293d3f3871aa421d2446b6353f3ce76bee04cc47e1eebfef17f56e338bc
fetched_at: '2026-06-29T00:09:49.190586+00:00'
page_id: '435105251'
product: rm
source: tdn-rm
title: Valores de Origem
type: documentation
url: https://tdn.totvs.com/display/LRM/Valores+de+Origem
version: 8
---

Esta tela será responsável por definir o que será considerado para o "Cálculo da Composição da Base de Cálculo".  
 Campos a serem preenchidos:

Aba Identificação - Valores de Origem

**ID do Valor de Origem:**  
Valor auto Incremental que identifica o valor de origem.  
  
**Descrição:**  
Informe a descrição do Valor de Origem.  
  
**Operação:**  
Defina se o valor de origem será somado ou subtraído aos demais valores de origem dessa composição.  
  
**Tipo de Origem:**  
Informe se a Origem será do tipo contábil ou através de Fórmula.  
  
**Considerar como Data Inicial a Data Base da regra de Apuração:**  
Defina se a Data inicial da regra será a Data base da Regra de Apuração.

ObservaçãoPara que essa flag tenha efeito é preciso preencher o campo "Data Base" na tela  e então será considerado esta data em vez da data Inicial do Avanço da Obra.

**Código da Fórmula:**  
Informe o código da fórmula que será considerada para o cálculo no valor de origem.

ObservaçãoO campo ficará habilitado caso o tipo de origem escolhido for "Fórmula".Aba Origem Contábil

**Conta Contábil:**  
Conta da qual deve-se considerar o valor.  
   
**Tipo de Movimentação:**  
Informe qual o tipo de movimentação será considerada no valor de origem.

* Débito - Considera apenas os lançamentos de Débito.
* Crédito - Considera apenas os lançamentos de Crédito
* Movimentação Conta - Considera apenas os lançamentos no período da apuração.
* Saldo Anterior - Considera o saldo anterior ao início do período da apuração.
* Saldo Atual - Considera o saldo até o período da apuração.

**Histórico Padrão:**  
Permite a inclusão de uma lista de históricos padrões que serão considerados como filtros para essa conta contábil.

ObservaçãoCaso não seja informado nenhum histórico padrão, não será filtrado por histórico padrão.
