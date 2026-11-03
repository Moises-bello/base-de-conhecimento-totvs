---
content_hash: 237adf48e7485ed712a452d1577114e8b9857ea689de2559fac44ca9fbffa4ee
fetched_at: '2026-06-29T00:11:39.974308+00:00'
page_id: '793183883'
product: rm
source: tdn-rm
title: Rastreabilidade de IP público (Termo de aceite / Assinatura contrato)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=793183883
version: 10
---

Ao realizar o aceite do termo na inscrição via portal do **Processo Seletivo** ou assinatura do contrato de matricula via **Central do Candidato** é necessário guardar qual o **IP público** que originou a requisição do aceite, portanto esse documento tem como objetivo esclarecer como esse procedimento é executado no **Portal do TOTVS Processo Seletivo**.

Clique em  ou [Assinatura do contrato](https://tdn.totvs.com/display/LRM/02.06+Assinatura+do+contrato) para conhecer mais sobre o recurso.

Como padrão o **Portal do TOTVS Processo Seletivo** utiliza o recurso Open Source do API ipify (<https://api.ipify.org/>) para obter o endereço de IP Publico, no entanto é permitido ao cliente modificar a configuração do arquivo do arquivo **totvs-app.global.config** para que o IP seja recuperado da requisição HTTP enviada para o RM ao realizar o aceite (neste caso não será utilizado o API ipify ).

Se optar em **NÃO** utilizar o API ipify, edite o arquivo **totvs-app.global.config (**disponível nas pasta de instalação ..\FrameHTML\web\js**)** e adicione a linha do exemplo abaixo.

bashX-Forwarded-For

É importante ressaltar que se servidor web onde está hospedado o portal estiver utilizando algum proxy com balanceador de carga é reponsabilidade do cliente configurar o mesmo para que o cabeçalho [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) seja considerado para preservar o IP da requisição inicial.
