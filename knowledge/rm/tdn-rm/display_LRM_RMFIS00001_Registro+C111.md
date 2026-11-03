---
content_hash: dd26176eec3fa19632421ca78054e43d95f12af656e64811722810448e81490c
fetched_at: '2026-06-29T00:08:44.004526+00:00'
page_id: '307837567'
product: rm
source: tdn-rm
title: RMFIS00001_Registro C111
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_Registro+C111
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.7 |
| **Ocorrência:** | Parametrização do Registro C111 - EFD Contribuições. |
| **Ambiente:** |  |
| **Passo a passo:** | Registro específico para a pessoa jurídica informar a existência de processo administrativo ou judicial que autoriza a adoção de tratamento tributário (CST), base de cálculo ou alíquota diversa da prevista na legislação. Trata-se de informação essencial a ser prestada na escrituração para a adequada validação das contribuições sociais ou dos créditos, pelo Programa Validador e Assinador da EFD-Contribuições.       * Para cadastro do Processo Judicial ou Administrativo, acesse o menu: Cadastros/ Mais - Processo Judicial e Administrativo;            * No lançamento fiscal / em Situações Tributárias/ aba de Processos Judiciais. Deve ser vinculado o processo judicial ou administrativo;         Segue abaixo resultado do exemplo:  |C001|0| |C010|21867387000158|2| |C100|1|0|GC00013|55|00|1|000004545||19102017|19102017|5000,00|2|0,00||5000,00||0,00|0,00|0,00|5000,00|600,00|0,00|0,00|0,00|32,50|380,00||| |C111|123456789|3| |C170|1|01.01||1,00000|UN|5000,00|0,00|0|100|5101|510101|5000,00|12,00|600,00|0,00|0,00|0,00||||0,00|0,00|0,00|01|5000,00|0,6500|||32,50|01|5000,00|7,6000|||380,00|| |C990|6| |D001|1| |D990|2| |F001|1| |F990|2| |M001|1| |M990|2| |1001|0| |1010|123456789|Teste|0|01|Teste Grazielhe C111|01012017| |1100|032017|01||101|100,00|0,00|100,00|50,00|0,00|0,00|50,00|0,00|0,00|0,00|0,00|0,00|50,00| |1990|4|      **Observação:**    Uma vez procedida à escrituração do Registro “C111”, deve a pessoa jurídica gerar os registros “1010” ou “1020” referentes ao detalhamento do processo judicial ou do processo administrativo, conforme o caso, que autoriza a adoção de procedimento especifico de apuração das contribuições sociais ou dos créditos. |
| **Observações:** |  |
