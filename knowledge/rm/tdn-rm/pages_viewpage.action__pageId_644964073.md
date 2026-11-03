---
content_hash: d891292c40f6360bac1d4811e6db48d4482bbbf4e4f230c3146271543a764af4
fetched_at: '2026-06-29T00:11:11.036077+00:00'
page_id: '644964073'
product: rm
source: tdn-rm
title: S-1010 - Tabela de Rubricas - Órgão Público
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=644964073
version: 6
---

false

**A partir das Versões:**

* 12.1.31.261
* 12.1.32.206
* 12.1.33.128
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1010 para atender ao leiaute do eSocial, versão S-1.0, para o grupo 4.

---

Em Cadastros | Eventos foram criados os campos abaixo:

1) Quando o parâmetro **"Compõe Teto Remuneratório (art. 37, XI, da CF/1988)"** estiver marcado, ao gerar o XML do evento S-1010 o sistema irá preencher a tag <tetoRemun>.

Essa tag é gerada quando a natureza jurídica do declarante é Administração Pública (grupo [1]).

2) Quando o campo **"Contribuições RPPS/Regime Militar"** for preenchido, ao gerar o XML do evento S-1010, o sistema irá preencher a tag <codIncCPRP>.

**ATENÇÃO:**

Este campo encontra-se disponível no sistema a partir das releases: 12.1.31.248, 12.1.32.188, 12.1.33.115 e superiores.
