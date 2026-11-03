---
article_id: 1500005988801
category: MDFe - Manifesto de Carga
content_hash: be282b09efc0fa94508424aca7a7fcaf669f355949920421043ccbcf27055810
fetched_at: '2026-06-28T22:40:08.107169+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Ao acessar a rotina
  apresenta error - variable does not exist CC0_VEICUL on { |o| POSICIONE
type: support-article
updated_at: '2021-10-21T14:45:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005988801-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Ao-acessar-a-rotina-apresenta-error-variable-does-not-exist-CC0-VEICUL-on-o-POSICIONE
---

**Dúvida**Após clicar em Ok, na tela de filtros apresenta o error:

variable does not exist CC0\_VEICUL on { |o| POSICIONE("DA3",1,CC0->CC0\_FILIAL+CC0\_VEICUL,"DA3\_PLACA") }(APLIB090.PRW)

**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFe - a partir da versão 12.1.25  
Cross Segmentos - TSS - a partir da versão 12  
  
**Solução**Deve ser verificado o nível de acesso no modulo do configurador, nesse cenário deve esta marcado as opções abaixo, para não apresentar o error.

169- gravar filtro do browser com empresa/filial  
190 - grava configuração do browser por empresa/filial
