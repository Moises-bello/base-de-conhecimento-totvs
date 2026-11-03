---
content_hash: 9aa9e064ec85122706f69d3e80afabf5ae9c91161733bbd601bfc23ffc9a4487
fetched_at: '2026-06-29T00:06:28.127297+00:00'
page_id: '233748218'
product: rm
source: tdn-rm
title: TTGO17_DT_SINDICATO_Ignora_Feriados_Contagem_Ferias_Normais
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGO17_DT_SINDICATO_Ignora_Feriados_Contagem_Ferias_Normais
version: 115
---

# Sindicato

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parâmetros de Férias* |
| **Situação/Requisito:** | Individualizar o tratamento referente a feriados de férias normais e férias coletivas criando mais um parâmetro no cadastro de sindicato. |
| **Solução/Implementação:** | Foi Criado no cadastro de sindicato na aba de férias o campo "Ignora feriados na contagem das férias Normais" e foi alterado o campo "Ignora feriados na contagem das férias" para "Ignora feriados na contagem das férias Coletivas".  No cadastro de individual de férias pela visão do funcionário ou pelo módulo de férias coletiva quando o flag "Coletivas" estiver desmarcado o sistema irá considerar a parametrização do campo  "Ignora feriados na contagem das férias Normais".  No modulo de férias coletivas quando o flag "Coletivas" estiver marcado o sistema irá considerar a parametrização do campo  "Ignora feriados na contagem das férias Coletivas". Uma vez que as férias sejam gravadas como coletiva no cadastro de férias individual o flag Coletivas continua sendo considerado. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGO17* |
| **Requisito (ISSUE):** |  |

divs
