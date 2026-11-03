---
content_hash: c7c4212e2810f23a017ed8e3f9b349a40e8c0c521829e4483e26416d26dd41e9
fetched_at: '2026-06-29T00:09:09.899932+00:00'
page_id: '394214662'
product: rm
source: tdn-rm
title: 3423778 DSAUGHFATF-1513 DT Data de vigência na importação de Tabelas de MATMED
  de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394214662
version: 3
---

# Data de vigência na importação de Tabelas de MATMED de Convênios

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Utilitários / Importação de Tabelas de MATMED de Convênios |
| **Situação/Requisito:** | Ao realizar a inclusão de um item na tabela de preços, o sistema incluía a vigência com a data atual, desconsiderando a vigência selecionada para aquela tabela. |
| **Solução/Implementação:** | Incluído opção para definir a vigência dos novos itens a partir da vigência selecionada ou da data atual.    1. Ao gravar a inclusão do item com a opção de vigência **Selecionada**, o item terá sua vigência a partir da **Data de Vigência** selecionada da tabela de MATMED. 2. Gravar a inclusão com a opção de **Data atual** irá definir a vigência do item a partir da data atual (comportamento padrão). |
| **Documento de Referência:** | <https://totvssuporte.zendesk.com/agent/tickets/3423778> |
