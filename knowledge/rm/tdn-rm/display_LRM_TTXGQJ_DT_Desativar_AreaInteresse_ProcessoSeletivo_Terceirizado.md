---
content_hash: 93ce8295c1143c9ccf665faa323dc7ea3b9f117af4b1cc2d52d32d2c9cad219d
fetched_at: '2026-06-29T00:06:21.669238+00:00'
page_id: '223175783'
product: rm
source: tdn-rm
title: TTXGQJ_DT_Desativar_AreaInteresse_ProcessoSeletivo_Terceirizado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXGQJ_DT_Desativar_AreaInteresse_ProcessoSeletivo_Terceirizado
version: 1
---

# ÁREA DE INTERESSE OFERTADA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Alterar área de interesse ofertada* |
| **Situação/Requisito:** | *Foi identificado que não é possível desativar uma área de interesse ofertada em um processo seletivo quando este possui instituição configurada e a área de interesse não possui, ou seja, o processo seletivo é terceirizado.* |
| **Solução/Implementação:** | *Quando o campo instituição é preenchido, o processo seletivo se caracteriza como terceirizado. Após indicar que este processo seletivo é terceirizado, as áreas ofertadas deste tipo de processo seletivo serão as Áreas de interesse Cliente, cadastradas em Tabelas auxiliares. As áreas de interesse cliente são áreas a ofertadas nos processos seletivos deste tipo, mas que não fazem parte dos cursos ofertados regularmente pela Instituição de ensino local. Essa situação acontece somente para processos seletivos realizados para terceiros, pois a instituição que está gerenciando o processo seletivo, oferece áreas que não compõem a grade de cursos da mesma. Sendo assim, não foi feita nenhuma alteração nas processos do cadastro da área de interesse, somente foi feito um ajuste para permitir desativar uma área de interesse em um processo seletivo desconsiderando a regra acima, porém para ativar ou criar uma nova área a regra acima continuará sendo aplicada.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
