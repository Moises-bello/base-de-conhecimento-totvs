---
content_hash: 8f7917f8b15c8791ed7f6b2e6946ad49b0f7936bb2bc4fd3ce9815bf7dfdb46d
fetched_at: '2026-06-29T00:09:51.638463+00:00'
page_id: '437256522'
product: rm
source: tdn-rm
title: '3931463 FISCAL01-6941 DT - NFS-e - Volta Redonda - Nenhuma NFS-e foi consultada.
  Erro: Há vários elementos raiz.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=437256522
version: 2
---

# Nenhuma NFS-e foi consultada. Erro: Há vários elementos raiz.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Consulta de NFS-e |
| **Situação/Requisito:** | Ao consultar a autorização da NFS-e do município de Volta Redonda é apresentado a mensagem:  "Nenhuma NFS-e foi consultada. Erro: Há vários elementos raiz. Linha 4 , posição 10206".  A causa deste problema é devido o TSS retornar no método retornanfse\_out o conteúdo do XMLPROT maiúsculo tornando o XML inválido. |
| **Solução/Implementação:** | Tratativa da mensagem para quando o ERP não conseguir buscar o XML devido a inconsistências do TSS, seja apresentado a mensagem "Não foi possivel obter o XML de Retorno da NFS-e". |
