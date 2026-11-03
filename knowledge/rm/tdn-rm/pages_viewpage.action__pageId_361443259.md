---
content_hash: 91a12183f2943cbf2bd5c6080ff6a6d02a327fac9144113747e1ac75982f5207
fetched_at: '2026-06-29T00:08:58.821515+00:00'
page_id: '361443259'
product: rm
source: tdn-rm
title: 2743902 RMSAU-3745 DT Procedimento pela Guia/Autorização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361443259
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Lançamento pela Guia/Autorização |
| **Situação/Requisito:** | Ao solicitar uma guia com procedimento que não utiliza tabela CBHPM, o sistema está emitindo a seguinte mensagem: "Porte CBHPM do item xxxxxx está incorreto. Informe o valor correto na Tabela de Procedimentos e Serviços" |
| **Solução/Implementação:** | Antes de exibir a mensagem, é necessário verificar as tabelas de preço diferenciadas, pois a situação que ocorria era que a tabela da condição contratual era CBHPM e a da tabela de preço diferenciada não era CBHPM. |
