---
content_hash: a72a7c5075240d6b265f690b7e5fbfaeb9b51bfd0752280f6c5d534c50be2212
fetched_at: '2026-06-29T00:08:51.684218+00:00'
page_id: '337361513'
product: rm
source: tdn-rm
title: Como verificar as configurações do Proxy do servidor do TSS?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337361513
version: 6
---

O Proxy atua como um intermediário entre uma rede local e a Internet e pode barrar as conexões de Web Service do TSS. Após realizar toda a instalação do TAF e do TSS, é necessário avaliar as configurações do Proxy do servidor conforme os passos abaixo:

* Acesse o Painel de Controle e clique em Opções da Internet:

* Clique na aba Conexões e em seguida em Configurações de LAN:

* Verifique no campo Servidor Proxy se a opção está habilitada:

* Caso o acesso à internet passe por um Proxy e ele esteja habilitado, esse também deverá ser configurado no arquivo **.ini** do servidor TSS.

* Segue abaixo a seção e os respectivos parâmetros para configuração no arquivo **.ini** do servidor TSS:

**[PROXY]**

Enable=1

Server=endereço do proxy

Port=porta do proxy

User=domínio\login usuário

Password=senha do usuário no Proxy
