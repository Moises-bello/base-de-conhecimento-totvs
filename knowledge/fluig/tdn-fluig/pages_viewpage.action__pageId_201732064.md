---
content_hash: 1906e1873b42cd3e81e84be96828157324734b9b54e6f384b7e23f745cfcddc2
fetched_at: '2026-06-28T21:35:19.291802+00:00'
page_id: '201732064'
product: fluig
source: tdn-fluig
title: DES - Por que está ocorrendo o erro "Read Timed Out" ao chamar um WebService
  CXF em desenvolvimentos sobre a plataforma?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201732064
version: 11
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

**Tipo de API:** Web service

# Ocorrência

Ocorre o erro "*Read Timed Out"* ao acessar um *WebService* CXF via desenvolvimento sobre a plataforma. O método parece executar internamente, porém demora demais e esse erro aparece antes de terminar o processamento do método em questão. ~Poderiam me ajudar?

# Causa

O Web Service está configurado para um tempo menor que o necessário ou utilizando o tempo padrão de trinta segundos, que não está sendo o suficiente.

# Solução

Conforme exemplo abaixo, deve-se configurar o WebService CXF antes de enviar a execução do método.

js

Outra forma possível é utilizando o método getCustomClient, conforme documentado segundo o link: 

Este código foi retirado de um tutorial nos blogs de auxílio de desenvolvimento ao Apache CXF ([link](http://lhein.blogspot.com.br/2008/09/apache-cxf-and-time-outs.html)) e serve apenas para envios de requisições via *stubs*, não servindo para envios de XML puros, ou seja, fora do padrão da plataforma de envio de requisições a serviços.
