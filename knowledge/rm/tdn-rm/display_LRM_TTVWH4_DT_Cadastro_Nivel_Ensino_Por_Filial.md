---
content_hash: 8a8623f1482ca34fbab2376cc408f6553a0d5f14df48cabdb0e70999f6597cb8
fetched_at: '2026-06-29T00:06:21.088292+00:00'
page_id: '223160063'
product: rm
source: tdn-rm
title: TTVWH4_DT_Cadastro_Nivel_Ensino_Por_Filial
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVWH4_DT_Cadastro_Nivel_Ensino_Por_Filial
version: 3
---

# CADASTRO DE NÍVEL DE ENSINO POR FILIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Cadastro de nível de ensino por filial* |
| **Situação/Requisito:** | *Ao tentar vincular um nivel de ensino a uma filial é apresenta erro de chave duplicada. Mesmo não havendo registros já associados.* |
| **Solução/Implementação:** | *Ajuste no método que efetua a propagação de parâmetros entre contextos, o mesmo estava com uma não conformidade, de duplicidade de chaves, que não possibilitava vincular um nível de ensino a uma filial.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.8.109* |
| **Versão Expedida:** | *N/A* |

divs
