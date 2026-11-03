---
content_hash: f3b68d63fcfc5aea8580f2e3b5620c8158d46d65eae9304d9bf0747448fd4a8e
fetched_at: '2026-06-29T00:10:22.790667+00:00'
page_id: '499108712'
product: rm
source: tdn-rm
title: DT Motivos de baixa na Integração com Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499108712
version: 4
---

# BAIXA DE LANÇAMENTO/RETORNO DE COBRANÇA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | BackOffice |
| **Módulo:** | Gestão Financeira |
| **Função:** | Baixa de Lançamento/Retorno de Cobrança |
| **Situação/Requisito:** | Criação de um campo na tela de baixa manual e retorno de cobrança para que seja informado o motivo de baixa, a partir de uma tabela dinâmica, para a integração com Protheus. |
| **Solução/Implementação:** | Otimizado o processo de baixa manual e retorno de cobrança com a criação do campo "Motivo de Baixa (Protheus)", quando ativa a nova integração Educacional x BackOffice Protheus ou a integração TIN x BackOffice Protheus EAI 2.0.  Deve ser criada uma tabela dinâmica com o nome BXPROTHEUS com a finalidade "2 - validação de campos complementares" e visível para todas as coligadas, em Serviços Globais | Cadastros | Tabela Dinâmica para o sistema Gestão Financeira.    As informações da tabela dinâmica devem ser obrigatoriamente preenchidas conforme o video acima:  **Código**: BXPROTHEUS  **Visível a todas coligadas**: Marcado  **Finalidade**: 2 – Validação de Campos Complementares.  Em anexos > “Item da tabela dinâmica”, insira com os mesmos códigos existentes na Tabela de Motivo de Baixa do Protheus. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-12537 |
| **Documento de Referência:** | N/A |
| **Pacote:** | 12.1.26 |
