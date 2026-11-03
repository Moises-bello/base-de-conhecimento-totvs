---
content_hash: 9a85bb43e14aaaa9ca037efc28d21f385595e633df06b60c0e1c7aa1d9897557
fetched_at: '2026-06-28T21:35:26.873229+00:00'
page_id: '437265941'
product: fluig
source: tdn-fluig
title: Descoberta de serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=437265941
version: 6
---

Atenção

Esta página foi revisada para considerar as configurações do TOTVS Fluig Plataforma a partir da **atualização Liquid - **1.6.5****.

# Índice

true.\*ndicenone

# Objetivo

---

Este guia tem o objetivo de apresentar o procedimento de liberação de acesso ao registro de serviços, para que eles possam ser localizados pelo serviço de descoberta de serviços.

# Introdução

---

A partir da **atualização Liquid - 1.6.5**, a plataforma dispõe de um modelo de serviços independentes para dar suporte à próxima geração de aplicativos. Para que estes serviços se comuniquem entre si, é necessário um serviço de descoberta. Este serviço conhece todos os demais serviços, desde que cada um dos serviços seja registrado no serviço de descoberta. Para que este processo seja possível, cada serviço dispõe de um cliente de descoberta de serviço e no momento de inicialização da plataforma, o mesmo se registra e fica disponível para os demais serviços.

# Serviços

---

Os serviços disponibilizam e se comunicam com outros serviços através de [APIs REST](https://api.fluig.com/) pelas requisições do protocolo HTTP. Seguindo a premissa de independência entre os serviços, um serviço não tem conhecimento / relacionamento com os outros serviços.

Um exemplo de novos serviços disponibilizados neste modelo, estão disponíveis no menu **Soluções**.

Estas soluções podem se comunicar entre si, entre as APIs da plataforma e a própria infraestrutura para suportar os serviços.

# Registro

---

Um dos serviços da infraestrutura é o Discovery. Ele é o responsável por registrar e fornecer informações sobre os serviços registrados. Para que o registro ocorra com sucesso, é necessário que a plataforma disponibilize acesso a este serviço de registro. Então o cliente de registro irá estabelecer a comunicação através da URL da plataforma configurada no painel de controle.

Caso esta URL não esteja disponível para conexão interna, o cliente do Discovery ainda vai tentar pelo endereço IP configurado no arquivo **domain.xml**localizado no diretório**[diretório\_instalação]/appserver/domain/configuration**.

actionscript3








]]>

Caso ainda não seja possível a comunicação, poderá aparecer no log do servidor uma mensagem como:

Server:fluig1] 11:19:51,485 WARN [com.fluig.core.discovery.client.ServiceDiscoveryClient] (Timer-12) Discovery not available yet for storage. Cause: FLUIG\_REST\_CLIENT\_500. Help: Make sure that the server where fluig is installed has access to the address: http://127.0.1.1:8080. Verifique se o servidor onde está instalada a plataforma tem acesso ao endereço: http://127.0.1.1:8080

No caso de aparecer frequentemente a mensagem acima no log, será necessário tomar a ação abaixo:

1. Configurar o endereço externo no host do servidor
