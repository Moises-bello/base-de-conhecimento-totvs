---
content_hash: 574183e03b316c07bda7396817cec867b6fd479f33f0af4df5e88c50149dfe96
fetched_at: '2026-06-29T00:06:11.984088+00:00'
page_id: '204966874'
product: rm
source: tdn-rm
title: TTIPRA_DT_Erro_Ao_Inserir_Nivel_De_Ensino_No_Cadastro_De_Filial_No_Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIPRA_DT_Erro_Ao_Inserir_Nivel_De_Ensino_No_Cadastro_De_Filial_No_Oracle
version: 1
---

# CADASTRO DE NÍVEL DE ENSINO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Cadastro de nível de ensino.* |
| **Situação/Requisito:** | *Erro ao inserir nível de ensino no cadastro de filial. Isto ocorre porque na propagação dos parâmetros para o novo nível de ensino há a*  *utilização de insert com select em campo do tipo LONG, o que não é possível de se fazer no Oracle.* |
| **Solução/Implementação:** | *Ajuste da query de inserção para que o campo do tipo LONG não seja inserido, uma vez que o mesmo não é necessário no momento da*  *propagação dos* *parâmetros. Ajuste adicional para que nesta query não seja usado o TOP (SQL Server) e o ROWNUM (Oracle) e sim o*  *DISTINCT para que não sejam inseridos parâmetros duplicados.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8.* |
