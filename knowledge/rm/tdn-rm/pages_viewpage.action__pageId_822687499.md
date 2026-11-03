---
content_hash: b5a14e3b15bed0a25dc5be84faa74b1deb5b62212b473eb3a455c4e756491f7e
fetched_at: '2026-06-29T00:11:46.469843+00:00'
page_id: '822687499'
product: rm
source: tdn-rm
title: Grupo de informações relativas ao local da prestação do serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822687499
version: 10
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **cServ** | **DPS/serv/** | **Sim** | **Grupo** | **Grupo de informações relativas ao local da prestação do serviço.** |
| cTribNac | DPS/serv/cserv | Sim | Cadastro do Produto, Anexo "Tributo do Produto Por Município", Campo "Código de Serviço Federal", vinculado ao município de incidência  DTRBMUNICIPIOPRD.CODIGOSERVICOFEDERAL | Para o caso de serviço prestado em "Águas Marítimas" o serviço informado nunca poderá ser 20.01 |
| cTribMun | DPS/serv/cserv | Não | Cadastro do Produto, Anexo "Tributo do Produto Por Município", Campo "Código do Serviço no Município", vinculado ao município de incidência  DTRBMUNICIPIOPRD.CODIGOSERVICO |  |
| xDescServ | DPS/serv/cserv | Sim | Cadastro do Produto, Campo "Descrição do Produto"  TPRODUTO.DESCRICAO |  |
| cNBS | DPS/serv/cserv | Não | Cadastro do Produto, Campo "Código NBS do Serviço"  TPRODUTO.NUMERONBS  À partir da versão 12.1.2502 esse campo passou a ter origem no cadastro de Classificação de Bens e Serviços ( DCLASSIFBENSSERVICO.NBS) vinculado ao Produto | NBS - Nomenclatura Brasileira de Serviços, Intangíveis e outras Operações que produzam Variações no Patrimônio |
| cIntContrib | DPS/serv/cserv | Não | Não será gerado |  |
