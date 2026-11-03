---
content_hash: 5c5e1cd707e954ae563610bd718267af14ab902ed1f1b72a9f205b4be4431295
fetched_at: '2026-06-29T00:08:55.826202+00:00'
page_id: '351017053'
product: rm
source: tdn-rm
title: 2367950 FINANCEIRO01-5788 DT Baixa com perda financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/2367950+FINANCEIRO01-5788+DT+Baixa+com+perda+financeira
version: 2
---

# BAIXA COM PERDA FINANCEIRA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa com perda financeira |
| **Situação/Requisito:** | Ao realizar a 'Baixa com Perda Financeira' de um lançamento que possui o tipo de documento com classificação 'Adiantamento', o sistema apresenta erro informando que 'Não é permitido lançamento com valor original igual a zero', a mensagem é apresentada pelo fato de lançamentos de adiantamento geraram um crédito de adiantamento no momento da baixa e nos parâmetros do sistema o parâmetro 'Permite Lançamentos Zerados' está desabilitado na etapa de 'Inclusão' das contas a pagar. |
| **Solução/Implementação:** | Otimizado o processo de baixa com perda financeira de lançamentos de adiantamento para não gerar o crédito de adiantamento. |
| **Tickets relacionados:** | N/A |
