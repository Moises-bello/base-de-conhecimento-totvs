---
content_hash: 62393891972f84c082d4842ae7010659dc165e6b24c54ce3f9416fb2fef814a5
fetched_at: '2026-06-29T00:11:03.546068+00:00'
page_id: '624131202'
product: rm
source: tdn-rm
title: Provider de Anonimização de Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624131202
version: 2
---

## **Descrição**

O provider de aluno foi criado para circundar as regras de anonimização de aluno do educacional, entretanto, por obrigação legal nenhum aluno poderá ser anonimizado. Toda anonimização é necessário que provider localize o seu CPF e este é feito por duas formas, passando o próprio CPF ou o número da carteira de identidade (RG).

## **Serviços**

A seguir segue os serviços disponíveis para utilizar via chamada API.

### **CanAnonimize**

Serviço que tem como resultado se pode ou não a anonimização do aluno por parte das regras do Educacional. Segue abaixo alguns possíveis cenários.

* Aluno existe na base de dados com CPF preenchido e a requisição é feita pelo CPF. Retorno do provider é que **não** é possível **anonimizar****.**

* Aluno existe na base de dados com CPF preenchido e a requisição é feita pela CARTIDENTIDADE.  Retorno do provider é que **não** é possível **anonimizar****.**

* Aluno existe na base de dados sem CPF preenchido e a requisição é feita pelo CPF.  Retorno do provider é que **é** possível **anonimizar****.**

* Aluno existe na base de dados sem CPF preenchido e a requisição é feita pelo CARTIDENTIDADE.  Retorno do provider é que **é** possível **anonimizar.**
