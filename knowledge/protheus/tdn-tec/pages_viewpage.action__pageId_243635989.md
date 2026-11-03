---
content_hash: 7896cd77b33f0c84ad7855e1aa11190f031ade94df37b15887791c813ac750cc
fetched_at: '2026-07-02T19:24:19.645097+00:00'
page_id: '243635989'
product: protheus
source: tdn-tec
title: Correção na validação e aplicação de patch para fontes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243635989
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Quando o nome de um fonte tinha 2 caracteres o patch não era aplicado. |
| Ocorrência | Para reproduzir:   * Criar um fonte, por exemplo AB.PRW * Compilá-lo e gerar o pacote deste fonte. * Ao aplicá-lo o fonte será retirado do repositório. * Alterar o nome do fonte para ABC.PRW * Compilá-lo e gerar o pacote deste fonte. * Ao aplicá-lo o fonte ainda estará no repositório. |
| Correção | Validação correta do nome dos fontes e aplicação do patch. |
| Informações adicionais | * Disponível em builds superiores a * Revisão: 8673 * SSIM-1128 |
