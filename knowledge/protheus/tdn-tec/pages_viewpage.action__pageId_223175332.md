---
content_hash: 9283b3003c9aadd654bdd03cfb32c476d65a1275b921a39acd8f7f07141e65fb
fetched_at: '2026-07-02T19:24:19.580890+00:00'
page_id: '223175332'
product: protheus
source: tdn-tec
title: Correção - TWsdlManager não suporte import de vários arquivos para o mesmo
  namespace
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223175332
version: 1
---

Essa build contém uma correção na classe AdvPL TWsdlManager.

|  |  |
| --- | --- |
| Situação | Classe TWsdlManager dá erro no parse de um WSDL com import de vários arquivos para o mesmo namespace. |
| Ocorrência | A classe TWsdlManager não consegue fazer o parse de um WSDL que contém imports de mais de um arquivo para o mesmo namespace, retornando erro e não permitindo montar a mensagem. |
| Correção | Foi adicionado à classe o suporte a import de múltiplos arquivos para o mesmo namespace. |
| Informações adicionais | * Referente ao chamado: SSIM-248 * Referente à ocorrência: TRP238 * Disponível em builds superiores a 7.00.131227A com data superior a 05/01/2016. |
