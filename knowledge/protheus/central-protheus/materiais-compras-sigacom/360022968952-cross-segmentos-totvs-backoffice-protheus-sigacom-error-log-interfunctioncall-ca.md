---
article_id: 360022968952
category: Materiais - Compras (SIGACOM)
content_hash: 05e6894dff83cd706c06b7bef8e0b802d38fcd2f41fd89f7393c3f04b5cd3239
fetched_at: '2026-06-28T22:41:17.634105+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Error Log InterFunctionCall:
  cannot find function A140DESPGA in AppMap on EVALVALID line : 1125 '
type: support-article
updated_at: '2022-05-16T21:43:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022968952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Error-Log-InterFunctionCall-cannot-find-function-A140DESPGA-in-AppMap-on-EVALVALID-line-1125
---

**Ocorrência**No módulo de Compras, ao tentar realizar a importação de uma nota via **Totvs colaboração** ou utilizar **rotina automática (Execauto)** da **MATA103** o sistema apresenta **error.log**:

**InterFunctionCall: cannot find function A140DESPGA in AppMap on EVALVALID line : 1125**

**Ambiente**

Protheus - Compras - A partir da versão 12.1.17

**Causa**Esse incidente ocorre, pois a configuração do dicionário para o campo D1\_VALFRE está incorreta.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos,

considerando fazer o procedimento com alguém do departamento TI ou analista especialista em loco: 

Verificar o X3\_VALID do campo D1\_VALFRE, afim de ajustar o conteúdo para MaFisRef("IT\_FRETE","MT100",M->D1\_VALFRE)

***OBSERVAÇÃO :***

Mais dúvidas e/ou informações sobre Rotina Automática, solicitar à equipe de Suporte do ADVPL.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
