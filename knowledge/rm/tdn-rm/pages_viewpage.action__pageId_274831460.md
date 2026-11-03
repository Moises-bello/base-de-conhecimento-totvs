---
content_hash: f2e9ede8b7f546dda711d3bb6170630e0a881350cd204c716340d616fb8a3cd1
fetched_at: '2026-06-29T00:08:34.670745+00:00'
page_id: '274831460'
product: rm
source: tdn-rm
title: 838446 CONTROLADORIA01-211 DT Registro J100 Contas Sintéticas - ECD (Sped Contábil)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274831460
version: 94
---

# Registro J100 Contas Sintéticas - ECD (Sped Contábil)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Geração do Registro J100 Contas Sintéticas - ECD (Sped Contábil) |
| **Situação/Requisito:** | Ao gerar o Sped no registro J100 os valores das contas analíticas estão corretos, porém os valores das contas sintéticas não estão de acordo com o somatório das analíticas.  Ao comparar o arquivo TXT no registro J100 com o balanço do sistema, os valores das contas sintéticas não batem |
| **Solução/Implementação:** | Ajuste na rotina que retorna o saldo anterior que não consta na tabela CSALDOEXERCICIO para que e mesma passe a contar com filtro por tipo de Natureza do Sped. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
