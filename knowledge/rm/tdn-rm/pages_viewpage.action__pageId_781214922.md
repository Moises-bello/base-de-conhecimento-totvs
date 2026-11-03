---
content_hash: 6792130312ec41edbbf6235b6cf90fc37957d6158c709a57ccb3e5734062fed1
fetched_at: '2026-06-29T00:11:38.157737+00:00'
page_id: '781214922'
product: rm
source: tdn-rm
title: Proposta - Usuário Portal de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781214922
version: 2
---

API de Usuário Portal de Imóveis

| Título | **API de Usuário Portal de Imóveis - GET** |
| --- | --- |
| Endpoint | <http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData> |
| Verbo | Get. |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Get, o sistema retorna a lista de usuários cadastrados na Tabela XPIUSUARIO do Portal de Imóveis. |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de Usuário Portal de Imóveis - POST** |
| --- | --- |
| Endpoint | <http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData> |
| Verbo | Post |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Post, o sistema irá cadastrar o usuário do Portal de Imóveis alimentando as seguintes tabelas:   * XPIUSUARIO: Tabelas que armazena os dados dos usuários do PI; * FCFO: Tabela (principal) que armazena os dados dos Clientes no financeiro; * XPESSOACONJUGE: Tabela que  armazena os dados do cônjuge dos clientes no TCGI; e * XCLIENTEPESSOAFISICA: Tabela que armazena os dados complementares dos clientes no TCGI; |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de Usuário Portal de Imóveis - PUT** |
| --- | --- |
| Endpoint | [http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID\_do\_Usuário\_na\_XPIUSUARIO]](http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID_do_Usuário_na_XPIUSUARIO) |
| Verbo | Put |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Put, o sistema irá atualizar os dados informados, para o usuário repassado na ID, na tabela XPIUSUARIO, que armazena os dados dos usuários do PI.  Ao utilizar este verbo é preciso informar todos os campos/tags do cadastro do usuário porque os campos que não forem informados serão setados como nulos.  Para atualizar somente um campo/tag, utilize o verbo Patch descrito mais abaixo. |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de Usuário Portal de Imóveis - PATCH** |
| --- | --- |
| Endpoint | [http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID\_do\_Usuário\_na\_XPIUSUARIO]](http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID_do_Usuário_na_XPIUSUARIO) |
| Verbo | Patch |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Patch, o sistema irá atualizar os dados informados, para o usuário repassado na ID, na tabela XPIUSUARIO, que armazena os dados dos usuários do PI.  Este verbo deve ser utilizado para atualizar os campos especificados, sem alterar o valor dos demais campos da tabela. |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de usuário Portal de Imóveis - DELETE** |
| --- | --- |
| Endpoint | [http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID\_do\_Usuário\_na\_XPIUSUARIO]](http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID_do_Usuário_na_XPIUSUARIO) |
| Verbo | Delete |
| Parameters | No parameters. |
| Descrição | Utilizando esta API com o verbo Delete, o sistema irá excluir os dados do usuário repassado no ID, na tabela XPIUSUARIO.  No exemplo de resposta abaixo, excluímos o usuário de ID 37, criado nos exemplos acima:  <http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/37> |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue
