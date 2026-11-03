---
content_hash: 9608c9c2e913292735366b057c580c65f825d3c8f9a842786485ead0d782a604
fetched_at: '2026-06-29T00:06:21.244024+00:00'
page_id: '223165990'
product: rm
source: tdn-rm
title: TTWMTS_DT_Requisicao_De_Substituicao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWMTS_DT_Requisicao_De_Substituicao
version: 1
---

# REQUISIÇÃO DE SUBSTITUIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Requisição de Substituição* |
| **Situação/Requisito:** | *Verificamos que o campo Salário existente na requisição do tipo Substituição, tanto na aplicação quanto na visualização da requisição no portal, está apresentando o valor da hora e não o valor do salário cheio.* |
| **Solução/Implementação:** | *Ajuste no geração da Requisição de Substituição, quando o funcionário é horista. Se o sistema estiver configurado para considerar tabelas salariais, é verificado na Tabela Salarial se o funcionário é horista. Caso contrário, é verificado no tipo de recebimento. Quando o funcionário for horista, a Requisição de Substituição gerada exibirá o seu Salário Hora, informando que a vaga é horista. Caso contrário, será exibido o salário mensal.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTWMTS* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.9* |

divs
