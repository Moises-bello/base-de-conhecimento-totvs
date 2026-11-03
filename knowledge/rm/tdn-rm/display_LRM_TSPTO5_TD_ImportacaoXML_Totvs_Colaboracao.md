---
content_hash: c4cab881f6695f30f6b9aa1e98db5f72334193e2c2366d1912c18a7f677b8f1f
fetched_at: '2026-06-29T00:06:01.101022+00:00'
page_id: '198936315'
product: rm
source: tdn-rm
title: TSPTO5_TD_ImportacaoXML_Totvs_Colaboracao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSPTO5_TD_ImportacaoXML_Totvs_Colaboracao
version: 4
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
| **Versões/Release:** | *11.82.40* |
