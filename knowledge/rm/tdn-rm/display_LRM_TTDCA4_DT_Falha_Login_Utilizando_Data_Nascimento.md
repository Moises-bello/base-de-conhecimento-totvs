---
content_hash: 3781eae62e77eb794d7de0890a26bc985531f3009b0b0568a38298ae6d082d14
fetched_at: '2026-06-29T00:06:06.098850+00:00'
page_id: '201728232'
product: rm
source: tdn-rm
title: TTDCA4_DT_Falha_Login_Utilizando_Data_Nascimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDCA4_DT_Falha_Login_Utilizando_Data_Nascimento
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Login no portal do processo seletivo* |
| **Situação/Requisito:** | *Quando o portal do processo seletivo utiliza data de nascimento para login o sistema apresenta erro no logon, mesmo informando uma data correta de um cadastro existente.* |
| **Solução/Implementação:** | *Foi verificado que algumas datas de nascimento possuem a hora no formato assim gerando o erro por causa da diferença, para garantir que sempre o logon ocorrerá sem erro o sistema não irá considerar a hora, somente a data, assim o logon ocorrerá de forma correta.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7* |
