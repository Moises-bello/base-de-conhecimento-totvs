---
content_hash: 19126c66dad661bd150168263a4fc2e6507bf823bacc690eb3e5ce619dc6361c
fetched_at: '2026-06-29T00:06:06.093401+00:00'
page_id: '201728222'
product: rm
source: tdn-rm
title: TSYUKZ_DT_Falha_Login_Utilizando_Data_Nascimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYUKZ_DT_Falha_Login_Utilizando_Data_Nascimento
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
| **Versões/Release:** | *11.82.41* |
