---
content_hash: 4d2eb7cc5dbf19189db957d688efdfb2d2f1aa0107e08088111cbdb4924bbea1
fetched_at: '2026-06-29T00:09:02.921577+00:00'
page_id: '381028835'
product: rm
source: tdn-rm
title: 3216192 EDUCACIONAL01-5676 DT Censo da Educação Básica 2018
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381028835
version: 1
---

# CENSO DA EDUCAÇÃO BÁSICA 2018

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Censo da Educação Básica |
| **Situação/Requisito:** | Ao realizar o Arquivamento e recuperação de dados do EducaCenso gera o o erro "Verificar o SQL responsável por gerar os registros "30" do EducaCenso definido nos parâmetros do Educacional" |
| **Solução/Implementação:** | Todas as consultas foram alteradas para não fazer comparação com vazio (''), pois isso pode gerar problema em bases Oracle. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
