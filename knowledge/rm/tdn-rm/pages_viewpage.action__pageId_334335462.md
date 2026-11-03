---
content_hash: f59011cb49b006d0cffdb0a653c4d7c0b8a01db6dec86781eb66a21ee4861b44
fetched_at: '2026-06-29T00:08:50.715569+00:00'
page_id: '334335462'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-1605 DT Geração de Fatura para Lançamentos do Educacional com
  Valores de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334335462
version: 2
---

# Inclusão de Faturas para Lançamentos do Educacional com Valores de Integração

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Inclusão de Faturas* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FIN000083 |
| **País(es):** | *Brasil* |

## Descrição

Possibilita a geração de faturas para lançamentos do Educacional, com valores de integração.

## Procedimento para Utilização

**Exemplo:**

1. Partindo de um lançamento gerado pelo educacional:
2. Considere os valores de integração associados:
3. Após executar a fatura:
4. O vencimento de fatura é gerado com os respectivos valores de integração:
5. O vencimento de fatura será baixado levando os valores de integração:

**Observação:**

Quando um lançamento do Educacional é submetido ao procedimento de fatura, o lançamento gerado é sempre um lançamento Financeiro, não estando assim submetido a regra de negócio do Educacional.

Neste sentido, os valores de integração compõem o lançamento apenas para a composição do valor líquido. Tratamentos como pagamento a maior, ou a menor, com reflexo ao conta corrente do aluno não serão executados.

A forma mais adequada para agrupar, desdobrar, ajustar valores e prazos é o processo de acordo.
