---
content_hash: 97f6926dd6e85a6068e0d3ae34cc55073bbe16071845a2da7bf42d2a7a480024
fetched_at: '2026-06-29T00:11:12.656837+00:00'
page_id: '656059783'
product: rm
source: tdn-rm
title: Serviços‎ 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656059783
version: 9
---

Segue a descrição dos principais serviços e como parametrizá-los no Portal de Imóveis:

#FF9000COMUNICAÇÃO COM TOTVS RM

Para que o Portal de Imóveis se comunique com o banco de dados do TOTVS, ele utiliza os serviços do HOST do RM, portanto estes devem estar habilitados no servidor de aplicação do TOTVS RM. 

Para habilitar os Serviços do HOST RM vide documento no link abaixo:

[http://tdn.totvs.com/pages/releaseview.action?pageId=89620766](https://tdn.totvs.com/pages/releaseview.action?pageId=89620766)

#FF9000ENVIO DE EMAILS

O Portal de Imóveis tem a possibilidade de envio de e-mails para seus usuários e ou clientes, portanto o servidor de aplicação do portal deve ter as portas de comunicação com o provedor de e-mails do cliente liberada no firewall.

#FF9000COMUNICAÇÃO COM SERVIDOR DE LICENÇAS DO PORTAL DE IMÓVEIS

Para leitura das licenças de uso adquiridas pelo cliente, favor, consultar a documentação: [Portal de Imóveis - Wizard de Instalação](https://tdn.totvs.com/pages/viewpage.action?pageId=633320979)

#FF9000GOOGLE MAPS

Para que localidades de mapas sejam demonstradas no Portal de Imóveis o servidor WEB do portal deve ter acesso a URL´s de validação do GEOCODE do Google

[https://maps.googleapis.com](https://maps.googleapis.com/)/

[http://maps.google.com/](https://maps.google.com/)

[https://drive.google.com](https://drive.google.com/)/

#FF9000LOCALIZAÇÃO DE ENDEREÇOS

Para que o Portal de Imóveis encontre os endereços através do CEP digitado o servidor deve ter acesso aos sites 

[www.cepaberto.com](http://www.cepaberto.com/)

[postmon.com.br](http://postmon.com.br/)
