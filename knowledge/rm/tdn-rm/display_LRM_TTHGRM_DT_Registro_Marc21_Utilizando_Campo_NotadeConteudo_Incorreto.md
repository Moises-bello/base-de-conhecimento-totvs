---
content_hash: 2e8cf7d9ade5c1c6c56856ee42648f83e0b2393e90546d6b946d83893a4f4e05
fetched_at: '2026-06-29T00:06:09.707477+00:00'
page_id: '203756261'
product: rm
source: tdn-rm
title: TTHGRM_DT_Registro_Marc21_Utilizando_Campo_NotadeConteudo_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHGRM_DT_Registro_Marc21_Utilizando_Campo_NotadeConteudo_Incorreto
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Registro MARC 21* |
| **Situação/Requisito:** | *Quando o campo 'Notas de conteúdo' era inserido na publicação, ao visualizar o registro MARC 21 o sistema estava mostrando a tag 505 referente ao campo 'Notas de conteúdo' porém mostrava também a tag 520 com o mesmo valor.* |
| **Solução/Implementação:** | *Foi identificado que as tags 505 e 520 estavam utilizando o mesmo campo, foi feito a correção para que a tag 505 mostra o campo 'Notas de conteúdo' e a tag 520 mostre o campo 'Resumo'.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
