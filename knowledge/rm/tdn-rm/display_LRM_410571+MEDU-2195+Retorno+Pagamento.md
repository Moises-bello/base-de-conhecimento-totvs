---
content_hash: c67cbbd370a9cd5fa1fd7ab8060af536727f44aca707d4f2e58dbb4e98411446
fetched_at: '2026-06-29T00:08:27.308883+00:00'
page_id: '271406640'
product: rm
source: tdn-rm
title: 410571 MEDU-2195 Retorno Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/410571+MEDU-2195+Retorno+Pagamento
version: 113
---

# Integração Bancária - Retorno Pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Integracao Bancária - Retorno Pagamento |
| **Situação/Requisito:** | Na importação do arquivo de retorno de pagamento, é apresentado a mensagem:  Linha 00003    Erro lançamento Ref.: - Incorrect Syntax near ')'.Valor pago:  Linha 00003    Erro Lançamento Ref.: - Erro ao preparar a baixa de lançamentos do retorno bancário. Incorrect Syntax near '.16'. |
| **Solução/Implementação:** | Na importação do retorno de pagamento, para os lançamentos recusados pelo banco, o serviço  de cancelamento de baixa é executado para cancelar a baixa destes lançamentos. Foi ajustado filtro do serviço de cancelamento de baixa para não  apresentar a mensagem de erro  Incorrect Syntax near. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito (informe o requisito relacionado):** | FIN000171 |

divs
