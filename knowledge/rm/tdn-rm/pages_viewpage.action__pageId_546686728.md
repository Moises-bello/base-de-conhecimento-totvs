---
content_hash: 035d62aef3ea7a744e9e5e4c54b9f6f99b0f8ad9964b74d89e00258ecd497784
fetched_at: '2026-06-29T00:10:41.966612+00:00'
page_id: '546686728'
product: rm
source: tdn-rm
title: LGPD - Serviços Via WebService FIN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546686728
version: 5
---

## **01. VISÃO GERAL**

Com base na [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) , implementamos algumas regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP e Rest.

Estas restrições se aplicam aos registros retornados (restrição de linha) ao consultar dados através destes serviços e implicam que um usuário só poderá ter acesso às informações que lhe pertencem, ou seja, informações que fazem referência a sua pessoa, e em caso de o usuário ser chefe ou supervisor o mesmo terá acesso aos dados de seus subordinados. Quando tiver permissão na tag serão retornados os registros de acordo com o filtro informado, do contrário irá aplicar o filtro por coligada. Para os serviços via SOAP as restrições de aplicam aos métodos "ReadView" e "ReadRecord".

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi criado o novo parâmetro ***"Desconsiderar Filtro de Produto em WebService",***com objetivo de que o sistema passe a considerar segurança dos datasevers, o novo parâmetro está localizado em **serviços globais - segurança - perfis,**em caso de o usuário estar vinculado a um perfil que não contenha permissão os datasevers retornarão apenas os seus próprios dados, ou em caso de ser chefe ou supervisor, retornará também os dados de seus subordinados.

OBS: Para que os outros dataservers que não foram atualizados para essa implementação funcione, ou até mesmo que mantenham o comportamento atual que o sistema já possuía, deverá dar permissão a esse novo parâmetro por coligada.

## **03.****LISTA DE DATASERVERS COM RESTRIÇÕES:**

| **FUNCIONALIDADE** | **DATASERVER** |
| --- | --- |
| Cadastro de Cliente/Fornecedor | FinCFODataBR |
| Cadastro de Lançamentos | FinLanDataBR |
| Cadastro de Boleto | FinBoletoData |
| Cadastro de Lançamentos | FinLanDataTBC |

]]>
