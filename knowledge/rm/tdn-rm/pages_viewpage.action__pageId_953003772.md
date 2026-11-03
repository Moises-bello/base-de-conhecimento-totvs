---
content_hash: 90c9c058491b9dfc1bfbfbe21380f15a68c6753747169b2b269fc4b2552b6511
fetched_at: '2026-06-29T00:12:10.855032+00:00'
page_id: '953003772'
product: rm
source: tdn-rm
title: Grupo ZX - Informações Suplementares da Nota Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003772
version: 10
---

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo ZX - Informações Suplementares da Nota Fiscal**  Criação de novo campo com o objetivo de padronizar a URL de consulta por chave de acesso que aparece no DANFE NFC-e | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Observação** |
| 424 | ZX01 | infNFeSupl | Informações suplementares da Nota Fisca | G | Raiz | - | 0-1 | Informações suplementares da Nota Fiscal, não afetando a assinatura digital. (NT 2015.002) |
| 425 | ZX02 | qrCode | Texto com o QR-Code impresso no DANFE NFC-e. Obs.: URLs, por UF, utilizadas para consulta QR Code acesse: <http://nfce.encat.org/desenvolvedor/qrcode/> | E | ZX01 | C | 1-1 | Consulte a documentação  [Geração do QR-Code](https://tdn.totvs.com/pages/viewpage.action?pageId=975768911) |
| 426 | ZX03 | urlChave | Texto com a URL de consulta por chave de acesso a ser impressa no DANFE NFC-e. Obs.: URLs, por UF, utilizadas para consulta por chave de acesso acesse: <http://nfce.encat.org/consumidor/consultenota/> | E | ZX01 | C | 0-1 | Informar a URL da “Consulta por chave de acesso da NFC-e”. A mesma URL que deve estar informada no DANFE NFC-e para consulta por chave de acesso. |
