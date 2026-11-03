---
content_hash: cf3ecd0ddd3d2753b0d4789da6086f61d410ecd115c731df3064ba1ad401e539
fetched_at: '2026-06-29T00:05:52.839429+00:00'
page_id: '1060235270'
product: rm
source: tdn-rm
title: WhiteList de servidores
type: documentation
url: https://tdn.totvs.com/display/LRM/WhiteList+de+servidores
version: 3
---

# **Informações**

---

A funcionalidade de *WhiteList* (lista branca) tem o proposito de controlar quais servidores em uma instalação podem executar a integração com o SmartLink.

Para utilizar a funcionalidade, é necessário acesso direto ao banco de dados, visto que todo o processo é feito por consultas SQL.

A WhiteList **não é** obrigatória para o funcionamento da integração. Caso ela esteja vazia, todos os servidores executarão a integração.

# **Funcionamento**

---

A *WhiteList* funciona por criar uma lista de servidores, dentre os quais a integração com o SmartLink seleciona para executar.

Ela existe através da tabela de banco **GNOTIFYSERVERWHITELIST**.

Esta tabela possui apenas um campo envolvido no funcionamento, que é a coluna **SERVERNAME**. As outras colunas são apenas de controle de criação/modificação.

### Inserindo um servidor

Para inserir um servidor na lista, execute o comando abaixo, substituindo os valores de acordo com a legenda:

* + ***NOMEDOSEUSERVIDOR*:** o endereço do servidor
  + ***PORTA*:**a porta da comunicação WCF do host desejado. Por padrão, o RM utiliza a porta 8050; mas pode ser trocada através da tag *Port* na configuração do host.

sql

Após a inserção, a integração **somente** executará utilizando o servidor inserido.

Vários servidores podem ser incluídos nesta lista.

### Verificando os servidores

Podemos verificar os servidores que estão na lista executando o comando a seguir:

sql

Desta forma, serão retornados os servidores permitidos a executar a integração.

### Removendo um servidor

Para remover um servidor da lista, basta executar o comando abaixo, novamente substituindo os respectivos valores:

sql
