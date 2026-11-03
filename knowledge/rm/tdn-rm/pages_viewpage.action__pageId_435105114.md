---
content_hash: b12ab6fccf8a8dd205c0b4bf52aedd6842acf1b4d6b8b5eb2bcc33dc16331fbd
fetched_at: '2026-06-29T00:09:47.977035+00:00'
page_id: '435105114'
product: rm
source: tdn-rm
title: Imóveis - Ocupação de área por M²
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105114
version: 5
---

Este anexo tem como função associar as áreas do imóvel ao contrato de locação, indicando quanto de cada área será consumido.   
 Nesse cadastro temos comportamentos diferentes de acordo com o valor do campo "Tipo de Locação" do Imóvel que está sendo associado ao imóvel. Segue quais são esses tratamentos:

* **Tipo Locação Imóvel:** Ao inserir o imóvel, nenhuma área é carregada pois nesse tipo de locação não é permitido o cadastro de áreas.
* **Tipo Locação Áreas Fracionadas:** Ao inserir o imóvel as áreas associadas que possuem área disponível são carregadas no anexo, tendo o valor do campo "Área ocupada" com o valor do Área Disponível menos o valor da Área Reservada. É possível fazer a inclusão, edição e exclusão das áreas do Imóvel;
* **Tipo Locação Áreas Unificadas:**Ao inserir o imóvel as áreas associadas são carregadas no anexo, tendo o valor do campo "Área ocupada" com o valor do Área Disponível menos o valor da Área Reservada. A diferença para a Áreas Fracionada, é que não é possível a inclusão, edição e exclusão das áreas do Imóvel.

Ao incluir/editar um registro de ocupação, é exibida uma tela de cadastro com os seguintes campos:

* **Cód. Área:** Código de identificação preenchido automaticamente pelo sistema;
* **Contrato de Locação:** Exibe o contrato de locação que está associado ao imóvel da área que está sendo associada;
* **Imóvel:** Exibe o imóvel da área que está sendo associada;
* **Código da área do Imóvel:** Exibe a área do Imóvel que está sendo associado ao contrato de locação. Nesse campo é possível incluir somente áreas associadas ao imóvel que está associado ao Contrato de Locação e que estejam disponíveis.
* **Tipo de Área:** Exibe o "Tipo de Área" da Área que está sendo associada. Esse campo é preenchido ao inserir a Área do Imóvel;
* **Localização:** Exibe a "Localização" da Área que está sendo associada. Esse campo é preenchido ao inserir a Área do Imóvel;
* **Compõe Saldo:**Informa se a área compõe o saldo de área locada e do valor final do contrato. Este tipo de área, quando inserida, não tem a sua ocupação alterada pelo usuário. O valor da ocupação será sempre em 100% da área total. Esse campo é preenchido ao inserir a Área do Imóvel e não é possível ser alterado.
* **Área ocupada(m²):** Esse campo determina o quanto m² será utilizado da Área no Contrato de Locação. Esse campo já vem preenchido com o valor da Área Disponível subtraído o valor da Área Reservada. Esse campo só poderá ser editado quando o Imóvel for do Tipo Locação "Áreas Fracionadas". Se a área não compõe o saldo, então este campo estará desabilitado para edição.
* **Percentual Área Locada:** Exibe a porcentagem de locação da área que está associando;
* **Valor (m²):** Determina o valor por m² da Área que está sendo associada. Esse campo vem preenchido com o valor cadastrado na área do imóvel. Ele pode ser editado, caso o Imóvel a ser associado, possui o parâmetro "O locador aceita negociação do valor de locação" marcado.
* **Valor total:** Exibe o valor total da locação da área. O valor é obtido multiplicando o valor da Área ocupada pelo Valor do m². Ele pode ser editado caso o imóvel a ser associado possua o parâmetro "O locador aceita negociação do valor de locação" marcado.
* **Data Inicial:** Define a data de inicio da locação da área, vem preenchido com a data de inicio de locação do Contrato de Locação associado;
* **Data Final:** Define a data final da locação da área, no cadastrado esse campo vem bloqueado. Ele só será preenchido em caso de Aditivos ou Encerramento de Contrato.

**Observações**:

* Áreas que não compõem saldo podem ser incluídas no contrato de locação porém a sua ocupação não pode ser alterada. Os seus valores de m² e ocupação não afetam no cálculo do valor total do contrato de locação. Essas áreas podem ser incluídas para apenas um contrato de locação. Ao vincular um imóvel com áreas fracionadas a um contrato de locação, o sistema irá criar ocupações dessas áreas caso elas não estejam locadas em outro contrato.

Veja Também

---
