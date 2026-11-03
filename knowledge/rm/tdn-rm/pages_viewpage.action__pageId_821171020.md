---
content_hash: 0e592090e003d5c972f6e598381855e7c64d2008a6d898fabdc39f5ad6b86d71
fetched_at: '2026-06-29T00:11:45.685431+00:00'
page_id: '821171020'
product: rm
source: tdn-rm
title: Integração Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821171020
version: 2
---

## Objetivo

Informar os dados de configuração da integração com o Fluig.

## Configuração

Na tela de Parâmetros Globais, selecione a Aba, Integração Fluig

Informe os dados necessários para realizar a conexão com o Fluig.

O Endereço do servidor do fluig, deve ser informado no formato com protocolo e porta(se necessário), exe: <http://10.0.0.1:8080/>  
Este endereço será acrescido da rota de integração do serviço do fluig.  
Dessa forma é esperado que o Endereço informando neste campo seja do servidor do Fluig, apenas com a rota base.

## Testar Conexão

Ao clicar em testar de conexão, o endereço informado será acrescido da rota de serviço do fluig, "webdesk/ColleagueService", exe: [http://10.0.0.1:8080/webdesk/ColleagueService](http://10.0.0.1:8080/)

Caso seja informado por exemplo: <http://10.0.0.1:8080/>portal/, o teste de conexão não será bem sucedido e a integração não será realizada, pois a rota acrescentada do serviço, poderá não existir.
