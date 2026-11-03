---
content_hash: 9afae1c1a4314e03ff527ba58f2c15b9e2936704f91334b0195146068712efc3
fetched_at: '2026-06-29T00:10:14.618368+00:00'
page_id: '461914439'
product: rm
source: tdn-rm
title: 5099086 FISCAL01-8123 DT Lançamento Fiscal - Período de Apuração do(s) Tributo(s)
  ISS não está aberto para movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461914439
version: 1
---

# Lançamento Fiscal - Período de Apuração do(s) Tributo(s) ISS não está aberto para movimentação

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Lançamento Fiscal |
| **Situação/Requisito:** | Ao tentar editar ou incluir um lançamento fiscal colocando o tributo ISS é retornada a mensagem de erro: "Período de Apuração do(s) Tributo(s) ISS não está aberto para movimentação.", quando o período de apuração do tributo está aberto. A data de apuração do ISS é a data de emissão. |
| **Solução/Implementação:** | Foi modificado a validação do período de apuração do tributo ISS no Lançamento Fiscal ou no Item do Lançamento para verificar o período conforme a parametrização de datas do ISS. Anteriormente era verificado fixo a data do lançamento mesmo nos casos em que o ISS era apurado pela data de emissão. |
