---
content_hash: 5161a5b57396b23124b68e70e7354723f41b18f611da123db6aa66e96c7a1b4a
fetched_at: '2026-06-28T21:35:19.158743+00:00'
page_id: '196809616'
product: fluig
source: tdn-fluig
title: DES - Desenvolvimento de formulários - componente de zoom
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=196809616
version: 24
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

**Versão:**  Anteriores a 1.5.1

# Ocorrência

A partir da atualização 1.6.1 está disponível o novo componente de zoom de datasets visando uma melhor experiência de uso em dispositivos móveis.

Importante

A técnica antiga de zoom, descrita na documentação abaixo, ainda é suportada pela plataforma. Porém, recomendamos fortemente a utilização da técnica atualizada, descrita na documentação de  que está de acordo com os padrões do Style Guide e permite maior fluidez utilizando o componente.

# Documentação

Este componente de zoom permite a consulta de entidades e outros formulário criados na plataforma para seleção de dados pelo usuário.

O acesso a este componente é realizado a partir de uma chamada Javascript no HTML da definição de formulário.

html/xml

Onde:

* **title:** é o título para a janela de zoom.
* **datasetId:** é o nome do dataset (Built-in, CardIndex ou Customized).
* **dataFields:** são os nomes dos campos a serem apresentados.
* **resultFields:** são os campos que devem ser retornados para o registro selecionado pelo usuário.
* **likeField:** o nome do campo para filtro de dados (se necessário).
* **likeValue:** o valor a ser usado no filtro de dados (se necessário).

**ATENÇÃO**: Este parâmetro só é válido para **datasets internos**. Datasets customizados **não** permitem a utilização de filtros.

* Para obter o registro selecionado pelo usuário devemos adicionar a seguinte função JavaScript ao formulário do processo:

html/xml

Onde *selectItem* é o registro selecionado pelo usuário na tela de zoom.

Importante

A mesma função “setSelectZoomItem” será usada para receber o resultado de todas as chamadas ao zoom. Assim, para diferenciar cada chamada foi criado o parâmetro *type*. Esse parâmetro é retornado em *selectedItem* e pode ser usado para diferenciar as chamadas ao zoom.

* Para acessar um campo do registro selecionado:

html/xml

Onde *fieldName* é o nome do campo de retorno que foi definido na chamada de zoom. O componente de Zoom da plataforma foi desenvolvido para permitir que o recurso de zoom fosse utilizado em definições de formulários.

Para que seja possível visualizar e resgatar informações dos campos *“metadatas”* do formulário, é necessário utilizar a seguinte nomenclatura:

|  |  |
| --- | --- |
| metadata\_id | Retorna o código do registro de formulário |
| medatata\_version | Retorna a versão do registro de formulário |
| metadata\_parent\_id | Retorna o código da pasta Pai |
| metadata\_card\_index\_id | Retorna o código do formulário |
| metadata\_card\_index\_version | Retorna a versão do formulário |
| metadata\_active | Versão ativa |

Abaixo um exemplo de código utilizado para visualização e resgate destes valores:

html/xml

A utilização da PK nos filtros ao utilizar dataset de Grupo, Papel ou Colaborador é opcional, porém o mesmo valor utilizado na URL do zoom deve ser utilizado para a obtenção do valor selecionado, conforme exemplo abaixo.

html/xml
 ]]>

Para utilizar filtros a chamada, é similar ao de *dataFields*.

html/xml

Neste exemplo, o zoom irá retornar somente os registros de formulários inativos.
