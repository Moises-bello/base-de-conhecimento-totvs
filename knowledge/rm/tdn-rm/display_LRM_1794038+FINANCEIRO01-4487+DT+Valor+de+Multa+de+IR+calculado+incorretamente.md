---
content_hash: b07159bf54463c178206b713962b6c54a56faf2ba06ee80aad8b4d91702e1eb7
fetched_at: '2026-06-29T00:09:08.431037+00:00'
page_id: '389546280'
product: rm
source: tdn-rm
title: 1794038 FINANCEIRO01-4487 DT Valor de Multa de IR calculado incorretamente
type: documentation
url: https://tdn.totvs.com/display/LRM/1794038+FINANCEIRO01-4487+DT+Valor+de+Multa+de+IR+calculado+incorretamente
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Inclusão de Lançamento com Classificação Gerador de IR |
| **Situação/Requisito:** | Ao executar a inclusão de lançamento, com classificação Gerador de IR, na data 10/10/2017, o lançamento de IR associado foi incluído com data de vencimento 17/11/2017, quando o correto deveria ser 20/11/2017. |
| **Solução/Implementação:** | Constatamos que o problema ocorreu porque no dia 20/11/2017 havia cadastrado um feriado estadual, sendo a data uma segunda-feira, o sistema buscou o primeiro dia útil anterior (17/11/2017). Ao executar a baixa deste lançamento com atraso, o sistema contabilizou um dia útil a mais, elevando o valor da multa devida. Um ajuste foi executado de modo que a existência de um feriado local não afete a criação do lançamento do imposto. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 1794038 |
| **Requisito:** | FIN000263 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | Não se aplica |
