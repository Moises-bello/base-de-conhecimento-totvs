---
content_hash: ee4b7958debf11012462d4c9b88717e5d72e78fa10301a86cbf09a5a94272c87
fetched_at: '2026-06-29T00:06:28.609190+00:00'
page_id: '233756326'
product: rm
source: tdn-rm
title: TUILPD_DT_Informacoes_Tributacao_Exclusiva_Outros
type: documentation
url: https://tdn.totvs.com/display/LRM/TUILPD_DT_Informacoes_Tributacao_Exclusiva_Outros
version: 116
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao informar eventos na aba Rendimentos de Tributação Exclusiva, Outros Campo 05, Linha 03 os valores são exibidos corretamente no Informe de Rendimentos (Na linha 03, do campo 05), porém ao gerar a DIRF em arquivo os valores referentes aos eventos informados nesse campo são levados (incorretamente) para a parte de Rendimentos Isentos e não tributáveis, campo Outros a Especificar. |
| **Solução/Implementação:** | *Retirado a opção para informar eventos no campo Outros, referente a tributação exclusiva, pois essa informação deve ir em código da receita específico.* |
| **Chamados relacionados:** | *TUILPD, TULKXY* |

divs
