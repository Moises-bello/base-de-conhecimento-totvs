---
content_hash: 439995e9208d4f5c3d5f50a71f4b770f46e0428a1b9ee5abd697479072d75a9c
fetched_at: '2026-06-29T00:08:20.735958+00:00'
page_id: '268586575'
product: rm
source: tdn-rm
title: TVWOZL_DT_Parametro_Proporcionalizar_eventos_considerando_dias_atestado_medico
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWOZL_DT_Parametro_Proporcionalizar_eventos_considerando_dias_atestado_medico
version: 115
---

# Parametrizador

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Comportamento do Parâmetro: "Proporcionalizar eventos considerando os dias de atestado médico"* |
| **Situação/Requisito:** | O sistema não está considerando para o cálculo da proporcionalidade do evento, os dias de afastamento. Ele deve proporcionalizar os dias de afastamento de forma integral, sem considerar os 15 primeiros dias da empresa. |
| **Solução/Implementação:** | Para o sistema proporcionalizar os dias de afastamento sem considerar os 15 primeiro dias da Empresa foi criado o parâmetro "Proporcionalizar eventos considerando os dias de atestado médico". Em que:      * Caso esteja marcado no cadastro de evento a proporcionalidade no afastamento e este parâmetro, o sistema irá proporcionalizar também os dias de atestado. * Caso esteja marcado apenas o parâmetro do cadastro de evento, o sistema irá proporcionalizar, mas não irá considerar os 15 primeiros dias de atestado médico. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TVWOZL.* |
| **Requisito (ISSUE):** |  |

divs
