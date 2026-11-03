---
content_hash: ef6bda66f28900a4177feab171a9d4d921baaf88b7fe1b10b8e4c4139af07f19
fetched_at: '2026-06-29T00:08:58.763429+00:00'
page_id: '361438175'
product: rm
source: tdn-rm
title: 2402354 EDUCACIONAL01-4409 DT Matrícula no Processo Seletivo RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361438175
version: 2
---

# MATRÍCULA NO PROCESSO SELETIVO RM

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Processo Seletivo RM |
| **Situação/Requisito:** | Não é possível matricular um candidato aprovado no Processo Seletivo, via integração do TOTVS Educacional X Processo Seletivo, o Responsável Financeiro é dado como Chave Duplicada na Tabela PPESSOA, porém se a matrícula for realizada sem a importação do dados do Responsável Financeiro informado no Processo Seletivo, é possível realizar a Matrícula do Candidato. |
| **Solução/Implementação:** | No TOTVS Educacional foi identificado uma falha ao matricular um candidato do processo seletivo RM que possua responsável financeiro. Foi identificado que a situação ocorria devido a uma inconsistência na GAUTOINC utilizada pelo educacional para gerar o CODCFO (Cli/For), como a GAUTOINC estava desabilitada o sistema gerar um CODCFO que já exista. Foi feito o ajuste para que o sistema se identificar que se o CODCFO existir, o sistema continuará executando o autoinc até encontrar um disponível, tal ação garante que não ocorrerá conflitos e também manterá a GAUTOINC sempre atualizada compatível com os códigos do Cli/For que no cadastro financeiro são gerados manualmente sem consulta com a GAUTOINC. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
