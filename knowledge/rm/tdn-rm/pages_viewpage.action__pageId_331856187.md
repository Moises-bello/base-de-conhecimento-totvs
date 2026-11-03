---
content_hash: 4f4ae9c6805fe90e651351c2e34d21d5da20227554735b73dad9f681f2eb1d85
fetched_at: '2026-06-29T00:08:49.702128+00:00'
page_id: '331856187'
product: rm
source: tdn-rm
title: DT Inclusão boleto ao cancelar fatura para lançamentos do educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331856187
version: 2
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **TOTVS Gestão Financeira*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cancelar Fatura.* | *Cancelar Fatura.* | |
| **Cadastros Iniciais:** | *Geração de lançamento do TOTVS Educacional.*  *Geração de fatura para o lançamento.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FINANCEIRO01-4574 |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle e SQL Server.* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Quando sistema estiver corretamente parametrizado para permitir a geração de fatura de lançamentos do TOTVS Educacional, ao cancelar a fatura gerada a partir desse tipo de lançamento será incluído novo boleto para o lançamento faturado.

## Procedimento para Utilização

1-Sistema precisa está configurado para permitir a geração de fatura a partir de lançamentos do TOTVS Educacional (parametrizado para não utilizar cobrança retroativa).

TOTVS Educacional | Integração | Financeiro | Educacional | Fin - Cobrança Retroativa:

* Alunos com crédito na instituição = Não efetuar operação
* Alunos em débito com a instituição = Não efetuar operação

2-Gerar lançamento a partir do TOTVS Educacional

3-Executar o processo de geração de fatura para o lançamento do TOTVS Educacional. Nesse momento, caso o boleto relacionado ao lançamento tenha status Não Remetido, Pendente de Remessa ou Recusado, ele será cancelado.

4-Ao executar o processo de cancelamento da fatura gerada, será gerado um novo boleto para o lançamento faturado.
