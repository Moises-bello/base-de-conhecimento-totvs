---
content_hash: 3266c24847b262af794d850130aba7d5cfd37ad5123e3141d1d3a1ea78364a89
fetched_at: '2026-06-29T00:11:39.892936+00:00'
page_id: '790646098'
product: rm
source: tdn-rm
title: Exemplos para regra de cálculo dos encargos 5 - Provisão de FGTS de férias
  e 6 - Provisão de encargos de férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790646098
version: 11
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Ao gerar o Encargo de provisões de férias quando o funcionário teve férias em dobro pagas, o sistema não calculará  o encargo de FGTS e INSS sobre o valor das férias em dobro, conforme legislação, as férias em dobro não tem incidência de INSS e FGTS.

Essa isenção de encargos está prevista no Art. 28, § 9º, "d" da Lei 8.212/91 para o INSS e no Art. 15, § 6º da Lei 8.036/90 para o FGTS.

Selecionando a provisão acumulada será gerada acumulada para os encargos do tipo:

* + 5 - Provisão de FGTS de Férias
  + 6 - Provisão de Encargo de Férias

Regra abaixo somente para os encargos  5 - Provisão de FGTS de Férias e 6 - Provisão de Encargo de Férias.

Se provisão do mês **anterior** férias em dobro = 0 e provisão do mês **atual** férias em dobro > 0 

Então provisão do mês **atual** - provisão do mês **atual** férias em dobro - provisão do mês **anterior**

Se provisão mês **atual** férias em dobro > 0 e provisão **anterior** férias > 0 e férias pagas no mês > 0

Então  provisão mês **atual**  - (provisão mês **anterior** - provisão mês **anterior** férias em dobro)

Senão provisão mês **atual** - provisão mês **anterior** 

Neste caso, os encargos 5 e 6 não devem considerar o valor das férias em dobro.

 

Lógica para o parâmetro "**Inibe Reversão de Valores na provisão mensal de férias para situações  onde houve abatimento de férias**" (Configurações/Parametrizador/Folha Normal/Contabilização):

Se o valor da provisão de férias em dobro do mês **atual** estiver zerado, não abater o valor de férias em dobro nos encargos 5 - Provisão de FGTS de Férias e 6 - Provisão de Encargo de Férias. Caso contrário, manter a fórmula atual.

## **02. EXEMPLO DE UTILIZAÇÃO**

Geração dos histórico de encargos após geração do histórico de provisões com parâmetro abate férias marcado e com uma férias em dobro FUNC 00001 e com mais de uma férias em dobro FUNC 00002.

Dica

Clique em cada um dos links para ver os exemplos de acordo com a parametrização.

11PARÂMETRO Inibe reversão desmarcado e PARÂMETRO Provisão acumulada marcado

***FUNC 00001***

**Cenário 01 -** Histórico de provisão antes de pagar as férias

22059,19 - 6430,33 = 15628,66

**Cenário 02 -** Histórico de provisão no mês de pagamento das férias

9220,74 - 6430,33 = 2790,41

**Cenário 03 -** Histórico de provisão depois do mês de pagamento das férias

***FUNC 00002***

**Cenário 01 -** Histórico de provisão antes de pagar as férias

64854,43 - 25060,28 = 39794,15

**Cenário 02 -** Histórico de provisão no mês de pagamento das férias

48166,82 - 25060,28 = 23106,54

**Cenário 03 -** Histórico de provisão depois do mês de pagamento das férias

48838,20 - 16706,85 = 32131,35

2PARÂMETRO Inibe reversão desmarcado e PARÂMETRO Provisão acumulada desmarcado

***FUNC 00001***

**Cenário 01 -** Histórico de provisão antes de pagar as férias

Se provisão referente ao anterior férias em dobro = 0 e provisão do mês atual férias em dobro > 0 

Então provisão do mês atual - provisão do mês atual férias em dobro - provisão anterior

mês atual 3 e mês anterior 2

20040,50 - 6297,00 - 12327,33 = 1416,17

**Cenário 02 -** Histórico de provisão no mês de pagamento das férias

Se provisão mês atual férias férias em dobro > 0 e provisão mês anterior férias > 0 e férias pagas no mês > 0

Então  provisão do mês atual  - (provisão do mês anterior - provisão do mês anterior férias em dobro)

mês atual 7 paga férias e mês anterior 6

