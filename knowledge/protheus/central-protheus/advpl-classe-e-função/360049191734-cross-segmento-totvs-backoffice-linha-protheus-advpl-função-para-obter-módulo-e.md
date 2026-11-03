---
article_id: 360049191734
category: ADVPL - Classe e Função
content_hash: a3ee18622200b370d45c78f995f9855b0ceec2fbde419fd655ee959e553109a6
fetched_at: '2026-06-28T22:40:16.824473+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função para obter
  módulo e permissões de acesso do usuário
type: support-article
updated_at: '2021-05-25T18:37:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049191734-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-para-obter-m%C3%B3dulo-e-permiss%C3%B5es-de-acesso-do-usu%C3%A1rio
---

**Dúvida**Existe alguma classe ou função que traga os módulos e acesso permitido para o usuário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Solução**

Atualmente não existe uma função equivalente.

É possível fazer usa das funções *FWSFAllUsers, PswOrder, PswSeek e PswRet* para gerar um resultado muito semelhante conforme exemplo abaixo:

```
#include "protheus.ch"  
  
function u_TestUsr()  
local aUsers as array  
  
aUsers := u_allUsers()  
varInfo("Users", aUsers)  
  
return nil  
  
user function allUsers()  
local aUsrAux as array  
local aUsers as array  
local nLoop as numeric  
local nOrder as numeric  
  
nOrder := PswOrder(1)  
aUsrAux := FWSFAllUsers()  
aUsers := {}  
  
for nLoop := 1 to len(aUsrAux)  
PswSeek(aUsrAux[nLoop][2])  
aAdd(aUsers, PswRet())  
next  
  
PswOrder(nOrder)  
  
return aUsers
```

**Saiba Mais**

**[FWSFAllUsers](https://tdn.totvs.com/display/PROT/FWSFALLUSERS)**

**[PswOrder](https://tdn.totvs.com/display/public/PROT/PswOrder+-+Seleciona+ordem+de+pesquisa)**

**[PswSeek](https://tdn.totvs.com/display/public/PROT/PswSeek+-+Pesquisa+o+arquivo+de+senhas)**

**[PswRet](https://tdn.totvs.com/pages/viewpage.action?pageId=267792734)**
