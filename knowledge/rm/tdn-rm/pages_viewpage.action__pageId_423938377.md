---
content_hash: 34ec24a261c9000139d63d136ee535d89bc5c8bde4614b73f77eb2f1f74e09e2
fetched_at: '2026-06-29T00:09:26.707480+00:00'
page_id: '423938377'
product: rm
source: tdn-rm
title: Eventos Contábeis Patrimoniais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938377
version: 27
---

* ### [Cadastro de Eventos Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=423938693)
* ###
* ###
* ###
* ###

* ###

### **Aplicação da Classificação do Centro de Custo no Evento Contábil**

Disponibilizada melhoria no Evento Contábil que possibilita ao usuário definir sobre qual contexto do evento contábil a classificação do centro de custo informada deverá ser aplicada, neste caso disponibilizamos para "Item do evento (este item)". Ao efetuar a contabilização de patrimônios através de evento contábil, a classificação do centro de custo irá afetar sobre os itens da contabilização de acordo com a parametrização definida no evento contábil.

**Classificação da Conta:** Se desejar, poderá informar neste campo a classificação da conta, cadastrada no default contábil da "Tabela" selecionada, desta forma, caso existam mais de uma conta no default indicado, o sistema só buscará para a contabilização a conta que tiver a classificação aqui informada.

**Exemplo**

Vamos supor que foi informado para um determinado item do evento contábil, que o sistema deverá buscar o default de débito da filial, com classificação igual a "FIL01" e que no cadastro de filial FXXX nos defaults a débito existem as seguintes contas informadas:

Conta           Classificação

1.1.1.0001    FIL00

1.1.1.0002    FIL01

1.1.1.0003    FIL02

Neste caso, utilizando-se a filial FXXX, com o evento contábil descrito neste exemplo, o sistema só irá buscar a conta contábil 1.1.1.0002 para lançamento do débito.

**Observação**

Caso, na tabela default utilizada, exista mais de uma conta contábil incluída como default a débito/crédito e não seja informada no item do evento contábil a "Classificação da Conta", o sistema irá buscar todas as contas encontradas, ocasionando diferenças entre os valores de Débito/Crédito na contabilização.

**Classificação Centro de Custo:**

Se informada, a classificação de centro de custo será utilizada como filtro das/para as contas informadas no default contábil da tabela default informada semelhante à classificação da conta mas com o acréscimo das particularidades abaixo que utilizam também a classificação do centro de custo.

O funcionamento deste filtro da(s) conta(s) é de acordo com a classificação de centro de custo do registro que está sendo contabilizado que observa a classificação do centro de custo no item do evento contábil e a classificação da conta para então recuperar a(s) conta(s) a ser utilizada na criação da partida.

Se nenhuma classificação de centro de custo for informada o sistema respeitará a regra apenas da classificação da conta (caso informada).

**Aplicar Classificação do C. Custo sobre:**

* **Item do evento (este item)**  
  Indica que o filtro da classificação do centro de custo, será aplicado somente sobre as partidas contábeis que serão geradas pelo default contábil do item parametrizado no campo "Buscar default em".

**Uso de fórmula no evento contábil:** Quando for utilizado fórmula será permitida a contabilização do lançamento com valor diferente do valor esperado pela ocorrência, aquisição ou transferência de controle.

Maiores detalhes consultar [Itens Evento](http://tdn.totvs.com/pages/viewpage.action?pageId=423938464) do cadastro de Eventos contábeis do módulo Contábil
