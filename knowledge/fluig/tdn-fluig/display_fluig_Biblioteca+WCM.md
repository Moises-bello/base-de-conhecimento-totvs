---
content_hash: c42548744d054b8e85cc7f04b10d79ec4484a88c9e9f4ad524e06df8ee3867b8
fetched_at: '2026-06-28T21:35:18.886869+00:00'
page_id: '185748245'
product: fluig
source: tdn-fluig
title: Biblioteca WCM
type: documentation
url: https://tdn.totvs.com/display/fluig/Biblioteca+WCM
version: 20
---

# Índice

none4.\*ndicetrue

# Objetivo

O objetivo deste guia é apresentar as características da biblioteca WCM.

# Conceito

A biblioteca WCM contém os elementos básicos que podem ser inseridos num *layout* na sua montagem, elementos tais como menu, cabeçalho e rodapé da página.

# Importação da biblioteca

Para utilizar a biblioteca WCM é necessário fazer a sua importação no *layout*. A importação é feita inserindo o seguinte código no topo do arquivo do *layout*:

xml]]>

Após importada, sua utilização é feita da seguinte maneira:

xml
 
Ex:
<@wcm.header authenticated="true"/>
<@wcm.menu />]]>

# Funções disponíveis

As funções disponíveis na biblioteca WCM são apresentadas nos quadros a seguir:

11HeaderHeader

### ***Header***

Insere o cabeçalho no *layout*, podendo indicar por parâmetro se é publico ou não.

]]>

| Parâmetro | Valores | Valor padrão | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| ``` authenticated ``` | true/false | false | Não | Indica se o cabeçalho é publico ou se o usuário precisa estar logado para visualizá-lo. |

**Figura 1 - Cabeçalho do *layout***

2MenuMenu

### Menu

Insere o menu no *layout* e não possui parâmetros.

]]>

**Figura 2 - Menu lateral do *layout***

3RenderSlotRenderSlot

### ***RenderSlot***

Insere um *slot* no *layout*. Os parâmetros incluem o id do *slot* e se o *slot* é editável ou não.

]]>

| Parâmetro | Valores | Valor padrão | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| id | string | Não possui | Sim | Valor do id do *slot*. Ex.: "SlotA". |
| decorator | true/false | false | Não | Indica se o título do *widget* será renderizado. |
| editableSlot | true/false | false | Não | Indica se o *slot* é editável ou não. |
| class | string | Não possui | Não | Classe CSS a ser inserida no *slot*. |

**Figura 2 - *Slot* do *layout***

1FooterFooter

### ***Footer***

Insere o rodapé no *layout*. Recebe por parâmetro a chave da *label* a ser exibida antes do nome do usuário.

]]>

| Parâmetro | Valores | Valor padrão | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| layoutuserlabel | string | Não possui | Sim | Chave i18n da label a ser exibida antes do nome do usuário.  Ex.: **Usuário**: João da Silva |

**Figura  4 - Rodapé do *layout***
