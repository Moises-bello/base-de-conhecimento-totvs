---
content_hash: 3f39b79a8b8f153542d78aa5f356679e208aad1045e892b189cdb27a46972536
fetched_at: '2026-06-29T00:08:25.627785+00:00'
page_id: '270919470'
product: rm
source: tdn-rm
title: 295199 MRH-3708 DT Verificação da Base de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270919470
version: 110
---

# VERIFICAÇÃO DA BASE DE DADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Verificação da Base de Dados* |
| **Situação/Requisito:** | Após realizar a parametrização para utilizar o rateio fixo por valor e executar a validação da base de dados o sistema continua validando o rateio por percentual e não por valor. |
| **Solução/Implementação:** | Ajustar a validação da base de dados para quando a opção de Utilizar rateio fixo por valor estiver marcada, não realizar validação por percentual, pois somente irá realizar a validação quando a opção de Utiliza cálculo por centro de custo estiver marcada e a opção de Rateio fixo por valor estiver desmarcada. |
| **Tickets relacionados:** | * [295199](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22295199%22 "295199") |

divs
