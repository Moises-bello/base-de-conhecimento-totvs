---
content_hash: d59ad15188e782db882d0dc0521c39d09810a44019f9b2278056c5d5c106b92e
fetched_at: '2026-06-29T00:06:04.784111+00:00'
page_id: '200911277'
product: rm
source: tdn-rm
title: TSVWI9_DT_Sincronismo_Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVWI9_DT_Sincronismo_Documentos
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
| **Versões/Release:** | *11.82.41* |
|  |  |
