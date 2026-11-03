---
content_hash: e5a1e40d6c6dd1c29bc2ac686225f4087da2efae95664b124aad277eb93c811d
fetched_at: '2026-06-29T00:06:05.396192+00:00'
page_id: '201721238'
product: rm
source: tdn-rm
title: TSUFP7_DT_Dados_Censo_Escolar_Turma
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUFP7_DT_Dados_Censo_Escolar_Turma
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Função:** | *Dados do Censo Escolar da Turma* |
| **Situação/Requisito:** | *Curso Educação Profissional no BD permite digitar até 5 posições, se o usuário cadastrar no RM.exe a quantidade acima, ocorre o erro: "Valor inválido para o campo "Curso educação profissional""* |
| **Solução/Implementação:** | *O campo Curso Educação Profissional foi alterado para permitir digitar apenas 5 posições. Continuará dando a mensagem "Valor inválido para o campo 'Curso educação profissional'" quando o valor for acima de 32767. Porque esse é o limite para campos do tipo "smallint", e não 99999. Portanto, a limitação de 5 caracteres é apenas para que não seja digitado um valor exorbitante que não será aceito.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | **N/A** |
| **Versões/Release:** | *12.1.6/12.1.7* |
