---
content_hash: 6ba24d7b2fa3b064e06cf23df0c474abf0c5a4d44d5b5ec1eb8d470693614d45
fetched_at: '2026-06-29T00:10:46.705681+00:00'
page_id: '555856217'
product: rm
source: tdn-rm
title: DT- Geração SEFIP - Base de Cálculo de INSS - Autônomos externos carreteiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555856217
version: 2
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Geração SEFIP - Importar autônomos externos (integrados de outros BackOffices) |
| **Situação/Requisito:** | Ao importar o arquivo de autônomos externos, o campo 'Valor da Remuneração' é alimentado com o valor integral do frete e quando geramos o arquivo SEFIP.RE, é levado o valor integral como base de cálculo do INSS. Neste caso o valor da base de INSS fica incorreto, pois para autônomos carreteiros com a categoria 15 e CBO 782510, deveria calcular somente 20% sobre o valor da remuneração para compor a base de INSS levada no arquivo SEFIP.RE |
| **Solução/Implementação:** | Feito  tratamento na geração do arquivo SEFIP.RE para calcular o valor de 20% (vinte por cento) sobre o valor do campo 'valor da remuneração' e levar como base de cálculo de INSS, para autônomos carreteiros com a categoria 15 e CBO 782510. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-10032](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10032) |
| **Documento de Referência:** | [SEFIP .Net](https://tdn.totvs.com.br/display/LRM/SEFIP+.Net) |
| **Pacote:** | N/A |
