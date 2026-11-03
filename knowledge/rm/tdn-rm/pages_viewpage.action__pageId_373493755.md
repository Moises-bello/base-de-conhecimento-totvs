---
content_hash: e993dba307f9c8fd442f4a3ce6a940eb7f568c167717ff79b3974eb35852e968
fetched_at: '2026-06-29T00:09:01.572763+00:00'
page_id: '373493755'
product: rm
source: tdn-rm
title: 2659128 FINANCEIRO01-7558 DT Saldo Inicial Incorreto do Relatório Extrato Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=373493755
version: 1
---

# Relatórios - Extrato de Cliente/Fornecedor

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Relatórios - Extrato de Cliente/Fornecedor |
| **Situação/Requisito:** | Ao emitir o relatório de "extrato de cli/for" contido na aba "Gestão financeira", o sistema apresenta valores negativos para determinados cli/for. Isto ocorre mesmo se o cli/for tiver somente lançamentos a pagar. O valor não deve ficar negativo. |
| **Solução/Implementação:** | Otimização no processo de geração de relatório extrato cliente/fornecedor. Agora o sistema trata corretamente os valores de baixa parcial para lançamento da baixa antiga. Obs.: Criado o script para excluir item de baixa para lançamentos faturados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000230 |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
