---
content_hash: 234754da4de0229b03d7e89fc1b731e400c2b40d8e84bc5d032d786ee23af527
fetched_at: '2026-06-29T00:08:30.436708+00:00'
page_id: '272432048'
product: rm
source: tdn-rm
title: MEDU-3071 DT Cadastro de Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272432048
version: 112
---

# Cadastro de Patrimônio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Patrimonial. |
| **Função:** | Cadastro de Patrimônio. |
| **Situação/Requisito:** | Atribuía ao campo CODIGOBARRA o valor do campo PATRIMONIO quando parâmetro "Geração do código de barras = Nº do patrimônio" mesmo para registro do tipo Título. Como campo nesse caso é ReadOnly ocorria mensagem de alerta na tela. |
| **Solução/Implementação:** | Implementar a validação do tipo de patrimônio a ser cadastrado para inibir a mensagem caso seja título. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
