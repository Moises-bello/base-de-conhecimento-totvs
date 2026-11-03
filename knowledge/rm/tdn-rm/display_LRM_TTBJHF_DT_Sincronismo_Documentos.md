---
content_hash: 2556254bc2514f6a3304459072bf4b2ed2e9a71ab29df63eaa39379142198af8
fetched_at: '2026-06-29T00:06:04.791943+00:00'
page_id: '200911358'
product: rm
source: tdn-rm
title: TTBJHF_DT_Sincronismo_Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBJHF_DT_Sincronismo_Documentos
version: 1
---

# Sincronismo de Documentos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Sincronismo de Documentos* |
| **Situação/Requisito:** | O Processo "Sincronismo de Documentos" não retorna as notas disponíveis na sefaz. |
| **Solução/Implementação:** | Melhorias no processo responsável pelo sincronismo de documentos do MD-e, no arquivo de retorno da SEFAZ, o campo INDCONT está com o valor 1 e, quando isto ocorre o ERP deve  solicitar um novo sincronismo até que o mesmo retorne 0, isto significa que para o lote corrente de NSU não existem documentos, no entanto existem outros lotes à serem  consultados. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.7* |
|  |  |
