---
content_hash: fdec190eddbf0bf07e5dc2f30c46f71d5d457ac6389c0114de94ee7ce19f20be
fetched_at: '2026-06-29T00:11:43.482832+00:00'
page_id: '807214768'
product: rm
source: tdn-rm
title: idePrestServ
type: documentation
url: https://tdn.totvs.com/display/LRM/idePrestServ
version: 2
---

## Identificação do prestador de serviços mediante cessão de mão de obra ou empreitada

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| idePrestServ | ideEstabObra | 1-1 | 14 | Identificação do prestador de serviços mediante cessão de mão de obra ou empreitada |  |
| cnpjPrestador | idePrestServ | 1-1 | 14 | Preencher com o CNPJ do prestador de serviços. Validação: Deve ser um CNPJ válido. Não pode pertencer ao declarante. Se {indObra} for igual a [1] (empreitada total) o CNPJ do prestador terá que ser o proprietário do CNO informado no campo {nrInscEstab}. | **Se** Existe um projeto associado ao Lançamento **&** O tipo de Obra for Empreitada Parcial **&** o Tipo de Projeto for próprio **Então** o campo será gerado com o CNPJ do Projeto  **Senão**, será gerado com o CNPJ do Prestador do serviço. |
| vlrTotalBruto | idePrestServ | 1-1 | 14 | Preencher com a soma da base de cálculo da retenção da contribuição previdenciária das notas fiscais emitidas para o contratante. Validação: Deve corresponder à soma dos valores informados no campo {vlrBaseRet} dos registros vinculados. |  |
| vlrTotalBaseRet | idePrestServ | 1-1 | 14 | Indicativo de Prestação de Serviços em Obra de Construção Civil.  Valores Válidos: 0 - Não é obra de construção civil ou não está sujeita a matrícula de obra; 1 - Obra de Construção Civil - Empreitada Total; 2 - Obra de Construção Civil - Empreitada Parcial;  Validação: Em arquivo gerado por Pessoa Física, deve ser igual a [1,2]. |  |
| vlrTotalRetPrinc | idePrestServ | 1-1 | 14 | Soma do valor da retenção sobre o valor das notas fiscais de serviço emitidas para o contratante. Validação: Deve corresponder à soma dos valores informados no campo {vlrRetencao}, subtraído da soma dos valores informados no campo {vlrRetSub} dos registros vinculados. |  |
| vlrTotalRetAdic | idePrestServ | 0-1 | 14 | Soma do valor do adicional de retenção sobre os valores das notas fiscais. Validação: Deve corresponder à soma dos valores  informados no campo {vlrAdicional} dos registros vinculados. |  |
| vlrTotalNRetPrinc | idePrestServ | 0-1 | 14 | Valor da retenção principal que deixou de ser efetuada pelo contratante ou que foi depositada em juízo em decorrência de decisão judicial. Validação: Deve corresponder à soma dos valores informados no campo {vlrNRetPrinc} dos registros vinculados. |  |
| vlrTotalNRetAdic | idePrestServ | 0-1 | 14 | Valor da retenção adicional que deixou de ser efetuada pelo contratante ou que foi depositada em juízo em decorrência de decisão judicial. Validação: Deve corresponder à soma dos valores informados no campo {vlrNRetAdic} dos registros vinculados |  |
| indCPRB | idePrestServ | 1-1 | 1 | Indicativo se o prestador é contribuinte da contribuição previdenciária sobre a receita bruta (CPRB), a qual reduz a alíquota de 11% para 3,5% na retenção de contribuição previdenciária: 0 - Não é contribuinte da CPRB - retenção de 11%; 1 - É contribuinte da CPRB - retenção de 3,5%. | Se Alíquota do INSS = 11%  então 0  Senão, 1 |
