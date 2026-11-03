---
content_hash: 8644da6ec364d507183c9433cae138173f79e55cc668c0455726910622c60f8b
fetched_at: '2026-06-29T00:08:22.306073+00:00'
page_id: '269421256'
product: rm
source: tdn-rm
title: 182873_Codigo_Sequencial_Cliente_Fornecedor_Integracao_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/182873_Codigo_Sequencial_Cliente_Fornecedor_Integracao_Protheus
version: 115
---

# Geração de código sequencial de cliente/fornecedor, quando parametrizado no TOTVS Gestão Financeira, para a integração por mensageria única

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Cadastro Cliente/Fornecedor |
| **Situação/Requisito:** | Ao cadastrar um cliente/fornecedor no Protheus com mesmo código em lojas diferentes é gerado erro de violação de chave estrangeira, devido a duplicação de código. |
| **Solução/Implementação:** | Melhoria na integração para que possa obedecer o comportamento do parâmetro do financeiro para geração de código sequencial para o Cliente/Fornecedor.   * Caso o parâmetro: BackOffice | Gestão Financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira   + 02.02 - Contas a Receber | 02.02.01 - Manutenção de lançamentos | 02.02.01.01 - Lançamento     - Cliente / Fornecedor | Usar código sequencial (se máscara for numérica) |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | MEDU-1215 |
| **Requisito (ISSUE):** | N/A |

divs
