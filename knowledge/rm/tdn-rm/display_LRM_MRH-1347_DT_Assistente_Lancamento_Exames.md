---
content_hash: cacee714225f42cadc4844f746ed46b4089c3b300ec004559bddbdda115bbc35
fetched_at: '2026-06-29T00:08:22.409425+00:00'
page_id: '269432395'
product: rm
source: tdn-rm
title: MRH-1347_DT_Assistente_Lancamento_Exames
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-1347_DT_Assistente_Lancamento_Exames
version: 110
---

# ASSISTENTE DE LANÇAMENTO DE EXAMES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Assistente de Lançamento de Exames |
| **Situação/Requisito:** | - Assistente de lançamento de exames estava trazendo os campos de data de agendamento e pendência incorretos dependendo do filtro selecionado. - Assistente estava exibindo colunas "IsInserting" e "Chapa" quando as mesmas não deveriam ser exibidas. |
| **Solução/Implementação:** | Foi ajustado o grid para trazer as datas dos exames corretamente conforme filtro informado no assistente.  Para os exames que não possuem data de pendência, foi atribuída a data fixa 01/01/1900 e para os que não possuem data de agendamento, o grid carregava automaticamente 01/01/0001. Os dois casos foram alterados para exibir o campo vazio. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | MRH-1347 |
| **Requisito (ISSUE):** |  |

divs
