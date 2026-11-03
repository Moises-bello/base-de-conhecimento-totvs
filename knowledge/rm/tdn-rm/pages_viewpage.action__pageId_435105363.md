---
content_hash: 79bc2f083a9e7ec98d37717c3dfa42645c48831df364e9114074f11c8351b8d3
fetched_at: '2026-06-29T00:09:50.073887+00:00'
page_id: '435105363'
product: rm
source: tdn-rm
title: Imóvel - Anexo - Período de Indisponibilidade do Imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105363
version: 6
---

A funcionalidade permite que se cadastre períodos em que o  ficará indisponível.

* **Concedendo Permissões para Acesso a Funcionalidade**

* **Menus de Acesso**

* **Tabela Dinâmica**
  + Para informar o **Motivo** da indisponibilidade é necessário cadastrar os motivos na **Tabela Dinâmica de Motivo:**

   
   
 

* **Cadastro de Período de Indisponibilidade**

* + **Código:** Campo com a informação do Identificador gerado de forma automática e sequencial
  + **Imóvel:** Campo que tem o imóvel para o qual se está cadastrando o Período de Indisponibilidade. Ele é automaticamente associado dado que se trata de um cadastro anexo
  + **Data Início e Data Fim:** Definem o período em que o imóvel ficará indisponível
  + **Motivo:** Campo usado para identificar o motivo pelo qual o imóvel ficou indisponível. A ideia deste campo é possibilitar ao usuário uma forma de agrupar, filtrar e pesquisar pelos motivos que deixam um imóvel indisponível
  + **Observação:** Campo que o usuário pode usar para colocar alguma informação que ele julgar pertinente
* **Validações**
  + Ao salvar um cadastro de **período de indisponibilidade** para um imóvel que esteja em um **contrato de locação efetivado** e cujo período de vigência coincida com o período de indisponibilidade, a situação será informada ao usuário dando ele a escolha de continuar e salvar o cadastro ou cancelar a operação.
  + Ao se tentar efetivar um **contrato de locação** cujo período de vigência coincida com o **período de indisponibilidade** de algum dos imóveis do contrato, a situação será informada ao usuário e **não será possível a efetivação deste contrato.**
  + Ao tentar incluir um imóvel em um contrato, cujo **período de indisponibilidade** coincida com o inicio de locação deste contrato, esta situação será informada ao usuário e **não será possível a efetivação deste contrato.**
  + Ao efetivar **aditivos de prorrogação de vigência do contrato**, será validado se os imóveis pertencentes a este contrato estão com **indisponibilidade cadastrada** que coincida com o **novo período de vigência definido pelo aditivo**. Caso exista esta situação, será exibida uma mensagem para o usuário mostrando quais são os contratos/aditivos foram identificados e é dada ao usuário a possibilidade de proceder com a efetivação ou cancelá-la.
  + Ao efetivar **aditivos de renegociação de contrato que incluam imóveis**, se algum imóvel incluído possuir uma **indisponibilidade cadastrada** que coincida com o **período de vigência do contrato**, será apresentada uma mensagem listando os contratos/aditivos identificados e é dada ao usuário a possibilidade de proceder com a efetivação ou cancelá-la.
