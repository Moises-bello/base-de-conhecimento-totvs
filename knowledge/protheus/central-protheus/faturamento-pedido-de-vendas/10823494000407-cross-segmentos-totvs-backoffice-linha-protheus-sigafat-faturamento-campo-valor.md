---
article_id: 10823494000407
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 482d0a08a549e62dcbe84a6ec13b89a418572c236d53ed998bcc28ca1e141724
fetched_at: '2026-06-28T22:38:42.610909+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Campo "Valor Presente" na aba Rentabilidade da Planilha Financeira no Pedido de
  Vendas
type: support-article
updated_at: '2022-12-13T19:28:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10823494000407-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-Valor-Presente-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min**

**Dúvida**

Qual a base da estruturação do campo "Valor Presente" na aba Rentabilidade da Planilha Financeira no Pedido de Vendas?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução**

A coluna Valor Presente que é uma fórmula matemático-financeira capaz de determinar o valor presente de pagamentos futuros descontados a uma taxa de juros apropriada.  
  
O Valor Presente muda conforme a condição de Pagamento escolhida e com base no conteúdo do parâmetro MV\_JUROS, que por padrão vem com 5%;  
  
Nesse exemplo, a condição escolhida foi: 30,60,90.  
  
  
Primeiro vamos entender a condição de pagamento. A data base é 11/03/15, sendo:

11/03 à 09/04 = 29 dias (1ª parcela = 333,33)  
11/03 à 09/05 = 59 dias (2ª parcela = 333,33)  
11/03 à 08/06 = 89 dias (3ª parcela = 333,34)

![](https://tdn.totvs.com/download/attachments/266963014/Planilha%20duplicata.png?version=1&modificationDate=1475242983000&api=v2)

A fórmula para o cálculo é:

O cálculo do valor total ou valor presente e realizado parcela a parcela utilizando a taxa de juros definida no parâmetro **MV\_JUROS**.

Valor Presente = Valor / ((1 + (Taxa Juros / 100)) \*\* (Prazo de pagamento / 30))

Deveremos realizar o cálculo para cada parcela, então:

**Cálculo da 1ª Parcela**

nTaxa      := SuperGetMV("MV\_JUROS")

nValor     := 333,33 (Valor da 1ª. Parcela)

dData      := 09/04/2015 (Vencimento 1ª. Parcela)

dDtEmissao := dDataBase (Neste Exemplo = 11/03/2015)

nPrazo     := dData - dDtEmissao

nPrazo     := 16/05/2017 – 17/04/2017

nPrazo     := 29 dias

**Desmembramento da Fórmula 1**

nValPres := nValor / ((1+(nTaxa / 100)) \*\* (nPrazo / 30))

nValPres :=333,33/ (( 1 + (5/100)) \*\* (29/  30))

nValPres :=333,33/ (( 1 + (5 / 100)) \*\* (29 / 30))

nValPres :=333,33/ ((1+(0,05)) \*\* (29 / 30))

nValPres := 72.39 / (1,05 \*\* 0.96666667)

nValPres :=333,33/ 317,97385061762432667048270927892

nValPres := 317,97385061762432667048270927892 (Valor Presente da 1ª Parcela)

**Cálculo da 2ª Parcela**

nTaxa      := SuperGetMV("MV\_JUROS")

nValor     :=333,33(Valor da 2ª. Parcela)

dData      := 09/05/2015 (Vencimento 2ª. Parcela)

dDtEmissao := dDataBase (Neste Exemplo =11/03/2015)

nPrazo     := dData-dDtEmissao

nPrazo     :=09/05/2015–11/03/2015

nPrazo     := 59 dias

**Desmembramento da Fórmula 2**

nValPres := nValor / ((1+(nTaxa / 100)) \*\* (nPrazo / 30))

nValPres :=333,33/ (( 1 + (5/100)) \*\* (59 / 30))

nValPres :=333,33/ (( 1 + (5/100)) \*\* (59 / 30))

nValPres :=333,33/ ((1 + (0,05)) \*\* (59 / 30))

nValPres :=333,33/ (1,05 \*\* 1.96666667)

nValPres := 72,39 / 1.10070842

nValPres := 302,83223868345173968617400883707 (Valor Presente da 2ª Parcela)

**Cálculo da 3ª Parcela**

nTaxa := SuperGetMV("MV\_JUROS")

nValor :=333,34(Valor da 3ª. Parcela)

dData := 08/06/2015 (Vencimento 3ª. Parcela)

dDtEmissao := dDataBase (Neste Exemplo =11/03/2015)

nPrazo := dData - dDtEmissao

nPrazo :=08/06/2015–11/03/2015

nPrazo := 89 dias

**Desmembramento da Fórmula 3**

nValPres := nValor / ((1 + (nTaxa / 100)) \*\* (nPrazo / 30))

nValPres :=333,34/ ((1 + (5 / 100)) \*\* (89 / 30))

nValPres :=333,34/ ((1 + (5 / 100)) \*\* (89 / 30))

nValPres :=333,34/ ((1 + (0,05)) \*\* (89 / 30))

nValPres :=333,34/ (1,05 \*\* 2.96666667)

nValPres :=333,34/ 1.15574384

nValPres := 288,42030832520268890400116602808 (Valor Presente da 3ª Parcela)

***Apuração do Valor Presente TOTAL***

nTotal: = 317,97385061762432667048270927892 (Valor Presente 1ª. Parcela) + 302,83223868345173968617400883707 (Valor Presente 2ª. Parcela) + 288,42030832520268890400116602808 (Valor Presente 3ª. Parcela)

nTotal: = **909,226412**(Valor Presente TOTAL)

**OBSERVAÇÃO: lembrando que \*\* refere-se a função exponencial (xy)**

**![](https://tdn.totvs.com/download/attachments/266963014/PLanilha%20Renta.png?version=1&modificationDate=1475242983000&api=v2)**

**Dúvidas na utilização do parâmetro MV\_JUROS contate a Equipe Protheus Financeiro e Planejamento.  
  
  
Saiba Mais:**

**[FAT0139 Processo para utilização de Rentabilidade no Pedido de Vendas (MATA410)](https://tdn.totvs.com/x/RojpDw)**
