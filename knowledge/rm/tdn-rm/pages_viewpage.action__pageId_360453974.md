---
content_hash: 0abd6067df319e6979d375db44827a72a9403e87e52decf8a975c226466cf8ec
fetched_at: '2026-06-29T00:08:58.657703+00:00'
page_id: '360453974'
product: rm
source: tdn-rm
title: Tipo de Referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=360453974
version: 4
---

# Visão Geral dos processos WebSevices de Tipo de Referência

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de tipo de referência através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de tipo de referência no TOTVS Gestão Bibliotecária.

Através do dataserver "**BibTipoRef****Data**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de tipo de referência no TOTVS Gestão Bibliotecária.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de um tipo de referência. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código.

O sistema irá realizar a consulta de tipo de referência, caso as informações passadas estejam de acordo com algum tipo de referência já existente no sistema.

### **Consulta de tipo de referência**

Para realizar a consulta de um tipo de referência, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA******e CODIGO*** como informações da chave para busca do tipo de referência.

xmlExemplo de XML para consulta de um Tipo de Referênciatrue

BibTipoRefData

1;4

CODCOLIGADA=1
]]>xmlExemplo do retorno de consulta de Tipo de Referênciatrue

1
4
Tipo de Referência
TR
]]]]>
]]>xmlExemplo do retorno sem registrostrue<BibTipoRef/>
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um tipo de referência. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de um tipo de referência, caso o código informado não exista na base.

Se o Código existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

### **Inclusão de tipo de referência**

Para realizar inclusão de um tipo de referência, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para o tipo de referência.

Caso o código informado não exista, será incluído um novo tipo de referência. Caso contrário, o mesmo terá suas informações atualizadas.

O **XML** deve conter a tabela **LTipoRef**com os campos ***CODCOLIGADA******e CODIGO*** como informações da chave para o cadastro de tipo de referência e, também, os campos obrigatórios para seu cadastro.

O código será sempre criado automático, dessa forma, informaremos o registro como "0".

xmlExemplo de XML para inclusão de um Tipo de Referênciatrue

BibTipoRefData



1
5
Tipo de Referencia
TR
]]]]>

CODCOLIGADA=1
]]>xmlExemplo do retorno da inclusão de Tipo de Referênciatrue1;5]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o código inserido no item ***SaveRecordResult.***

### **Alteração de tipo de referência**

Para realizar alteração de um tipo de referência, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de tipo de referência.

O **XML** deve conter a tabela **LTipoRef**com os campos ***CODCOLIGADA******e CODIGO***como informações da chave para a atualização do cadastro de tipo de referência.

xmlExemplo de XML para alteração de informações de Tipo de Referênciatrue

BibTipoRefData



1
5
Tipo de Ref
TiR
]]]]>

CODCOLIGADA=1
]]>xmlExemplo do retorno da alteração do cadastro de Tipo de Referênciatrue1;5
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de um tipo de referência. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de um código caso encontre o registro.

### **Exclusão de tipo de referência**

Para realizar exclusão de um tipo de referência, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de tipo de referência.

O **XML** deve conter a tabela **LTipoRef**com os campos ***CODCOLIGADA******e CODIGO*** como informações da chave para o cadastro de tipo de referência e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de um Tipo de Referênciatrue

BibTipoRefData



1
5
Tipo de Ref
TiR
]]]]>

CODCOLIGADA=1
]]>xmlExemplo do retorno de exclusão de Tipo de ReferênciatrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
