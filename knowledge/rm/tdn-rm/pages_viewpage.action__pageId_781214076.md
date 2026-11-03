---
content_hash: 15643aa9d7c0730248c371bef7d06f7a6e6dd69d1960723202fe8db278382fb8
fetched_at: '2026-06-29T00:11:38.119006+00:00'
page_id: '781214076'
product: rm
source: tdn-rm
title: API - SEGURANÇA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781214076
version: 3
---

Segurança

### Apis de Seguranças

API: GET: [http://localhost:8051/api/imb/v1/securitys/813000033/companys/20/persons/111.222.333-50](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)

API que retorna as permissões de uma tag de segurança por coligada e por CPF.

[API: GET:http://localhost:8051/api/imb/v1/securitys/813000033/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)[companys/20/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[persons/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)[111.222.333-50](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[/tables/xcomissoes](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)

API que retorna as permissões de uma tag de segurança por coligada, CPF e por restrições de campos de uma tabela

API: GET: [http://localhost:8051/api/imb/v1/securitys/813000033/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[tags/0\_1\_3\_2/](http://localhost:8051/api/imb/v1/securitys/813000346/tags/0_1_3_2/companys/20/persons/044.266.846-50/tables/xcomissoes)[companys/20/persons/111.222.333-50](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)

API que retorna as permissões de uma tag de segurança e subtags (ExecuteId, InsertId, DeleteId, EditId), por coligada e por CPF

[API: GET:http://localhost:8051/api/imb/v1/securitys/813000033/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)[tags/0\_1\_3\_2/](http://localhost:8051/api/imb/v1/securitys/813000346/tags/0_1_3_2/companys/20/persons/044.266.846-50/tables/xcomissoes)[companys/20/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[persons/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)[111.222.333-50](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[/tables/xcomissoes](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)

API que retorna as permissões de uma tag de segurança e subtags (ExecuteId, InsertId, DeleteId, EditId), por coligada, CPF e por restrições de campos de uma tabela

API: GET: [http://localhost:8051/api/imb/v1/securitys/813000033/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[tags/4/](http://localhost:8051/api/imb/v1/securitys/813000346/tags/0_1_3_2/companys/20/persons/044.266.846-50/tables/xcomissoes)[companys/20/persons/111.222.333-50](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)

API que retorna as permissões de uma tag de segurança e subtag (TagId), por coligada e por CPF

[API: GET:http://localhost:8051/api/imb/v1/securitys/813000033/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)[tags/4/](http://localhost:8051/api/imb/v1/securitys/813000346/tags/0_1_3_2/companys/20/persons/044.266.846-50/tables/xcomissoes)[companys/20/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[persons/](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)[111.222.333-50](http://localhost:8051/api/imb/v1/securitys/813000033/persons/04426684650)[/tables/xcomissoes](http://localhost:8051/api/imb/v1/securitys/813000033/persons/044.266.846-50/tables/xcomissoes)

API que retorna as permissões de uma tag de segurança e subtags (TagId), por coligada, CPF e por restrições de campos de uma tabela

Modelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

Dados recebidos:

* codColigada: Código da coligada do usuário;
* codUsuario: Código do usuário;
* securityId:  Tag de segurança;
* executeId: Tag de visualizar utilizada na verificação;
* insertID: Tag de inserir utilizada na verificação;
* deleteID: Tag de deletar utilizada na verificação;
* editID: Tag de edição utilizada na verificação;
* tagId: Qualquer tipo de tag que queira verificar;
* allowEdit: Permite editar;
* allowInsert: Permite inserir;
* allowView: Permite visualizar;
* allowDelete: Permite deletar;
* allowTagId: Permite executar um tag que foi passada;
* imbTableFieldRestrictionsSecurity: permissões dos campos da tabela definido no parâmetro
