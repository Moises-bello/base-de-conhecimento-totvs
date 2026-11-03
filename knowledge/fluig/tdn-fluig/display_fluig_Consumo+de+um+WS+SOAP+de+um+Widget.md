---
content_hash: 6c3a7e4bc062d1ba149fa1151e81f8e886cc67d2a94d2e004bde54b8ff52b4b0
fetched_at: '2026-06-28T21:35:18.638022+00:00'
page_id: '179700175'
product: fluig
source: tdn-fluig
title: Consumo de um WS SOAP de um Widget
type: documentation
url: https://tdn.totvs.com/display/fluig/Consumo+de+um+WS+SOAP+de+um+Widget
version: 12
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é apresentar um exemplo de como consumir um *WebService*SOAP de um *widget*.

# Pré-requisitos

---

Para que se tenha uma compreensão completa destas informações, alguns conhecimentos são considerados pré-requisitos, entre eles:

* Visão geral sobre o fluig
* Visão geral sobre integração de sistemas
* WebServices
* SOAP

Informação:

Chamadas SOAP realizadas dentro de uma página (via widget) utilizam a sessão atual do usuário, ou seja, assumem o usuário logado. Porém, caso um login seja informado na chamada, a plataforma verifica se ele corresponde ao usuário da sessão.

# Consumir um WS SOAP de um *Widget*

---

Neste exemplo é utilizado o *WebService* ECMCardService, método Create para criar um registro de formulário.

Antes de iniciar, é necessário existir um *template* de formulário publicado no fluig, como o modelo a seguir:

xmlTemplate de formulário
