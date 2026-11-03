---
content_hash: 24effce5fa5113fd4a8890909ea9c937ff517b99fc0b244da996693befdd4d9b
fetched_at: '2026-06-29T00:08:28.942292+00:00'
page_id: '271871712'
product: rm
source: tdn-rm
title: 427841_MEDU-2686_DT_Integração Bancária - Retorno de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271871712
version: 108
---

# Integração Bancária - Retorno de Cobrança

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Integração Bancária - Retorno de Cobrança |
| **Situação/Requisito:** | Ao importar arquivo de retorno, o sistema apresenta a seguinte mensagem: "Linha 00002 Erro Boleto Ref.: - Erro ao preparar a baixa de lançamentos do retorno bancário, ..., Não foi informada uma referência de boleto válida para o(s) lançamento(s) a ser(em) baixado(s). Porém, este lançamento possui uma referência válida e é registrado corretamente, conforme no inicio do log. |
| **Solução/Implementação:** | Otimização no processo de importação de arquivo de retorno por agrupamento de extrato. Agora o sistema realiza o agrupamento corretamente quando o parâmetro de agrupamento de extrato estiver marcado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000169 |

divs
