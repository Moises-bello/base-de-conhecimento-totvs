---
content_hash: 709c6e824c72d2c217399669d17f55266c48298df469db26f3c6eb3cef2372b9
fetched_at: '2026-06-29T00:09:53.021326+00:00'
page_id: '439711252'
product: rm
source: tdn-rm
title: DT Opção de Ativo/Inativo para Tipo de Documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439711252
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Tipo de Documento |
| **Situação/Requisito:** | Eu, como Analista Financeiro, necessito de uma opção no cadastro de Tipo de Documento que indique se o registro está inativo.  CRITÉRIOS DE ACEITE:   * Usar campo INATIVO já criado na tabela FTDO. * Campos disponível na visão de Tipos de Documento. * Default para o campo é desmarcado (0 - não inativo). * Registros inativos não podem ser selecionados em todos os pontos do sistema e outros módulos (lookup), mas na tela da entidade já vinculada a um tipo de documento o mesmo deve ser exibido. * Para as entidades do Financeiro vinculadas a um tipo de documento o serviço de inclusão deve consistir se registro está inativo. * Para alteração de lançamento se o tipo de documento foi alterado validar no serviço se o mesmo está ativo. * Na inclusão de default de cli/for (serviço) validar se ativo. |
| **Solução/Implementação:** | No cadastro de Tipo de Documento foi criado o campo "Inativo".,    Na pesquisa dos lookups de tipo de documento não serão exibidos os tipos de documentos inativos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4417> |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
