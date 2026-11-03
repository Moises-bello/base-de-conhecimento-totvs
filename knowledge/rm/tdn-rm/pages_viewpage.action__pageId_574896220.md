---
content_hash: cbb2a9c9be3eaa30ac9257c534d541bb503b932aac98991860d919a271a692e8
fetched_at: '2026-06-29T00:10:53.084345+00:00'
page_id: '574896220'
product: rm
source: tdn-rm
title: Totvs Incorporação - Parâmetros - DAI(Declaração de Atividades Imobiliarias)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574896220
version: 3
---

Parametrização utilizada para informar onde a DAI irá obter as áreas(Venda e Aluguel) e as características dos imóveis.

### Configuração DAI Venda

##### Campos de Área da DAI (Somente dados das tabelas **XSUBUNIDADE e XSUBUNIDADECOMPL**):

* **AREA\_UTIL\_CONSTRUIDA**: Informar o campo onde está armazenado a área útil construída. Sugestão: **XSUBUNIDADE.AREA**
* **AREA\_TOTAL\_CONSTRUIDA:**Informar o campo onde está armazenado a área total construída. Sugestão: **XSUBUNIDADE.AREA\_TOTAL**
* **AREA\_TERRENO:**Informar o campo onde está armazenado a área do terreno. Sugestão: **XSUBUNIDADE.AREA\_TOTAL**

##### Campos de Quantidade da DAI:

* **QTD\_DORMITORIOS:** Informar o cadastro do tipo de característica que representa o numero de dormitórios.
* **QTD\_BANHEIROS:**  Informar o cadastro do tipo de  característica que representa o numero de banheiros.

### Configuração DAI Aluguel

##### Campos de Área da DAI:

* **AREA\_UTIL\_CONSTRUIDA**: Informar o campo onde está armazenado a área útil construída. Sugestão: **XALGIMOVEL.AREATOTAL**
* **AREA\_TOTAL\_CONSTRUIDA:**Informar o campo onde está armazenado a área total construída. Sugestão: **XALGIMOVEL.AREATOTAL**
* **AREA\_TERRENO:**Informar o campo onde está armazenado a área do terreno. Sugestão: **XALGIMOVEL.AREATOTAL**

##### Campos de Quantidade da DAI:

* **QTD\_DORMITORIOS:** Informar o cadastro do tipo de característica que representa o numero de dormitórios.
* **QTD\_BANHEIROS:**  Informar o cadastro do tipo de  característica que representa o numero de banheiros.
* ****QTD\_VAGAS\_GARAGEM**:** Informar o cadastro do tipo de  característica que representa o numero de vagas de garagem.
