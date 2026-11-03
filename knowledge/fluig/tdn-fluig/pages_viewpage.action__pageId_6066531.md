---
content_hash: 57bc2ad0dc0967c81f9e342c1a60ee8c4082e2f20b857ec39efaeafd9bbbfe75
fetched_at: '2026-06-28T21:35:27.905214+00:00'
page_id: '6066531'
product: fluig
source: tdn-fluig
title: Visão ESB Servers
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6066531
version: 17
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

### ESB Servers

A **visão ESB Servers** dentro da perspectiva TOTVS ESB tem como finalidade realizar configurações específicas para cada o servidor Fluig ESB.

Detalhes como portas, configurações do monitor, logs e memória do Fluig ESB são realizadas através dessa perspectiva. Ainda permite o gerenciamento de vários servidores Fluig ESB localizados remotamente.

### Interface

Ao abrir a **visão ESB Servers**, tem-se duas áreas distintas. O painel à esquerda demonstra uma listagem de servidores Fluig ESB cuja finalidade é cadastrar e conectar ao servidor Fluig ESB para realizar configurações necessárias. Na listagem tem-se um item raiz denominado **Servers**. Para cadastrar deve-se seguir os passos abaixo.

* Clicar com o botão direito em cima do item **Servers**.
* Selecionar o item **ESB** e o subitem **ESB Server**.
* Ao clicar aparecerá uma janela contendo os seguintes campos que deverão ser preenchidos:

| Campo | Descrição |
| --- | --- |
| **Server Name** | Descreve o nome do servidor Fluig ESB. Deverá ser um nome de fácil identificação. |
| **Host** | Nome ou IP da máquina que se encontra instalado o servidor Fluig ESB. |
| **Port** | Número da porta de conexão ao servidor Web Service configurado no Fluig ESB.  Por padrão, a porta configurada para o servidor Web Service do Fluig ESB é 8085. |

* Após preencher as informações clicar no botão **Finish**.

Com os procedimentos adotados, aparecerá o novo item cadastrado na listagem de servidores Fluig ESB. Para conectar ao servidor ESB cadastrado com finalidade de realizar as configurações necessárias, basta clicar duas vezes sobre o item na listagem.

Ao conectar com o servidor Fluig ESB, irá carregar no painel central do Editor as configurações do servidor ESB. As configurações disponíveis são:

* [System Properties](http://tdn.totvs.com/display/fluig/System+Properties)




* Cluster Configuration

Após configurar o servidor Fluig ESB conforme desejado, pode-se salvar e aplicar no servidor Fluig ESB através do menu principal **File** e item **Save**.
