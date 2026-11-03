---
content_hash: 0361c7caca0413a3cb310c7d16ca6e1cd7d6141e73e62d21d5438623b7cb81ba
fetched_at: '2026-06-29T00:12:10.801010+00:00'
page_id: '953003709'
product: rm
source: tdn-rm
title: Grupo YB - Informações do Intermediador da Transação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003709
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo YB - Informações do Intermediador da Transação** | | | | | | | | | |  |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | **Mais Informações** |
| 392.26 | YB01 | infIntermed | Grupo de Informações do Intermediador da Transação | G | A01 |  | 0-1 |  | Obrigatório o preenchimento do Grupo de Informações do Intermediador da Transação nos casos de “operação não presencial pela internet em site de terceiros (intermediadores)" | NÃO SERÁ GERADO |
| 392.27 | YB02 | CNPJ | CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios. | E | YB01 | N | 1-1 | 14 | Informar o CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios. | NÃO SERÁ GERADO |
| 392.28 | YB03 | idCadIntTran | Identificador cadastrado no intermediador | E | YB01 | C | 1-1 | 2-60 | Nome do usuário ou identificação do perfil do vendedor no site do intermediador (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios. | NÃO SERÁ GERADO |
