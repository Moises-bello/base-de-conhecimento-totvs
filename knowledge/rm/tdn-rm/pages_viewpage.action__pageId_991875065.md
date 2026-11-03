---
content_hash: d52af0424ba8751b5281577bff020d37e6842275dac9df1e69f73a90cedf183a
fetched_at: '2026-06-29T00:12:16.521523+00:00'
page_id: '991875065'
product: rm
source: tdn-rm
title: Instalação e configuração do Rewrite e do ARR (Application Request Routing)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=991875065
version: 6
---

## **01. INSTALAÇÃO DO REWRITE E DO ARR (APPLICATION REQUEST ROUTING)**

Como requisito para o funcionamento do portal é necessário instalar o **URL Rewrite** e **ARR (Application Request Routing)** no IIS.

### **ARR (Application Request Routing)**

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do ARR**:  <https://www.microsoft.com/en-us/download/details.aspx?id=47333> 

Apenas uma vez para cada IIS

**A instalação deve ser realizada apenas uma vez para cada IIS.**

Após finalizar a instalação **ARR (Application Request Routing),** deverá ser **habilitado** a propriedade **"Enable proxy"**

### **URL Rewrite**

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do URL Rewrite**: <https://www.iis.net/downloads/microsoft/url-rewrite>

Após a Instalação, será criado um ícone: “**URL Rewrite**” no IIS

Após configurar o servidor, é necessário configurar o arquivo de configuração do Host do RM. Para isso, acesse o arquivo **RM.Host.Service.exe.config** que está disponível no caminho padrão do instalador do RM.exe.

Inserir as chaves as chaves abaixo:

      <add key="**ApiPort**" value=**"porta\_definida\_no\_rewrite (IIS)"** />  
      <add key="**DefaultDB**" value=**"informe\_aqui\_o\_nome\_do\_alias"** />

O usuário associado ao **serviço** tem que ter **permissão** para acessar a porta da **API** definida no **URL Rewrite**.

## **02. CONFIGURAÇÃO** **DO REWRITE**

Acessar o IIS -> Ir no aplicativo FrameHTML -> Abrir até a pasta do Portal Processo Seletivo -> URL Rewrite

Editar as informações da regra criada:

Editar a URL de ação do Rewrite e incluir o nome do servidor e a porta de comunicação configurada na tag "**ApiPort**" do arquivo de configuração do Host.

Após esses ajustes a tag do rewrite com o **nome da máquina** no arquivo configuração na pasta "..\FrameHTML\web\app\Edu\portalprocessoseletivo" é ajustado:

js









]]>

Pelo instalador de portais essa tag já vem configurada.

Verificar a porta configurada na tag ApiPort do arquivo de configuração do Host, por padrão é usada a porta 8051.

Importante

Após realizar as configurações, é necessário reiniciar o IIS
