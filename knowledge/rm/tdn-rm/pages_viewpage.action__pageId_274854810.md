---
content_hash: 100d516f9fabfcf2785fe3a686473d28e60b356a0e0d7fa4459efd98679c02fe
fetched_at: '2026-06-29T00:08:34.943700+00:00'
page_id: '274854810'
product: rm
source: tdn-rm
title: DT DDA - Conciliar Títulos em Cobrança pela "Raiz do CNPJ"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274854810
version: 7
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção* *& Projetos* |
| **Módulo:** | *Totvs Gestão Financeira.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *DDA* | *Débito Direto Autorizado.* | |
| **Requisito/S****tory/Issue:** | FINANCEIRO01-872 |
| **País(es):** | *BRASIL* |

## Descrição

Permite o usuário realizar a Conciliação de Títulos em Cobrança pela Raiz do CNPJ do Cliente/Fornecedor.

## Procedimento para Utilização

No Totvs Gestão Financeira | Movimentações Bancárias | Integração Bancária | DDA - Débito Direto Autorizado | Processos | Conciliar Título em Cobrança o campo Raiz Do CNPJ estará disponível para conciliação do título.

Obs.: Ao selecionar somente o campo Raiz do CNPJ e realizar a conciliação, o sistema irá buscar o primeiro lançamento que possua a Raiz de CNPJ para ser conciliado.

O sistema busca os 8 primeiros dígitos do CNPJ:

CNPJ: **63.858.023**/0001-51

Raiz do CNPJ: **63.858.023**

No lançamento financeiro o campo "CPF/CNPJ" na aba Identificação é utilizado para buscar a Raiz do CNPJ. Posteriormente a Raiz do CNPJ do lançamento é comparado com os 8 primeiros dígitos do campo "Inscrição do Cedente" para conciliar o título ao lançamento.
