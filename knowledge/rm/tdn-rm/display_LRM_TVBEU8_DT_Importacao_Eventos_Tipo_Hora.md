---
content_hash: 2fb303c2dd46e874844922fda3732f48ffaa29dd4cd2366c5c7d30337182f1df
fetched_at: '2026-06-29T00:08:13.968792+00:00'
page_id: '244435297'
product: rm
source: tdn-rm
title: TVBEU8_DT_Importacao_Eventos_Tipo_Hora
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBEU8_DT_Importacao_Eventos_Tipo_Hora
version: 113
---

# IMPORTAÇÃO DE MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Importação de Movimento* |
| **Situação/Requisito:** | Ao realizar a importação de evento do tipo hora diretamente pra o envelope de pagamento com mais de 533,33 horas, o sistema importa o evento com o valor negativo, não é apresentado nenhuma mensagem ou erro informando que o limite é de 533,33 horas por evento.     Cliente deseja que seja criada uma mensagem de erro, informando que o limite de horas e que barre a importação do evento. |
| **Solução/Implementação:** | *Adicionado validação na importação de movimento quando o campo Hora for maior que o limite permitido (546:07).* |
| **Chamados relacionados:** | *TVBEU8* |

divs
