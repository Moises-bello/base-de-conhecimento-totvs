---
content_hash: c612d974eca57841b5fa3fefc809354cdd5c61df3aa39de31f04c818f8fca531
fetched_at: '2026-07-02T19:24:21.515756+00:00'
page_id: '267810392'
product: protheus
source: tdn-tec
title: Correção - FRename e FRenameEX não funcionam em Unix
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267810392
version: 1
---

As funções FRename e FRenameEX foram corrigidas para funcionarem em ambientes Unix.

|  |  |
| --- | --- |
| Situação | As funções FRename e FRenameEX não renomeiam arquivos em ambientes Unix. |
| Ocorrência | Nos ambientes Unix o arquivo não é renomeado e retorna erro 161. |
| Correção | O mensagem para renomear o arquivo chegava ao SmartClient sem ser sanitizada, contendo caracteres de controle no caminho do arquivo, fazendo com que ele não fosse encontrado pelo sistema. |
| Informações adicionais | * Referente ao chamado: TWGDA0 * Referente à ocorrência: SSIM-1257 * Disponível em builds superiores a 7.00.131227A 2.2.1 |
