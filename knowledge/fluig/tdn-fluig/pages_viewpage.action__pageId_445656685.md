---
content_hash: 6dc91e3e87216b325eae8f21dd3824da26ac746e2a16ae16620b7f37f4042964
fetched_at: '2026-06-28T21:35:27.020550+00:00'
page_id: '445656685'
product: fluig
source: tdn-fluig
title: Como expor dados em ambientes públicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445656685
version: 11
---

Atenção

Esta página foi revisada para considerar as configurações do TOTVS Fluig Plataforma a partir da **atualização 1.6.5 - Liquid**.

# Índice

true.\*ndicenone

# Objetivo

---

Existem algumas situações em que as páginas públicas precisam acessar informações disponíveis na plataforma para interagir com o cliente.

Este guia tem o objetivo de apresentar uma técnica segura para liberar o acesso às informações disponíveis no TOTVS Fluig Plataforma sem requisitar autenticação.

## Introdução

Alguns parceiros e clientes utilizam o OAuth para realizar as chamadas nas APIs, no entanto a chave fica localizada dentro da página. Essa técnica não é recomendada, pois um atacante pode se apossar da chave que está publicamente acessível e obter acesso irrestrito ao dados.

Para evitar essa situação, foi criada uma técnica que se baseia em duas etapas:

1. Na instalação de um componente ou aplicativo da Store serão criadas chaves através da classe *activator* configurada. Para a criação das chaves de autenticação deve ser definido um código que obedece ao padrão de 4 pares de 4 caracteres: XXXX-XXXX-XXXX-XXXX.
2. Esse código será usado posteriormente para buscar os *tokens* que serão usados na autenticação. Essa etapa será realizada dentro da camada REST no servidor, desta forma somente os dados que forem necessários serão expostos, e fica a cargo da implementação gerenciar a segurança destes dados.

## Como utilizar

Para realizar essa implementação, siga os passos abaixo:

falsePassos01Passo 01

Inclua a dependência do projeto **fluig-sdk-keyring**, que existe a partir da **atualização 1.6.5 - Liquid**:

com.fluig
fluig-sdk-keyring
${fluig.version}
compile
]]>02Passo 02

Depois implemente o **activator** conforme a documentação técnica de[Eventos de Componentes](http://tdn.totvs.com/display/fluig/Eventos+de+Componentes) e no método **enable** inclua a chamada ao método Keyring.

java

Para consultar um exemplo de implementação no GIT, [clique aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/sample-component/sample-component-service/src/main/java/com/samplecomponent/activate/oauth/Activate.java).

03Passo 03

Na classe que implementa o serviço REST, utilize **Keyring.getKeys(tenantId, <CHAVE>)**. Este método vai retornar as chaves que serão utilizadas para fazer a autenticação via OAuth nas requisições.

Para assinar a requisição recomendamos utilizar a biblioteca**signpost-core**, dependência e exemplo a seguir:

oauth.signpost
signpost-core
1.2.1.1
]]>javaExemplo

Para consultar um exemplo de implementação no GIT, [clique aqui.](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/sample-component/sample-component-rest/src/main/java/com/samplecomponent/rest/SampleActivateRest.java)

Exemplos de desenvolvimento de componentes

Consulte nosso repositório de [exemplos de desenvolvimentos de componentes](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/sample-component)para mais informações sobre o desenvolvimento, os projetos e componentes. 

## Recursos criados

Pronto! Após realizar esses passos, deve ser possível o acesso às informações disponíveis no TOTVS Fluig Plataforma sem autenticação.

Atenção!

No provisionamento das chaves são criados alguns recursos que não devem ser alterados ou excluídos.

* OAuth Provider com o nome customapps-<TENANT\_ID> no tenant que o componente foi ativado.
* OAuth Application com o código: <KEY>-<TENANT\_ID>
* Application User: integration-<KEY>-<TENANT\_ID>
