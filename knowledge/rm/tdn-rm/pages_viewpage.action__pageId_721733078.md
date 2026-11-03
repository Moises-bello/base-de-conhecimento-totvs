---
content_hash: a6eb826d4e7b77dfd55e53a7fa1b651a81092446e7d91f201db3db3d03bff9eb
fetched_at: '2026-06-29T00:11:27.272592+00:00'
page_id: '721733078'
product: rm
source: tdn-rm
title: 'Servidores e Portas API-APP Dashboard:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721733078
version: 6
---

Após a instalação da BibliotecaRM, serão criados :

**a)** Pasta do **dashboard**.

Criada no caminho definido pelo usuário no momento da instalação.

**Exemplo:**

* C:\totvs\CorporeRM\RM.Net\wwwroot\dashboard

**b)** Tags **HTTPPort** e **ApiPort** no **RM.Host.config**.

**Exemplo:**

* <add key="HTTPPort" value="8051" />
* <add key="ApiPort"    value="8052" />

**Importante:**Para visualizar as informações do "Dashboard " é obrigatório que  o **HOST** seja iniciado como administrador, caso contrário, será demonstrada na tela a mensagem para o usuário  "carregando" e nada será exibido.
