---
content_hash: c44f074103e40bc01085a3a1795f635ac16696eca589f4bda94e8e49cbf8e650
fetched_at: '2026-06-29T00:08:27.249332+00:00'
page_id: '271401840'
product: rm
source: tdn-rm
title: 94516 MEDU-233 Baixa Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271401840
version: 110
---

# Baixa de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa |
| **Situação/Requisito:** | O sistema faz o calculo de impostos (PIS,COFINS,CSLL) quando ocorrem baixas parciais em lançamento de 'contas a receber' com clientes que sejam de sociedade mista, calculado com base no valor líquido de cada baixa, quando o correto é calcular com base no valor BRUTO de cada baixa. |
| **Solução/Implementação:** | Implementado no formulário de baixa e recebimento de cheque, o campo 'Base de Cálculo dos Tributos', para que seja informada a base de cálculo que deve ser utilizada para geração de tributos em baixa parcial. Este campo estará disponível somente para lançamentos a receber que possuem tributos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A. |
| **Requisito (informe o requisito relacionado):** | FIN000040. |

divs
