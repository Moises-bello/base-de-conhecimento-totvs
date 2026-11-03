---
content_hash: 7621b96a6b64afaf7ce3674e1c427d422fcfa41ada1e3295b31f8e6dfe45c47f
fetched_at: '2026-06-29T00:08:25.729506+00:00'
page_id: '270924549'
product: rm
source: tdn-rm
title: MEDU-1948 DT Remetente Email Envio Automatico Final Pesquisa Opiniao
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1948+DT+Remetente+Email+Envio+Automatico+Final+Pesquisa+Opiniao
version: 112
---

# ENVIO DE E-MAIL AUTOMÁTICO AO FINAL DA AVALIAÇÃO DE PESQUISA DE OPINIÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Avaliação e Pesquisa* |
| **Função:** | *Envio de e-mail automático ao final da avaliação de pesquisa de opinião* |
| **Situação/Requisito:** | *Foi identificado que quando o parâmetro de tipo de remetente para envio de e-mail está configurado para usuário logado o sistema não envia o e-mail ao final da avaliação do tipo pesquisa de opinião.* |
| **Solução/Implementação:** | *Foi identificado que quando configurado para o remetente o usuário logado, o usuário do contexto é utilizado, porém os executores de prova utilizam usuários genéricos para montar o contexto que não possuem e-mail e ao enviar o email o serviço da framework não consegue detectar o email de remetente pois não encontra o usuário, sendo assim foi alterado para utilizar a configuração global de envio quando ocorrer esta situação, não impedindo assim o envio do e-mail ao finalizar a avaliação.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
