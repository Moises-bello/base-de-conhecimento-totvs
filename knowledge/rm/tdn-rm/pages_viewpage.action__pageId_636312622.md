---
content_hash: 1d169080526850f1e1769dfc11b8c96db98049d6eca7b7503cd4590c84f86611
fetched_at: '2026-06-29T00:11:06.899875+00:00'
page_id: '636312622'
product: rm
source: tdn-rm
title: FISCAL01-16489 - Agrupamento do R-2055 "Funrural" por código de Cliente quando
  deveria ser por CPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=636312622
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16489 |

## **02. SITUAÇÃO/REQUISITO**

Ao consultar os eventos R-2055 é apresentada a inconsistência abaixo:

<regOcorrs><tpOcorr>1</<wbr>tpOcorr><localErroAviso><wbr>Registro: evtAqProd - XPATH: /Reinf/evtAqProd</<wbr>localErroAviso><codResp><wbr>MS1459</codResp><dscResp>Não é permitido o envio de mais de um evento para o contribuinte, num mesmo período de apuração, mesmo estabelecimento adquirente e produtor rural, exceto se for para retificação de um evento enviado anteriormente ou se o evento anterior tenha sido excluído.</dscResp></<wbr>regOcorrs>

Isso pois o cliente possui mais de um cadastro de Cliente/Fornecedor para um mesmo Produtor Rural, que possui o mesmo CPF, porque o Cli/For têm várias Fazendas em Minas Gerais e cada Fazenda possui Inscrições Estaduais distintas.

## **03. SOLUÇÃO.**

Foi realizado ajuste no agrupamento para geração da R-2055, levando em consideração apenas o CGC do  
participante (participante podendo ser tanto Cliente Destino como Cli/For).
