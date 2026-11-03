---
content_hash: 8bd35deb54eb8d2bcd0518357358678c4ce8bb931b0debda6b63796fd8a5f016
fetched_at: '2026-06-29T00:10:46.709420+00:00'
page_id: '555856270'
product: rm
source: tdn-rm
title: DT- Geração SEFIP - somar todos os valores pagos à autônomos externos no mesmo
  mês
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555856270
version: 5
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Geração SEFIP - Importar autônomos externos (integrados de outros BackOffices) |
| **Situação/Requisito:** | Os autônomos que prestam serviços para o cliente em questão emitem mais que uma nota durante o mês, com isso é gerado e integrado vários títulos para o mesmo autônomo, porém ao gerar o arquivo SEFIP.RE marcando a opção 'Importar autônomos externos (integrados de outros BackOffices)' é gerado vários registros do mesmo autônomo que foram importados para a tabela PPAGTOAUTONOMOEXT, sendo que desta maneira o programa validador do SEFIP (C.E.F), não valida o arquivo gerado, pois não aceita a existência de mais de um registro por (PIS/CPF) e apresenta o erro: “Registro do trabalhador duplicado”. |
| **Solução/Implementação:** | Feito  tratamento na geração do arquivo SEFIP.RE para somar os valores de remuneração dos registros de autônomos que tenham os campos CODFILIAL, CNPJTOMADOR, CEITOMADOR, NROINSCRICAO, CATAUTONOMO, DATAINIATIVIDADE iguais na tabela PPAGTOAUTONOMOEXT. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-9965](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-9965) |
| **Documento de Referência:** | [SEFIP .Net](https://tdn.totvs.com.br/display/LRM/SEFIP+.Net) |
| **Pacote:** | N/A |
