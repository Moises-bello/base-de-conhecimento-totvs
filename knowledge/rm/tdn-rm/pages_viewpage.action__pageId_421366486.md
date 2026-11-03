---
content_hash: 071af8a49ab9a785188453d4ce7c054900c0347ed4eec194cff24c1564c0026d
fetched_at: '2026-06-29T00:09:13.512303+00:00'
page_id: '421366486'
product: rm
source: tdn-rm
title: 3852646 MATESTCNTFTOF01-3398 DT Ajuste na Validação de Condição de Pagamento
  de Contrato e Item de Contrato segundo a Natureza
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421366486
version: 5
---

# VALIDAÇÃO DE CONTRATO E ITEM DE CONTRATO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Menu | *BackOffice* | Gestão Estoque, Compras e Faturamento | Contratos | Manutenção de Contrato (Inclusão ou Alteração) |
| **Situação/Requisito:** | Ao criar um contrato, o campo **Natureza Contrato** deve ser preenchido com a opção Venda, Compra ou Ambos. Após isso o campo **Código da Condição de Pagamento** deve ser preenchido com uma condição de pagamento, porém o sistema não valida se o **Tipo de Plano** informado dentro da condição de pagamento é o mesmo da natureza do contrato, da mesma forma que ocorre na movimentação. Com isso o usuário pode inserir uma condição de pagamento de Compra em um contrato de Venda, mas ao faturar o item de contrato será apresentada uma inconsistência ao usuário. |
| **Solução/Implementação:** | Foi adicionada uma validação de Condição de Pagamento tanto para Contrato quanto para Item de Contrato segundo a Natureza.  Assim o código de pagamento deverá estar em conformidade seguindo a seguinte prioridade: 1º Natureza do item de contrato; 2º Natureza do contrato |
| **Tickets Relacionados:** | 3852646 |
| **Requisito:** | MATESTCNTFTOF01-3398 |
