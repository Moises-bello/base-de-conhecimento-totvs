---
content_hash: 6e27e16e27eee55173a15e1b15e53cafc76524e10a1ac8b8ca8a045673ee265a
fetched_at: '2026-06-29T00:08:17.059765+00:00'
page_id: '252051511'
product: rm
source: tdn-rm
title: TVQAIC_DT_Excluir_Evento_Movimento_Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=252051511
version: 114
---

# CONSULTA MOVIMENTO DE INTEGRAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Consulta Movimento de Integração* |
| **Situação/Requisito:** | *Ao acessar o movimento de integração dos funcionários, ao tentar excluir um* *evento de horas extras com mais de 728 horas vindo do CHRONUS, é apresentada a mensagem* *de erro "Valor era muito grande ou muito pequeno para Int16"* |
| **Solução/Implementação:** | *Ajuste no tipo do valor HORA para Int32.* |
| **Chamados relacionados:** | *TVQAIC* |

divs
