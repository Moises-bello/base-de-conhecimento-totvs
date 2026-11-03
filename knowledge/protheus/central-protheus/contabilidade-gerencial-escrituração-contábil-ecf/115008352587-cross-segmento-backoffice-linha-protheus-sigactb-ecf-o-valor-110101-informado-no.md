---
article_id: 115008352587
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 6a4ec6ba1733d432d712e4956df34cf93684cbe0d3832bd07173ed2b1b3cb3d4
fetched_at: '2026-06-28T22:40:47.404632+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - o valor '110101'
  informado no campo conta superior (c1o_ctasup) não existe na base de dados.
type: support-article
updated_at: '2025-07-16T17:26:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008352587-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-o-valor-110101-informado-no-campo-conta-superior-c1o-ctasup-n%C3%A3o-existe-na-base-de-dados
---

**Ocorrência**

Erro apresentado ao importar o ECF para o TAF

O valor '110101' informado no campo Conta Superior (C1O\_CTASUP) não existe na base de dados.

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 11.80

**Solução**

Mensagem:

|T010|20140901|01|1|5|1101010001|CAIXA|||110101|20140901|

|T010AA||01|1.01.01.01.01|2015|

Verificar na tabela CT1 se a conta 110101 (sintética) esta cadastrada no TAF no bloco J050, este não estando, confira no Contábil na tabela CT1 a existência da conta 110101 , a sua data de vigência se esta dentro do período

Com isso veja se a rotina de escrituração importo a conta para  TAF : [J050 e J051 COMO GERAR](http://tdn.totvs.com/pages/releaseview.action?pageId=284465420)

Saiba Mais:

[MP - SIGACTB - ECF - O valor '01' informado no campo Cod Natureza Cta/Grp (C1O\_CODNAT) não existe na base de dados.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008352827-MP-SIGACTB-ECF-O-valor-01-informado-no-campo-Cod-Natureza-Cta-Grp-C1O-CODNAT-n%C3%A3o-existe-na-base-de-dados-)

Veja tratamento das Autocontidas  
[MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)  
Veja as tabelas   
[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)
