---
content_hash: 380518f9cfd4c35098d1f6599b1c9b832ab03a5a9285113b56f331e6034a8326
fetched_at: '2026-06-29T00:06:10.567732+00:00'
page_id: '203764538'
product: rm
source: tdn-rm
title: TTDMB2_WebService_RhuAusenciaData
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDMB2_WebService_RhuAusenciaData
version: 1
---

# WEB SERVICE RHUAUSENCIADATA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | WebService RhuAusenciaData |
| **Situação/Requisito:** | Ao tentar realizar a leitura do dataserver, RhuAusenciaData, utilizando o wsDataServer pelo aplicativo SoapUI, ele está nos retornando a mensagem: Ocorreu a seguinte mensagem ao efetuar a leitura da visão: Index was outside the bounds of the array. |
| **Solução/Implementação:** | Alterado a forma de recuperar os dados do DataServer e foi adicionada validação que verifica se há dados a ser recuperado. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTDMB2 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.8 |
