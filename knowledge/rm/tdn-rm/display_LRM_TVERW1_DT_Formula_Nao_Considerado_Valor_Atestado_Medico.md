---
content_hash: 9d3a43e40e37772ec5e0a9788823b4af90d27d317d63f2a747b0d407453c7670
fetched_at: '2026-06-29T00:08:15.477808+00:00'
page_id: '244741118'
product: rm
source: tdn-rm
title: TVERW1_DT_Formula_Nao_Considerado_Valor_Atestado_Medico
type: documentation
url: https://tdn.totvs.com/display/LRM/TVERW1_DT_Formula_Nao_Considerado_Valor_Atestado_Medico
version: 110
---

# CÁLCULO FOLHA DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Cálculo da Folha de Pagamento* |
| **Função:** | *Cálculo de Fórmula* |
| **Situação/Requisito:** | Cliente utiliza a função BASECALCULO na fórmula de um evento onde retorna a Base de INSS Total, porém quando é lançado o evento de ATESTADO CC 145, a Base de INSS do Evento de Atestado não compõe a função BASECALCULO do evento onde é retornado um valor incorreto. |
| **Solução/Implementação:** | *Ajustado o lançamento do atestado médico para que seja considerado em fórmula quando o lançamento não for por grupo de eventos.* |
| **Chamados relacionados:** | *TVERW1* |

divs
