---
content_hash: aa314205add7bbddf2289c24776e5465ba36c315f387027ba45f91bd1c5b76d2
fetched_at: '2026-06-29T00:11:33.450779+00:00'
page_id: '761005426'
product: rm
source: tdn-rm
title: DT - IRRF Simplificado
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+IRRF+Simplificado
version: 9
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo d IRRF Simplificado |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-3985](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3985) |

## **02. SITUAÇÃO/REQUISITO**

Com a entrada do IRRF Simplificado, o produto deve fazer o cálculo IRRF, lançado o desconto mais benéfico para o funcionário, ou seja, o de menor valor apurado.

Para isto será necessário executar a comparação do cálculo de IRRF para cada funcionário considerando o cálculo mais benéfico entre a base de cálculo com o valor de dedução simplificada e a base de cálculo com o valor das deduções legais.

## **03. SOLUÇÃO**

Novo Valor Fixo com a finalidade “Valor a deduzir no IRRF simplificado”, que será usado para comparar com o somatório das deduções legais e considerar o que for mais benéfico para o funcionário.

Possibilidade de não calcular para funcionários que optarem pelo cálculo integral sem comparar com o valor simplificado marcando o parâmetro “Desconsiderar desconto simplificado do IRRF” em parâmetros do cadastro de Funcionários. Essa marcação poderá ser feita pelo processo de Alteração Global de Campos.

Campos informativos nas tabelas PFPERFF, PFPERFFCOMPL e PFUFERIASRECIBO, indicando se o cálculo daquele período foi considerado a dedução simplificada. Estes campos serão apenas visíveis e não editáveis nos respectivos cadastros.

ATENÇÃO - LEMBRETE

**Para a criação dos campos acima é necessário atualização da base de dados.**

## **04. DEMAIS INFORMAÇÕES**

Veja mais informações [IRRF – Ajuste na Tabela do Imposto de Renda](https://www.totvs.com/blog/fiscal-clientes/irrf-ajuste-na-tabela-do-imposto-de-renda/)

## **05. ASSUNTOS RELACIONADOS**

* [Valores Fixos](https://tdn.totvs.com/display/LRM/Valores+Fixos)
* [Cadastro de Funcionários - Parâmetro “Desconsiderar desconto simplificado do IRRF”](https://tdn.totvs.com/pages/viewpage.action?pageId=452719181)
* [Cálculo do IRRF Simplificado](https://tdn.totvs.com/pages/viewpage.action?pageId=761006653)
