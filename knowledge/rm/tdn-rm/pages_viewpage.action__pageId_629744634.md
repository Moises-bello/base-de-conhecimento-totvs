---
content_hash: 29d2acbfb2840147afc48efc8daf120a1085da352e68527914144087af213c7f
fetched_at: '2026-06-29T00:11:05.326466+00:00'
page_id: '629744634'
product: rm
source: tdn-rm
title: Utilizar Alíquota Interestadual Calculo DIFAL - Serviço de tributação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=629744634
version: 10
---

Foi realizado ajuste no processo de cálculo da "Base de Cálculo" para que seja verificado se o parâmetro "Utilizar Alíquota Interestadual Calculo DIFAL".

Se o mesmo estiver habilitado o sistema irá efetuar o cálculo do ICMS próprio considerando Base \* Aliq . E caso esteja desabilitado, irá considerar o valor que está no item de movimento (ValorICMSItem).

falseInformações

Os Fornecedores Optante de Simples, destaca a Alíquota e o Valor do ICMS nos Dados adicionais da NFe, para que os clientes possam utilizar o Credito do Imposto.

O cliente fez a compra para utilizar no Ativo Imobilizado, nesta situação deve ser utilizada o valor do Imposto como credito e calcular o Diferencial de Alíquota.

O Cálculo do Diferencial de Alíquota deve ser feito entre a “Alíquota Interestadual e a Alíquota Interna”.

Nesta situação temos 3 Alíquotas para cálculo.

Alíquota do Simples: 2,04% (não existe campo especifico)

Alíquota Interestadual: 12%

Alíquota Interna: 18%

Para atender esta situação foi criado na Regra do ICMS – Sub Pasta Dados ICMS ST, um novo campo “Utilizar Alíquota Interestadual Calculo DIFAL”

O campo funciona da seguinte forma:

Somente na inclusão do Movimento no RM Nucleus e no Processo de Escrituração.  
Somente para Movimentos de Entrada (somente nos Codigos de CFOP de Entrada).

Caso o campo **"Utilizar Alíquota Interestadual Calculo DIFAL"** esteja **habilitado**:

**Exemplo:**

No RM Nucleus, na Linha do Tributo ICMS foi utilizado a Alíquota 2,04% (alíquota informada manualmente) e o Valor do Imposto de 19,64.

Imagem

No Cálculo da Base de Cálculo do Difal deve ser utilizado a Alíquota Interestadual: 12% (informada na CFOP - Sub Pasta Dados ICMS ST ) e Valor do Imposto 115,80 (965,00 x 12%).

| Base do Difal = (965,00 – 115,80) = 849,20  849,20 / 0,82 = 1.035,61 |
| --- |

Caso o campo "Utilizar Alíquota Interestadual Calculo DIFAL"\* esteja **desabilitado**:

**Exemplo:**

No RM Nucleus, na Linha do Tributo ICMS foi utilizado a Alíquota 2,04% (alíquota informada manualmente) e o Valor do Imposto de 19,69.

Imagem

No Cálculo da Base de Cálculo do Difal deve ser utilizado a Alíquota Interestadual: 2,04% (informada no Movimento) e Valor do Imposto 19,69 (965,00 x 2,04%).

| Base do Difal = (965,00 – 19,69) = 945,31  945,31 / 0,82=1.152,82 |
| --- |

O ajuste não funciona em CFOP do tipo 6.

Disponível a partir da biblioteca 12.1.29
