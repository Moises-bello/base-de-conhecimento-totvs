---
content_hash: 21be350df34dd4915d212b59ede93b5d53d5f4fa2c46e1fac22d74b479d2cc56
fetched_at: '2026-06-28T21:35:24.780737+00:00'
page_id: '271655314'
product: fluig
source: tdn-fluig
title: BPM 090 - Como solucionar o erro na movimentação de atividades de serviço?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271655314
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Dentro de um processo que utiliza atividades de serviço, estas não são movimentadas automaticamente, ficando a atividade pendente com o usuário System:Auto, nem mesmo o fluxo de contorno pode ser executado.

No log do servidor é exibida a seguinte mensagem:

java

# Causa

A fila JMS referente a atividade de serviço não foi criada durante a atualização do fluig

# Solução

Para que esta fila seja criada, será necessário incluir, no arquivo standalone.xml, o seguinte trecho de código:

java



true
]]>

Para tal, busque por "jms-queue" e insira junto com as outras filas.

# Observações

Caso seu ambiente seja cloud, será necessário entrar em contato com o time responsável para atualização.
