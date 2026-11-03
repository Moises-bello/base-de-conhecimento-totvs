---
content_hash: 42de227d5cb335016d2adb4e687e93c303d974c9c93818cad38c3329850e816f
fetched_at: '2026-06-29T00:08:15.589181+00:00'
page_id: '244912047'
product: rm
source: tdn-rm
title: TVMSAP_DT_Inscricao_Candidato_Portal_Faixa_Etaria_Area
type: documentation
url: https://tdn.totvs.com/display/LRM/TVMSAP_DT_Inscricao_Candidato_Portal_Faixa_Etaria_Area
version: 114
---

# INSCRIÇÃO DO CANDIDATO - PORTAL - FAIXA ETÁRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Inscrição do candidato - portal* |
| **Situação/Requisito:** | *Ao tentar realizar a inscrição do candidato pelo portal em uma área de interesse que possui controle de faixa etária, o sistema não está validando corretamente a faixa etária, alertando para o candidato que a faixa etária está inválida mesmo ele estando na faixa etária permitida da área de interesse.* |
| **Solução/Implementação:** | **Foi identificado que a função javascript que faz a validação de faixa etária não estava realizando a operação de comparação corretamente, foi feito o ajuste e a validação da faixa etária passou a ser executada corretamente.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
