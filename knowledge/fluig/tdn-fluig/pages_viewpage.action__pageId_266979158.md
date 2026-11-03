---
content_hash: ddd50a68ddce8f75a14535f25da2c8179ea02047cf9b91a9067c26d4cccdee33
fetched_at: '2026-06-28T21:35:23.854721+00:00'
page_id: '266979158'
product: fluig
source: tdn-fluig
title: ESB - Como consumir informações de um sistema que não possui WS através do
  TOTVS ESB?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266979158
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS ESB

# Ocorrência

É necessário consumir informações de um determinado sistema que não possui Web Services e cujo banco de dados é ORACLE. É possível consumir as informações via TOTVS ESB, e gerar um WS a partir dele para ser consumido pelo TOTVS Fluig Plataforma e por outras aplicações?

# Solução

É possível disponibilizar as informações em formato TXT ou XML para o TOTVS ESB e ele recebe essas informações, realiza a transformação e envia para o Web Service do TOTVS Fluig Plataforma

Os componentes abaixo serão utilizados:

* [TOTVS Sender](http://tdn.totvs.com/display/fluig/TOTVS+Sender)
* [Transformer](http://tdn.totvs.com/display/fluig/Transformer)
* [FILE Sender](http://tdn.totvs.com/display/fluig/FILE+Sender)
