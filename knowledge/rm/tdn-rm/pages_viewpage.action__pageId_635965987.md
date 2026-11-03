---
content_hash: 34b38283ea22f02a6a7d867f58ed72b6b990cb8005a36c0914b9d2853b17125b
fetched_at: '2026-06-29T00:11:06.857408+00:00'
page_id: '635965987'
product: rm
source: tdn-rm
title: PDC - Parametrização - multiTenant
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=635965987
version: 6
---

### Introdução

---

O Pdc a partir da versão 12.1.33, estará pronto para trabalhar com ambientes multiTenant. Para maiores informações sobre esse tipo de ambiente, favor [clicar aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=287079669).

### Configurações para parametrização

---

[Ao montar o servidor do PDC](https://tdn.totvs.com/pages/viewpage.action?pageId=435105274) precisaremos, além de definir a porta e endereço da frameHTML como [orientado aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105274), devemos também definir o host como mostra a imagem abaixo:

Onde o parâmetro **Nome do host** é o subdomínio que será acessado via Url pelo PdC.

Deveremos também deifnir na pasta FrameHTML um arquivo config chamado app.config com a seguinte informação:

xml


]]>

Além desta modificação, o arquivo Web.config da pasta FrameHTML web deverá conter na linha de <appsettings/> a seguinte informação:

xml]]>

Feitas estas modificações, o PdC estará pronto para acessar o banco em formato multiTenant, onde o subdomínio será o alias do banco que será acessado, exemplo:

[https://pdc.dominio/FrameHTML/Web/App/Imb/PortalCliente/#/](https://prj-gcadbh.rm.cloudtotvs.com.br/FrameHTML/Web/App/Imb/PortalCliente/#/)

Onde pdc é o subdomínio definido como nome do host.

Importante: O arquivo alias.dat deve possuir o nome do banco idêntico ao Nome do host, caso esteja diferente não será possível a conexão.

Verificar também se o Host está no mesmo servidor que o Portal, caso esteja em outro servidor, não esquecer de alterar a tag Host, colocando como valor o endereço de onde está o host. Verificar também se a porta do servidor está aberta para conexão externa

xml]]>
