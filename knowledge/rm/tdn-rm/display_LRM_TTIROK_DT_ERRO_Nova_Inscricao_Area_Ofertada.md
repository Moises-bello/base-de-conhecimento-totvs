---
content_hash: 4cf8fe377d2d75213aaa4fc8ba487558ee3a8ea3cdb4ee7ac30eb7cdd8043cc0
fetched_at: '2026-06-29T00:06:11.112867+00:00'
page_id: '203766808'
product: rm
source: tdn-rm
title: TTIROK_DT_ERRO_Nova_Inscricao_Area_Ofertada
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIROK_DT_ERRO_Nova_Inscricao_Area_Ofertada
version: 3
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
| **Versões/Release:** | *12.1.8* |
