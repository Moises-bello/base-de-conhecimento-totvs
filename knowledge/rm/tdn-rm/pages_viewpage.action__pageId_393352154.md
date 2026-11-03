---
content_hash: 5b7bc2a899cbd6cf43eaf3ac5bca3a732cc57469a3015c76d68762e251f4da69
fetched_at: '2026-06-29T00:09:09.202970+00:00'
page_id: '393352154'
product: rm
source: tdn-rm
title: 3339651 FOPCALCULO01-4498 - Histórico de Provisão - Fórmula de valor a somar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393352154
version: 1
---

# Histórico de Provisão

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Geração do Histórico de Provisão |
| **Situação/Requisito:** | Ao utilizar uma fórmula com o resultado negativo nos campos "Valor a somar na provisão de férias vencidas" e "Valor a somar na provisão de férias proporcionais" em configurações|Parametrizador|Férias|Fórmulas e marcando o parâmetro "Considera valor negativo de fórmula a somar p/ férias vencidas e proporcionais", o sistema não considera a fórmula para cálculo, apresentando a mensagem abaixo no log da geração da provisão:  "Fórmula para somar ao valor da Provisão de Férias Vencidas: provnega  Fórmula provnega não retornou valor" |
| **Solução/Implementação:** | Ajuste no cálculo de provisão de férias para considerar fórmulas negativas para Férias Proporcionais e Vencidas de acordo com o parâmetro: "Considera valor negativo de fórmula a somar p/ férias vencidas e proporcionais" |
| **Tickets relacionados:** | 3339651 |
