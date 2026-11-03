---
content_hash: dbf87a6552158646c8525bd1adbce1b163e466fbe27c1c4cbe8abfa637f5517f
fetched_at: '2026-06-29T00:08:52.718135+00:00'
page_id: '342302339'
product: rm
source: tdn-rm
title: 2201346 FINANCEIRO01-5205 DT Gerar contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342302339
version: 2
---

# Gerar contabilização

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Gerar contabilização |
| **Situação/Requisito:** | Ao utilizar a função **TABLAN('IDLANMOVORIGEM','I')** no evento contábil, sistema informa que o campo **IDLANMOVORIGEM** não pertence a tabela **FLAN**. Segue abaixo mensagem exibida ao contabilizar inclusão de lançamento com evento contábil que valida este campo: "O Evento Contábil 1-160 possui uma fórmula (**IDLANMOV**) que não pode ser executada. Verifique o item de Evento e as fórmulas correspondentes.". |
| **Solução/Implementação:** | O campo IDLANMOVORIGEM não é mais utilizado na integração do Financeiro com o Nucleus. O campo passou a ser suportado na execução do evento contábil apenas para garantir a compatibilidade de recontabilização de lançamentos gerados em data anterior à publicação da "Nova Baixa". |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FINTRF000018 |
| **Documento de Referência:** | N/A |
