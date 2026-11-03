---
content_hash: 7e7158aeddfb17775c3a25822d398cd3d9a2ae0049912aa371a672b17ce5be23
fetched_at: '2026-06-29T00:08:32.705676+00:00'
page_id: '273996651'
product: rm
source: tdn-rm
title: 711396 Financeiro01-536 Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/711396+Financeiro01-536+Baixa
version: 115
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa de lançamentos. |
| **Situação/Requisito:** | Ao baixar um lançamento de "Devolução" gerado a partir de um "Distrato" realizado no TIN (novo modelo integração TIN x Financeiro), o processo de baixa não está sendo concluído, pois, o processo de finalização dos lançamentos parcialmente baixados não está sendo concluído para lançamentos que estão com contabilização no modelo antigo, apresentando a mensagem:  Erro ao salvar dados da venda [4898].Campo "ValorOriginal" do lançamento "37-518" não pode ser alterado em: - Lançamentos Exportados para Contabilidade” |
| **Solução/Implementação:** | Ajustado serviço de alteração de lançamento, para não validar se a contabilidade esta exportada quando serviço estiver sendo utilizado pelo processo de finalização do lançamento. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000040 |

divs
