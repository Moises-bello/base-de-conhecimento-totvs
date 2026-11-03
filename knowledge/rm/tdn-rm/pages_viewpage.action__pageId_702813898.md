---
content_hash: 8fb676ebca2679fdbc94d9dc8338290dfbb787a89834851534dc30172c9253c9
fetched_at: '2026-06-29T00:11:22.420764+00:00'
page_id: '702813898'
product: rm
source: tdn-rm
title: NFS-e - Item da lista de serviço (Código de Serviço Federal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=702813898
version: 17
---

#f5f5f5#363636noneItem da lista de Serviço (NFS-e)

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

O campo Código de Serviço Federal, que fica no cadastro do produto anexo , refere-se ao Item da lista de serviço definido pela Lei Complementar 116, de 31 de Julho de 2003. Neste documento iremos indicar como este campo é gerado no XML da NFS-e.

## **02. Cadastro do ServiçoCadastro**

Apesar do código ter sido definido através da Lei Complementar 116/03, algumas prefeituras validam uma máscara diferente. Abaixo seguem alguns exemplos:

**Lei Federal:** 1.01 - Análise e desenvolvimento de sistemas

**Prefeitura A:** 01.01 - Análise e desenvolvimento de sistemas

**Prefeitura B:** 1.01 - Análise e desenvolvimento de sistemas

**Prefeitura C:** 101 - Análise e desenvolvimento de sistemas

No RM temos dois locais para cadastrar de código do serviço federal, um em anexo do produto, "[Dados Fiscais do Produto](https://tdn.totvs.com/display/LRM/Dados+Fiscais+do+Produto)" e outro também no anexo do produto, "[Tributos do Produto por Município](https://tdn.totvs.com/pages/viewpage.action?pageId=423938770#TributosdoProdutoporMunic%C3%ADpio-NFS-e)".

CadastroDados Fiscais do Produto

No anexo, "Dados Fiscais do Produto" o cadastro deve sempre ser preenchido com a definição da lei federal e o processo de montagem do XML da NFS-e irá adequar o código conforme a necessidade de cada prefeitura

Exemplo: "**8.01****- Ensino regular pré-escolar, fundamental, médio e superior"** deverá ser cadastrado com o código **8.01** independente da forma como deverá ser gerado no xml da nota

Tributos do Produto por Município

No anexo "Tributos do Produto por Município" o cadastro deve obedecer a máscara encontrada no Schema de cada prefeitura

Exemplo: O código "**8.01****- Ensino regular pré-escolar, fundamental, médio e superior"** deverá ser preenchido no sistema conforme as regras de cada prefeitura. podendo ser "**08.01.01**" ou "**8.01.01**" etc.

****03. XML da NFS-eNFSe****

O XML da NFS-e, de qualquer município, é montado conforme o  com o TSS e no momento da montagem do XML o processo irá alterar a máscara do Item da Lista de Serviço conforme configurado pelo processo

**Importante:** Para movimentos que possuírem mais de um item:

Consideramos o primeiro item como base, desta forma verificamos se ele possui o código de serviço federal preenchido no anexo: Tributos do produto por município, caso não tenha, é buscado o código de serviço federal do Anexo: Dados Fiscais e aplicado a mascara de acordo com o município. 

Em seguida, validamos se o seguinte item possui o código se serviço federal preenchido no anexo: Tributos do produto por município, caso tenha, ele é comparado com o encontrado anteriormente. Se forem iguais o código é mantido, se forem diferentes, é apresentado mensagem de erro informando que os códigos precisam ser iguais, caso ele esteja vazio é buscado o código de serviço federal do Anexo: Dados Fiscais e aplicado a mascara de acordo com o município. Feito isso o código encontrado é comparado com o código encontrado no primeiro item, caso sejam iguais o código é mantido, caso contrario é apresentado mensagem de erro informando que os códigos precisam ser iguais.  E assim sucessivamente até percorrer todos os itens.
