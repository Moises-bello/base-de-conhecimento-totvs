---
content_hash: b57c057a1ecfbe126f0312b737b31e74ad602f43a909e0647b6a311c645d1058
fetched_at: '2026-06-29T00:08:58.113387+00:00'
page_id: '359473603'
product: rm
source: tdn-rm
title: 'TAF - Erro: A chave EnableNumber deve estar configurada no LicenseServer.ini
  como 1.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359473603
version: 3
---

Erros e AçõesErro

Erro: A chave EnableNumber deve estar configurada no LicenseServer.ini como 1.

Ação

Ação:

Para corrigir a inconsistência, é necessário alterar as configurações no arquivo do ambiente de instalação do License Server.

No servidor de licença, dentro da pasta onde foi instalado o arquivo de licença, o usuário deve localizar o arquivo TOTVSAPPSERVER.ini. Este arquivo possui a tag ‘EnableNumber = 0’, que deverá ser alterada para ‘EnableNumber =1’.
