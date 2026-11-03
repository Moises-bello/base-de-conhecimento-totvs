---
content_hash: 2a29c98428df604838379b926fda9d93b83dd8341dfef388c4d27c9647055b77
fetched_at: '2026-06-29T00:09:52.954289+00:00'
page_id: '439704800'
product: rm
source: tdn-rm
title: 2057581 CONTROLADORIA01-1042 DT Evolução do Relatório Cliente Fornecedor /
  Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439704800
version: 4
---

# Evolução do Relatório Cliente Fornecedor / Contábil

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Evolução do Relatório Cliente Fornecedor / Contábil |
| **Situação/Requisito:** | Foi feita uma baixa no RM Fluxus no dia 30/04 e executada a contabilização desta baixa. Em seguida essa contabilização foi integrada ao lote zero. Neste momento, se emitirmos o relatório Razão Cliente Fornecedor/Contábil para a conta de cliente/fornecedor utilizada na baixa, o saldo deste relatório fecha corretamente com o saldo apresentado no relatório "Extrato Cliente/Fornecedor". Após cancelar a baixa no RM Fluxus ocorre a inconsistência descrita abaixo.  No momento que a baixa é cancelada no Fluxus no dia 05/05, por exemplo, é gerado um estorno nesta data. Após o estorno é integrado ao lote zero. O que ocorre é que se for emitido o relatório Cliente Fornecedor/ Contábil no dia 30/04 os valores passam a não fechar, pois neste dia no Saldus a contabilização da baixa é apresentada e no relatório de Extrato Cliente Fornecedor do lado do financeiro a baixa já foi cancelada. Portanto é preciso que o relatório do lado contábil consiga fechar os valores com o financeiro quando ocorrer estas situações. |
| **Solução/Implementação:** | Evolução do relatório Razão Cliente Fornecedor / Contábil para que seja possível parametrizar se serão exibidos ou não os lançamentos do tipo Estorno/Estornado. Utilizando o parâmetro "Não exibir lançamentos de Estorno/Estornado", disponível apenas para este tipo de relatório, será possível utilizar o recurso. A evolução visa ajudar na comparação de dados com o relatório de cliente fornecedor do módulo financeiro. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
