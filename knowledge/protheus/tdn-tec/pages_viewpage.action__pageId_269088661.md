---
content_hash: d9a0e374041bd307d77d38e61d40548c0df769b042e4ac30276e11644845bd82
fetched_at: '2026-07-02T19:24:22.309184+00:00'
page_id: '269088661'
product: protheus
source: tdn-tec
title: Correção - Função ComputerName não retorna FQDN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269088661
version: 2
---

A função ComputerName deve retornar em ambientes não Windows o FQDN da máquina.

|  |  |
| --- | --- |
| Situação | Função ComputerName não retorna o FQDN. |
| Ocorrência | Em ambientes não Windows, a função ComputerName não retorna o FQDN, retornando na verdade o hostname junto com o domínio NIS/YP. |
| Correção | A função foi corrigida para que retorne o FQDN ao invés do domínio NIS/YP. |
| Informações adicionais | * Referente ao chamado: TVMDPE-TVRDO5 * Referente à ocorrência: SSIM-1194 * Disponível no Label 7.00.131227A, release SmartClient 2.3.3 |
