---
content_hash: b6c37757bf9a9c8cb94233941030f4968d1033767697c3100cb824fefce3473d
fetched_at: '2026-06-29T00:06:11.108778+00:00'
page_id: '203766770'
product: rm
source: tdn-rm
title: TTBJS0_DT_ERRO_Nova_Inscricao_Area_Ofertada
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBJS0_DT_ERRO_Nova_Inscricao_Area_Ofertada
version: 2
---

# INSCRIÇÃO ÁREA OFERTADA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Inscrição Área Ofertada* |
| **Situação/Requisito:** | *No momento da seleção de um grupo de áreas ofertadas no portal de inscrições, o portal realiza uma query que está indevida no SPSAREAINTERESSE.GRUPO LIKE 'Alem%'.*  *Não é viável ter um LIKE no grupo, precisaria ser = (igual), pois desta forma como está, as áreas aparecem todas duplicadas.* |
| **Solução/Implementação:** | *Ao retornar a url para invocar o método ajax, utilizado o método encodeURI() do javascript para tratar os caracteres com acentos.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.82.41* |
