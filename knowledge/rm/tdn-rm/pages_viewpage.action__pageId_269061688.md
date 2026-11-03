---
content_hash: b27fc7963e7c6c94de48e2d958eaf7275940be30967d679cf13a0af0c824290d
fetched_at: '2026-06-29T00:08:21.615257+00:00'
page_id: '269061688'
product: rm
source: tdn-rm
title: MRH-1909 _DT_Orcamento_Admissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269061688
version: 113
---

# ORÇAMENTO ADMISSÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Orçamento Admissão* |
| **Situação/Requisito:** | ERRO ao executar a fórmula EVT\_1111 para funcionário ADMISSAO01: System.ApplicationException: A fórmula EVT\_1111 não pode ser executada! Referência de objeto não definida para uma instância de um objeto. |
| **Solução/Implementação:** | Módulo do orçamento realiza calculo errado quando possui fórmula vinculada aos eventos. Ajuste no módulo de Orçamento para executar fórmulas afim de calcular valores corretamente. Objeto não possuía uma instancia definida. |
| **Chamados relacionados:** | MRH-1909 |

divs
