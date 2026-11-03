---
content_hash: 81c2b28923f9957d8e3e1aab100ede700a2049d01bc57c4bc468f6a2e25cdf32
fetched_at: '2026-06-29T00:11:25.642991+00:00'
page_id: '714228101'
product: rm
source: tdn-rm
title: DT - Limite Campo Hora na Ficha Financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Limite+Campo+Hora+na+Ficha+Financeira
version: 23
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Ficha Financeira |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHCALCRM-2901](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2901) |

## **02. SITUAÇÃO/REQUISITO**

Verificar os campos que tem máscara se são calculados para aceitar até 546:07 e caso sim, passar aceitar até 999:59.

## **03. SOLUÇÃO**

Alterar o tipo do campo para int e também a máscara, que só aceita 3 dígitos. Aumentando o tamanho do campo possibilita números maiores. Neste caso teria que também alterar todos os módulos de Lançamento de eventos, como também as grids de lançamentos que tem em módulos como as Retificações, Rescisão Complementar, Entrada de Dados, etc e relatórios.

ATENÇÃO

Para permitir que o TOTVS Folha de Pagamento aceite valor até 999:59 no campo hora, foi necessário criar script de banco de dados para alterar o tipo do campo para int. 

Caso o cliente possua índice (SQL e Oracle) ou estatísticas (SQL) vinculado ao campo hora nas **tabelas** relacionadas abaixo, poderá retornar erro ao atualizar a base e a mesma ser travada. 

Neste caso **recomendamos que seja feito a atualização antes em uma base de homologação** e caso ocorra erros referente a marcação LB.2022.08\_07, orientamos que os índices (SQL e Oracle) ou estatísticas (SQL) sejam excluídos antes da atualização da base de dados.

Após o processo de atualização ser concluído o com sucesso, é necessário avaliar com o DBA da sua empresa a necessidade de recriar os índices novamente, pois os mesmos podem impactar na performance. 

Lembrando que os clientes possuem autonomia para fazer otimizações para o uso do banco de dados. No caso das tabelas abaixo, por padrão o produto não tem os índices para os campos relacionados.

Tabelas:

* PEVTRELACSALCMP campo:NHORAS
* PEVTRELACSALCMPCC campo:NHORAS
* PFENTMOV  campo: HORA
* PFFINANC  campo: HORA
* PFFINANCCOMPL  campo: HORA
* PFHSTENTMOV  campo: HORA
* PFMOVCC  campo: HORA
* PFMOVCCCOMPL  campo: HORA
* PFRESILICAOMOV  campo: HORA
* PFVALORFORCADO  campo: HORA
* PFVERBAS  campo: HORA
* PFVERBASCOMPL  campo: HORA
* PFVERBASDIS  campo: HORA
* PFVERBASDISFER  campo: HORA
* PFVERBASDISFERHIST  campo: HORA
* PFVERBASDISHIST  campo: HORA
* PORCAMENTOPERFILEVENTOS  campo: HORA
* PFMOVTOMADOR  campo: HORA
* PFRESILICAOMOVBASE  campo: HORA
* PORCAMENTOMOVVALOR  campo: HORA
* PPOSTRANSFERENCIA  campo: HORA
* PSIMULADEMISSAOEVENTOS  campo: HORA
* PFSUBSTITUICAO  campo: NROHORAS
* PFSUBSTITUICAO  campo: NROHORASORIGINAL

Foi incluída uma validação onde o atualizador não permitirá a atualização caso existem índice (SQL e Oracle) ou estatísticas (SQL). Caso seja reportado o erro desta situação, pode ser verificado no banco a lista de tabelas e colunas dos índice (SQL e Oracle) ou estatísticas (SQL) existentes com as consultas abaixo:

ÍndicesORACLEsqlVerificar índicesSQLsqlVerificar índicesEstatísticasSQLsqlVerificar estatísticas
