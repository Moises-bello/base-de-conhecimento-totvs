---
content_hash: cea7af873f6f20fb87003abbf6c4cea2d91564fc85b3809b960c16a6c7092587
fetched_at: '2026-06-29T00:09:02.451972+00:00'
page_id: '379312304'
product: rm
source: tdn-rm
title: 3193643 FINANCEIRO01-7724 DT Cálculo de valor líquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379312304
version: 1
---

# Cálculo de valor líquido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Cálculo de valor líquido |
| **Situação/Requisito:** | Se o parâmetro 'Data Conversão' na opção Conversão de Moeda estiver definido como Vencimento e a flag ‘Usar no cálculo do valor líquido’ estiver habilitada, o valor líquido da visão de lançamento fica diferente do valor líquido na edição do título |
| **Solução/Implementação:** | Quando o parâmetro "Usar no calculo do valor líquido" estiver marcado, na visão e edição de lançamentos o campo data para calculo do valor líquido não será apresentada, e será utilizada a data parametrizada na "Data Conversão" |
| **Conversores e Parâmetros:** | Na etapa Valor Líquido, a opção Conversão de Moeda - Data Conversão deve estar definido como Vencimento e a opção Usar no cálculo do valor líquido. |
| **Tickets relacionados:** | 3193643, 2142434 |
| **Requisito:** | FINANCEIRO01-7724 |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
