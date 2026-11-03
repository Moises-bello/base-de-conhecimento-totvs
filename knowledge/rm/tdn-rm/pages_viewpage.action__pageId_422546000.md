---
content_hash: 61929dbf97d2ede3c367d6c39a946854d153cbb84fdc56eb57389821d771fa15
fetched_at: '2026-06-29T00:09:22.553184+00:00'
page_id: '422546000'
product: rm
source: tdn-rm
title: Flexibilização de Geração de Guias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546000
version: 5
---

# **Conteúdo**

**2Conteúdo**

## **01. Introdução**

O processo de flexibilização realiza o agrupamento dos valores das guias dos tributos INSS, IRRFPJ e ISS, otimizando o processo de geração automática de guias. Ao optar pela geração de guias pelo processo de Flexibilização, vamos ter duas opções, que segue:

1. Gerar as Guias Nota a Nota
2. Gerar as Guias utilizando Agrupamento

## **02.** **Nota a Nota**

Ao selecionar essa opção o TOTVS Gestão Fiscal irá uma guia para cada nota existente no período de apuração, tendo a possibilidade de realizar o filtro desses lançamentos de acordo com o tributo e respeitando a sua regra básica.

Utilização da telaleftISS – Regra Básica (por município)

* Cliente/Fornecedor
* Tipo de Documento
* Número do Documento
* Tipo de Lançamento
* Projeto
* Centro de Custo
* Data de Entrada e Data de Emissão
* Município de Prestação do Serviço
* Código do Serviço
* Alíquota do Tributo
INSS – Regra Básica (por código de receita, por contratada Cliente/Fornecedor)

* Cliente/Fornecedor
* Tipo de Documento
* Número do Documento
* Tipo de Lançamento
* Projeto
* Centro de Custo
* Data de Entrada e de Emissão
* Filial
* Código de Receita
IRRF PJ – Regra Básica: por código de receita

* Cliente/Fornecedor
* Tipo de Documento
* Número do Documento
* Centro de Custo
* Datas de Entrada e ou Emissão
* Filial
* Código da Receita
IRRF, PIS-RF, COFINS-RF, CSLL-RF e CSRF - Regra Básica (por código de Receita)

* Cliente/Fornecedor
* Tipo de Documento
* Número do Documento
* Centro de Custo
* Datas de Baixa e/ou Emissão
* Filial
* Código da Receita
falseNa geração de guias Nota a Nota é importante que se defina um filtro (com valores comuns entre os lançamentos) para a geração das guias. exemplo:  
Ao selecionar a geração de guia nota a nota para o tributo ISS filtrando por Cliente/Fornecedor "A" e por Tipo de Lançamento igual a "Saída", teremos como resultado guias nota a nota de todos os lançamentos de saída do período do cliente/fornecedor "A".

## **03.** **Agrupamento**

Quando selecionar a opção de agrupamento o TOTVS Gestão Fiscal vai exibir, de acordo com o tributo, as opções:

Centro de Custo Contábil:

Neste campo deverá ser informado o Centro de Custo Contábil a ser utilizado pelo sistema na Contabilização do lançamento.

**Observação:**

No momento da contabilização do lançamento, o Centro de Custo Contábil irá prevalecer sobre o Centro de Custo informado para os default(s) do Evento Contábil, ou seja, todas as contas a débito e crédito serão contabilizadas com o Centro de Custo do lançamento.

Utilização da telaleftISS – Opções de Agrupamento

* Alíquota Tributo
* Centro de Custo Contábil
* Cliente/Fornecedor
* Código de Serviço
* Projeto
* Tipo de Lançamento (Entrada e Saída)
INSS

* Centro de Custo Contábil
* Filial
* Projeto
IRRF PJ

* Centro de Custo Contábil
* Cliente Fornecedor
* Filial
* Projeto
IRRF, PIS-RF, COFINS-RF, CSLL-RF e CSRF

* Cliente/Fornecedor
* Filial
false

O processo de agrupamento irá gerar as guias de acordo com tipo de agrupamento selecionado, dentro desse processo ainda é possível realizar os filtros pertinentes aos tributos, aumentando as opções para geração, exemplo:  
Ao selecionar o Tributo ISS, agrupando por cliente e fornecedor, passando para o filtro o cliente "A", o TOTVS Gestão Fiscal irá gerar uma única guia com todos os valores de ISS desse cliente/fornecedor, respeitando a regra básica do tributo. Ao realizar o agrupamento os campos alíquota e Tipo não serão preenchidos por que ao agrupar o TOTVS Gestão Fiscal irá buscar todos os lançamentos entrada e saída e todas as alíquotas.

Importante:Em cada filial só poderão ser geradas guias cujos lançamentos de origem se relacionam com esta filial. A exceção será para os tributos federais que poderão ser geradas na filial matriz, ou seja, todas as filiais deverão ser apresentadas no filtro.falseAlgumas opções não fazem sentido para determinados tributos, por exemplo: opção de filtro por Filial para guias de ISS. Nesse caso, as guias de ISS devem ser geradas em cada filial. Porém, como existe um filtro pré-definido do próprio sistema, como tipo de tributo, período, etc, ainda assim poderemos utilizar um único filtro para todos os tributos.