9220,74 - (22059,19 - 6430,33) = - 6408,12

**Cenário 03 -** Histórico de provisão depois do mês de pagamento das férias

Se não existir variáveis para os dois cenários acima então será: provisão mês atual - provisão mês anterior

mês atual 8 e mês anterior 7

9.698,84 - 9.220,74 = 478,10

***FUNC 00002***

**Cenário 01 -** Histórico de provisão no mês de pagamento das férias

Se provisão do mês atual férias férias em dobro > 0 e provisão do mês anterior férias > 0 e férias pagas no mês > 0

Então  provisão do mês atual  - (provisão do mês anterior - provisão do mês anterior férias em dobro)

mês atual 7 paga férias e mês anterior 6

48166,82 - (64854,43 - 25060,28) = 8372,67

**Cenário 02 -** Histórico de provisão depois do mês de pagamento das férias

Se não existir variáveis para os cenários: 

* provisão referente ao mês anterior férias em dobro = 0 e provisão do mês atual férias em dobro > 0 - Nesse caso o cenário não condiz com a condição de ser provisão referente ao anterior férias em dobro = 0
* provisão do mês atual férias férias em dobro > 0 e provisão do mês anterior férias > 0 e férias pagas no mês atual > 0 - Nesse caso o cenário não condiz com a condição de ser férias pagas no mês > 0

Então o cálculo será: provisão do mês atual - provisão do mês anterior

mês atual 8 e mês anterior 7

48838,20 - 48166,82 = 671,38

3PARÂMETRO Inibe reversão marcado e PARÂMETRO Provisão acumulada desmarcado

Se o valor da provisão de férias em dobro do mês atual estiver zerado ou se o valor da provisão de férias em dobro mês anterior for maior que o valor da provisão de férias em dobro do mês atual, a fórmula é:

provisão do mês atual sem abatimento - provisão do mês anterior com abatimento

Caso contrário, será:

(provisão do mês atual sem abatimento - provisão de férias em dobro) - (provisão do mês anterior com abatimento - provisão de férias em dobro)

***FUNC 00001***

**Cenário 01 -** Histórico de provisão antes de pagar as férias

(provisão do mês atual sem abatimento - provisão de férias em dobro) - (provisão do mês anterior com abatimento - provisão de férias em dobro)

mês atual 3 tem provisão férias em dobro e mês anterior 2 está zerado

(20040,50 - 6297,00) - (12327,33 - 0) = 1416,17

**Cenário 02 -** Histórico de provisão no mês de pagamento das férias

(provisão do mês atual sem abatimento - provisão de férias em dobro) - (provisão do mês anterior com abatimento - provisão de férias em dobro)

mês atual 7 e mês anterior 6 têm valor de provisão férias em dobro 

(22438,67 - 6430,33) - (22059,19 - 6430,33) = 379,48

**Cenário 03 -** Histórico de provisão depois do mês de pagamento das férias

Está nessa condição: Se o valor da provisão de férias em dobro do mês atual estiver zerado, não abate o valor de férias em dobro. Então o cálculo será: provisão mês atual - provisão mês anterior 

mês atual 8 valor da provisão de férias em dobro zerado e mês anterior 7 têm valor de provisão férias em dobro

9.698,84 - 9.220,74 = 478,10

***FUNC 00002***

**Cenário 01 -** Histórico de provisão no mês de pagamento das férias

(provisão do mês atual sem abatimento - provisão de férias em dobro) - (provisão do mês anterior com abatimento - provisão de férias em dobro)

mês atual 7 e mês anterior 6 têm valor de provisão férias em dobro 

(65337,77 - 25060,28) - (64854,43 - 25060,28) = 483,34

**Cenário 02 -** Histórico de provisão depois do mês de pagamento das férias

Nesse caso temos mais de uma férias em dobro e foi paga somente uma delas, por isso o campo férias em dobro continua com valor nos dois meses. Será considerada a seguinte condição: o valor da provisão de férias em dobro mês anterior for maior que o valor da provisão de férias em dobro do mês atual.

Portanto será calculado da seguinte forma:

provisão do mês atual sem abatimento - provisão do mês anterior com abatimento

mês atual 8 e mês anterior 7 têm valor de provisão férias em dobro

48838,20 - 48166,82 = 671,38

## **03.** **TABELAS UTILIZADAS**

* PFHSTPROV
* PFENCARGO
