---
content_hash: 67236f0d44fb82e70b6f9accd060259c57b6d5c35637ca52fb6db5f4c36ababe
fetched_at: '2026-06-29T00:06:23.416873+00:00'
page_id: '224102461'
product: rm
source: tdn-rm
title: TTWAEY_DT_Cancelamento_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWAEY_DT_Cancelamento_Rescisao
version: 120
---

# CANCELAMENTO DE RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Cancelamento de Rescisão |
| **Situação/Requisito:** | Ao tentar realizar o cancelamento de rescisão, que possui uma requisição de desligamento concluída, selecionando a opção de 'Cancelar a requisição', o sistema apresenta mensagem de erro. |
| **Solução/Implementação:** | Alteração na forma em que a mensagem será apresentada. A mensagem passará ser mostrada como aviso de Log, dessa forma não impedirá o processo de cancelamento da rescisão. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTWAEY |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.9, 11.82.43 |

divs
