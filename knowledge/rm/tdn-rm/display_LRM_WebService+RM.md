---
content_hash: ec0c211333703ee831ea39e3aa1dcd8eb86a36d166941fdc43c423a5bd0a05c5
fetched_at: '2026-06-29T00:06:24.202004+00:00'
page_id: '224114650'
product: rm
source: tdn-rm
title: WebService RM
type: documentation
url: https://tdn.totvs.com/display/LRM/WebService+RM
version: 132
---

# WebService RM

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.80 , 12.0 |
| **Passo a passo:** | **Objetivo:**  O objetivo deste guia é apresentar como expor o WebService do RM através do RM.Host.Service.  ****Introdução:****  O WebService do RM é iniciado em conjunto com o serviço do Host. Quando o Host é inicializado ele cria o serviço do WebService por default na porta 8051, caso o arquivo de configuração do host possua a tag "<add key="**HttpPort**" value="8051" />" o serviço será criado na porta informada. 1Verificar o Serviço do WebServiceVerificar o Serviço do WebService Para verificar se o serviço está funcionando basta acessar a página [http://bhd0003447:8051/WsPageIndex/](http://localhost:8051/WsPageIndex/), deve ser exibida a página da TOTVS contendo os serviços do WebService do RM.      Caso a a página não esteja disponível é necessário reservar a porta para o usuário executor do serviço do Host.   Ambientes que utilizam SSL Ambientes que utilizam SSL  Em ambientes que utilizam SSL o link muda para:  **[https://<SERVIDOR>:8051/wsPageIndex/Index](https://servidor_na_nuvem:8051/wsUpdate/Index)**      Para reservar a porta é necessário executar no prompt de comando uma linha de comando, informando a porta e o usuário executor do serviço do host.      **Linha de Comando**: netsh http add urlacl url=http://+:**8051**/ user=**NetworkService** Alias DefaultAlias Default Para configurar o Alias Default é necessário incluir a tag DefaultDB no arquivo de configuração do Host.  Acesse a máquina ou servidor que está executando o serviço.  Vá ao diretório **C:\totvs\CorporeRM\RM.Net** e edite o arquivo **RM.Host.Service.exe.config**.      Inclua a tag **<add key="DefaultDB" value="CorporeRM" />** dentro da limitação **appSettings**.  O valor a ser atribuído a tag **DefaultDB** deve ser idêntica ao nome do alias que aponta para a base de dados utilizada. No nosso exemplo que citamos atribuímos o valor "**CorporeRM**" ao alias e respectivamente ao **DefaultDB**. xmlRM.Host.Service.exe.Config                ]]>Atenção  Para que estas configurações entrem em vigor será necessário reiniciar o serviço do Host.    Após reiniciar o serviço basta [verificar o serviço](http://localhost:8051/WsPageIndex/) do WebService, se o DEFAULTDB estará configurado com o alias informado. |

divs
