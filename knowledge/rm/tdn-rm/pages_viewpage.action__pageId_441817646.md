---
content_hash: 474a4e9f17e53ade55e4032d4ba1a6742f7ed297301d6101c7b6ae86f5a66db3
fetched_at: '2026-06-29T00:09:53.755696+00:00'
page_id: '441817646'
product: rm
source: tdn-rm
title: 4032244 FINANCEIRO01-10195 DT Relatorio Extrato Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=441817646
version: 1
---

# EXTRATO CLIENTE/FORNCEDOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Relatório de Extrato Cliente/Fornecedor |
| **Situação/Requisito:** | Apos migrar da versão 12.1.17 para a versão 12.1.19 o Saldo Anterior/Inicial ficou incorreto.  TESTES REALIZADOS: Acessei a base "4032244\_ENGIMPLAN12119" na coligada 1, apos acessei a aba 'Gestão Financeira'>>Extrato de Cliente/Fornecedor. Na geração do relatório informei os seguintes parâmetros:  Filial = 1 Cliente/Fornecedor: "C0028 - HOSPITALIA CIRURGICA CATARINENSE LTDA" Data Inicial: 01/06/2018 Data Final: 30/06/2018 Desmarquei as opções "A Pagar" e "Fornecedores". Habilitei os parâmetros "Considerar Valor do Adiantamento para o valor do lançamento" e Mostrar Devoluções nos lançamentos só pagar e só a receber". Selecionei o relatório "FINREL0024 - Extrato de cliente/fornecedor. |
| **Solução/Implementação:** | Otimização das consultas sql para tratar corretamente os valores do itens de baixa dos lançamentos baixados parcialmente no modelo antigo de baixa. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | 12.1.19, 12.1.22, 12.1.23 |
