---
content_hash: d0910ae325e806be2adee737fba1b810696ef8b5b1bf21b263aaba35472455c3
fetched_at: '2026-06-29T00:08:57.030134+00:00'
page_id: '353272345'
product: rm
source: tdn-rm
title: 2596734 FINANCEIRO01-6356 Baixa do lançamento 'em aberto' quando existe lançamentos
  baixados vinculados ao mesmo boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353272345
version: 3
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Baixa de lançamento com boleto |
| **Situação/Requisito:** | Foram gerados 3 lançamentos do educacional associado a um boleto, sendo que dois lançamentos estão baixados com bolsa de 100%.  Este boleto foi remetido e ao importar o arquivo de retorno é apresentado o seguinte erro:  Erro ao preparar a baixa de lançamento referente a linha 5 do arquivo de retorno bancário. O Lançamento 1-23208 já está baixado. Valor Pago: 1.000,00  No arquivo de retorno existe a chave do lançamento com a referência do boleto e tal boleto está em aberto. |
| **Solução/Implementação:** | Sistema baixa corretamente boleto vinculado a mais de um lançamento, tendo entre esses lançamentos "em aberto" e "baixado". |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 2596734 |
| **Requisito:** | Informe o requisito relacionado. |
| **Documento de Referência:** | Não se aplica |
