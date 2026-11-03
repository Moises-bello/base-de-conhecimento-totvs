---
content_hash: edfde40704074a9cc7c68c02e3dad96a4093d79a5323f6471ac2eae37e6fec62
fetched_at: '2026-06-29T00:08:55.383754+00:00'
page_id: '348299965'
product: rm
source: tdn-rm
title: 2390965 RMSAU-3105 - DT Problemas com lote de medicamentos na Requisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=348299965
version: 1
---

# Problemas com lote de medicamentos na Requisição

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Movimentação de Estoque |
| **Situação/Requisito:** | Ao confirmar um item na movimentação de estoque cujo lote já esteja preenchido, o sistema está limpando o lote após a confirmação |
| **Solução/Implementação:** | Na confirmação do item sem informar o código de barras o sistema não limpa o lote caso o mesmo esteja informado |
