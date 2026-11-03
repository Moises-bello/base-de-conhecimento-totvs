---
content_hash: 81b345b0a089d13cddd0a2e3194f04e6e189d9347d28df955d5924eb0aeb6174
fetched_at: '2026-06-29T00:08:26.313294+00:00'
page_id: '271174298'
product: rm
source: tdn-rm
title: 275624 MRH-4840 DT Integração de funcionário (BackOffice RM x SigaMNT)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271174298
version: 112
---

# INTEGRAÇÃO DE FUNCIONÁRIO (BACKOFFICE RM X SIGAMNT)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Integração BackOffice RM x SigaMNT* |
| **Situação/Requisito:** | *A integração via mensageria única 1001 (BackOffice RM x SigaMNT) define que todas as mensagens do RM seriam disparadas por fórmula visual. Foi realizado uma alteração no produto que diz que se a entidade EMPLOYEE versão 2.003 estiver mapeada numa integração ativa, serão disparadas mensagens na atualização do funcionário, o que está em desacordo com a premissa citada da integração 1001.* |
| **Solução/Implementação:** | *Se a integração 1001 (BackOffice RM x SigaMNT) estiver habilitada e a entidade EMPLOYEE estiver mapeada a partir da versão 2.003, a mensagem não será disparada via código, para os clientes MANSERV e SONORA, sendo disparada pelo gatilho definido na fórmula visual.* |
| **Tickets relacionados:** | *MRH-4840,* *MRH-4344* |

divs
