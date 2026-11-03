---
content_hash: 690825ea6c65f0427b45d032c14aed2988c6b3ba94dd47367fe02a54da1f6df5
fetched_at: '2026-06-29T00:11:05.283303+00:00'
page_id: '628949767'
product: rm
source: tdn-rm
title: FISCAL01-15553 DT Utilizar Alíquota Interestadual Calculo DIFAL - Serviço de
  tributação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628949767
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Diferencial de Alíquota |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15553 |

## **02. SITUAÇÃO/REQUISITO**

Os Fornecedores Optante de Simples, destaca a Alíquota e o Valor do ICMS nos Dados adicionais da NFe, para que os clientes possam utilizar o Credito do Imposto.

O cliente fez a compra para utilizar no Ativo Imobilizado, nesta situação deve ser utilizada o valor do Imposto como credito e calcular o Diferencial de Alíquota.

O Cálculo do Diferencial de Alíquota deve ser feito entre a “Alíquota Interestadual e a Alíquota Interna”.

Nesta situação temos 3 Alíquotas para cálculo.

Alíquota do Simples: 2,04% (não existe campo especifico)

Alíquota Interestadual: 12%

Alíquota Interna: 18%

Para atender esta situação é necessário cria na Regra do ICMS – Sub Pasta Dados ICMS ST, um novo campo “Utilizar Alíquota Interestadual Calculo DIFAL” , como deve funcionar o campo:

Somente na inclusão do Movimento no RM Nucleus e no Processo de Escrituração.  
Somente para Movimentos de Entrada (se der para habilitar o campo somente nos Codigos de CFOP de Entrada).  
Habilitado:  
No RM Nucleus, na Linha do Tributo ICMS deve ser utilizado a Alíquota 2,04% (aliquota informado manualmente) e o Valor do Imposto de 19,64.

No Cálculo da Base de Cálculo do Difal deve ser utilizado a Alíquota Interestadual: 12% (informada na CFOP) e Valor do Imposto 115,80 (965,00 x 12%).

Base do Difal = (965,00 – 115,80) = 849,20

849,20 / 0,82 = 1.035,61

Obs: Este é o tipo de cálculo deve ser implementado.

4. Desabilitado

No RM Nucleus, na Linha do Tributo ICMS deve ser utilizado a Alíquota 2,04% (incluída manualmente) e o Valor do Imposto de 19,69.

No Cálculo da Base de Cálculo do Difal deve ser utilizado a Alíquota Interestadual: 2,04% (informada no Movimento) e Valor do Imposto 19,69 (965,00 x 2,04%).

Base do Difal = (965,00 – 19,69) = 945,31

945,31 /0,82=1.115,81

Obs: Atualmente este cálculo já é feito e esta correto.

## **03. SOLUÇÃO**

Ajuste no processo de cálculo da "Base de Cálculo" para que seja verificado se o parâmetro "Utilizar Alíquota Interestadual Calculo DIFAL" , se o mesmo estiver habilitado o sistema irá efetuar o cálculo do ICMS próprio considerando Base \* Aliq , caso esteja desabilitado, irá considerar o valor que está no item de movimento (ValorICMSItem).
