---
content_hash: d30e2f0ff78f29ef00aa0ed04875e23678b8e8e3a497eac127348acdfbf50352
fetched_at: '2026-06-29T00:06:27.443043+00:00'
page_id: '232822029'
product: rm
source: tdn-rm
title: TUGFWQ_DT_Classificacao_Nao_Desclassifica_Nota_Zerada
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGFWQ_DT_Classificacao_Nao_Desclassifica_Nota_Zerada
version: 121
---

# CLASSIFICAÇÃO DE CANDIDATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Classificação de candidatos* |
| **Situação/Requisito:** | *Alguns candidatos em processos seletivos que tiraram 0 em alguma prova, não foram desclassificados e continuaram para as chamadas,  mesmo com a opção de desclassificar por nota zerada marcada.* |
| **Solução/Implementação:** | *Foi identificado que esta situação ocorre quando a área ofertada do processo seletivo possui fórmula para cálculo de resultado, assim o sistema não validava corretamente o valor zerado da prova nem a regra de desclassificar por nota zerada. Foi feito o ajuste para que se a nota estiver zerada o status da opção do candidato seja definido como desclassificado e não seja invalidado pela fórmula de cálculo de resultado. Assim, o sistema define corretamente os desclassificados por nota e no momento da chamada de aprovados, o sistema irá considerar somente candidatos classificados.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | **12.1.9**  *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
