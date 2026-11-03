---
content_hash: fb6318bc305850e5df8339f9defc407c6190fd3f4622ca14a0f295cd80cbcb11
fetched_at: '2026-06-29T00:08:14.013222+00:00'
page_id: '244436910'
product: rm
source: tdn-rm
title: TVDE75_DT_Importador_SALUNO
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDE75_DT_Importador_SALUNO
version: 115
---

# IMPORTADOR - SALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Importador - SALUNO* |
| **Situação/Requisito:** | *O importador não está validando se os campos CODCOLCFO e CODCFO estão preenchidos, porque ao não informar um dos campos e importar um aluno, no cadastro do mesmo ocorre erro ao salvar.* |
| **Solução/Implementação:** | *Ajuste no layout de importação da tabela SALUNO informando que é obrigatório o preenchimento dos campos CODCOLCFO e CODCFO quando se deseja informar um responsável financeiro para o aluno. Além disso, foi alterado no importador para ocorrer esta validação.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
