---
content_hash: 3045f3249772d5b549957c09648663ce863f7d10a6a04096be471a3ffe892b93
fetched_at: '2026-06-29T00:10:46.699989+00:00'
page_id: '555850129'
product: rm
source: tdn-rm
title: Fórmula para contabilização de lançamento - TOTVS Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555850129
version: 4
---

---

Durante o processamento da contabilização ou geração da nota fiscal é possível recuperar o valor da bolsa processado para o lançamento utilizando a fórmula VALORBOLSALAN.

**Fórmula VALORBOLSALAN**

**Declaração da fórmula:** ValorBolsaLan(int campoValor, int tipoBolsa, string codBolsa)

=>  int campoValor

0 = Será retornado o valor da bolsa

1 = Será retornado o valor da bolsa na baixa

2 = Será retornado o valor da bolsa sem considerar o valor do desconto por antecipação da parcela

3 = Será retornado o (valor da bolsa sem o desconto por antecipação - valor da bolsa (considerando o maior desconto por antecipação) )

=>  int tipoBolsa

    Escalável = 0,

    Especial = 1,

    Todas = -1

=>   string codBolsa

Pode passar o código da bolsa, se for passado vazio ou -1 indica que o sistema vai somar todas as bolsas.

Para geração de lançamento parametrizado com essa fórmula o valor da bolsa não irá variar conforme o desconto por antecipação e nem perder a bolsa, neste caso a fórmula sempre traz o valor da bolsa.

Contabilização

Na contabilização do lançamento quando o evento contábil estiver parametrizado para aplicar na “Bolsa”, a fórmula pode ser utilizada conforme o exemplo abaixo.

VALORBOLSALAN(0,-1,TABBOLSALAN('CODBOLSA','S'))

=>  TABBOLSALAN('CODBOLSA','S')  -  retorna o código da bolsa corrente, ou seja, que está sendo processada.
