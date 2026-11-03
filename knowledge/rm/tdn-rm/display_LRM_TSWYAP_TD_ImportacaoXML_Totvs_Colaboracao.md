---
content_hash: 03b8985271319f526d8927a2b82bbcf5edcf74a0e63134fb5cbb0aa0a4c2c6f2
fetched_at: '2026-06-29T00:06:01.793602+00:00'
page_id: '198940374'
product: rm
source: tdn-rm
title: TSWYAP_TD_ImportacaoXML_Totvs_Colaboracao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWYAP_TD_ImportacaoXML_Totvs_Colaboracao
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Importação de XML Totvs Colaboração* |
| **Situação/Requisito:** | *Ao importar o XML a data estava sendo apresentada com uma diferença de horas, devido ao fuso horário contido no campo da data de emissão, logo a conversão da data apresentava uma diferença entre a data que o cliente realizou a exportação do arquivo com a data do sistema.* |
| **Solução/Implementação:** | *Ajuste na importação que considera a data que o XML do cliente foi emitido, desconsiderando o fuso horário colocado no campo referente a data de emissão.* |
| **Conversores e Parâmetros:** | *Não se aplica* |
| **Chamados relacionados:** | *Não se aplica* |
| **Requisito (ISSUE):** | *Não se aplica* |
| **Versões/Release:** | *12.1.7* |
