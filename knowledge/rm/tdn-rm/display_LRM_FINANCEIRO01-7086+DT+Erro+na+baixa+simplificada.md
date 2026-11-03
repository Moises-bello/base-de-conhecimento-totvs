---
content_hash: 5b9f3322a826fd760523e5f75588ba9b64b80ee32a05aaab7584a3a19aa9c97f
fetched_at: '2026-06-29T00:08:59.457080+00:00'
page_id: '362455352'
product: rm
source: tdn-rm
title: FINANCEIRO01-7086 DT Erro na baixa simplificada
type: documentation
url: https://tdn.totvs.com/display/LRM/FINANCEIRO01-7086+DT+Erro+na+baixa+simplificada
version: 2
---

# Inconsistência na inclusão de baixa simplificada

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | Ao realizar a baixa simplificada ir e voltar na navegação da baixa, o sistema cria uma forma de pagamento default que não estava sendo apagada. Desta forma o sistema entendia que não era possível realizar a baixa com valor de desconto de pontualidade, pois tal valor só é gerado com uma baixa completa onde o valor da baixa deve ser igual ao valor liquido. |
| **Solução/Implementação:** | Agora o sistema limpa as formas de pagamento na baixa simplificada sempre que o usuário volta na navegação. |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |
