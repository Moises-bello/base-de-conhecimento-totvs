---
content_hash: fd499611889b7faf9950bc865e283783076676e64ed5bd24406c852330b3054a
fetched_at: '2026-06-29T00:12:07.356385+00:00'
page_id: '923577621'
product: rm
source: tdn-rm
title: Débito automático online Bradesco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=923577621
version: 6
---

# Conteúdo:

Conteúdo:

# 1. Débito automático online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de débito automático online registrado no Banco Bradesco.

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite uso do débito automático online" na aba "Débito online" caso a  selecionada possua os dados bancários correspondentes ao Banco Bradesco e definir os parâmetros de acordo com os dados fornecidos pelo banco. 

* **Ambiente**: Define o ambiente que será feito o débito automático.
* **URL do serviço de débito automático**: Deve ser informada a URL do serviço de débito automático disponibilizada pelo banco.
* **URL do serviço de homologação de débito automático**: Deve ser informada a URL do serviço de homologação de débito automático disponibilizada pelo banco.
* **URL do sistema autorizador**: Deve ser informada a URL do sistema autorizador disponibilizada pelo banco.
* **URL de serviço de homologação do sistema autorizador**: Deve ser informada a URL de serviço de homologação do sistema autorizador disponibilizada pelo banco.
* **Client ID**: Deve ser informado o código do cliente gerado pelo banco.
* **Certificado digital**: Deve ser informado o certificado digital que foi cadastrado junto ao banco.
