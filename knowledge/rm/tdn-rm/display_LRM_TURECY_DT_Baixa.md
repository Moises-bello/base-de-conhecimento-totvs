---
content_hash: 0bb37deacc1debd226ee376e350e9b72f66232309f16d53bc3188cf5ca5a9928
fetched_at: '2026-06-29T00:08:04.766029+00:00'
page_id: '235581175'
product: rm
source: tdn-rm
title: TURECY_DT_Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TURECY_DT_Baixa
version: 118
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa. |
| **Situação/Requisito:** | Ao baixar um cheque onde não existe cotação para o item de baixa que representa o cheque, está apresentando erro divisão por zero. |
| **Solução/Implementação:** | Ajuste no serviço de baixa para verificar se o item de baixa tem cotação, e somente se existir, aplicar a cotação aos valores. |
| **Conversores e Parâmetros:** | NA. |
| **Chamados relacionados:** | NA. |
| **Requisito (ISSUE):** | FIN000040. |

divs
