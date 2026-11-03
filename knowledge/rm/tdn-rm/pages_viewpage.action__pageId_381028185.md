---
content_hash: a38c51709d4082dd2e7a813e392fe4c79d62c5b11c345cddd2d1e0bc2b1c8846
fetched_at: '2026-06-29T00:09:02.875174+00:00'
page_id: '381028185'
product: rm
source: tdn-rm
title: 898262 CONTROLADORIA01-1656 Configurações Cartão de Crédito/Débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381028185
version: 4
---

# Configurações Cartão de Crédito/Débito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Configurações Cartão de Crédito/Débito |
| **Situação/Requisito:** | Ao acessar a parametrização referente a pagamento via cartão de crédito (checkout), não está sendo possível escolher um Meio de Pagamento que esteja cadastrado com o Tipo Primitivo Cartão de Débito. Como é possível realizar a operação também através de cartão de débito, este tipo primitivo também deve ser considerado no loockup relacionado ao meio de pagamento. |
| **Solução/Implementação:** | Ajuste na tela de parametrização de meio de pagamento para que ao ativar a função débito seja exibido no lookup meios de pagamento do tipo primitivo "Cartão de Débito". |
| **Conversores e Parâmetros:** | Totvs Gestão Financeira > Avançar > 02.02 – Contas a Receber > 02.02.02 – Baixas > 02.02.02.03 – Cartão de Crédito/Débito > Avançar > Bandeira 1/3  Totvs Gestão Financeira > Avançar > 02.02 – Contas a Receber > 02.02.02 – Baixas > 02.02.02.03 – Cartão de Crédito/Débito > Avançar > Bandeira 2/3 |
| **Tickets relacionados:** | 898262 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A. |
